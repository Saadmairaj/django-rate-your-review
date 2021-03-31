from datetime import datetime
from django.conf import settings
from django.dispatch import receiver
from django.views.generic.edit import FormView
from django.db.models.signals import post_save
from django.views.generic import ListView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
from .forms import ReviewForm, RegisterForm

# Tensorflow imports
from tensorflow import keras
from tf.utils import (add_padding, encode_review,
                      modify_word_index, filter_text)


# Post save function callback to predict
# the rating with tensorflow.
@receiver(post_save, sender=Review)
def predict(sender, **kw):
    print(kw)
    obj = kw['instance']
    model = keras.models.load_model("tf/model.h5")
    word_index = modify_word_index()
    review = filter_text(obj.text)
    encode = add_padding([encode_review(review, word_index)],
                         value=word_index['<PAD>'], maxlen=250)
    # updating the rating like below to stop recursion.
    Review.objects.filter(
        id=obj.id).update(rating=(
            model.predict(encode)[0][0]) * (
                settings.RATING_OUT_OF/10), 
                last_updated=datetime.now())


class RegisterView(FormView):
    form_class = RegisterForm
    model = UserCreationForm
    template_name = 'review/register.html'
    success_url = "/login"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ReviewView(FormView):
    model = Review
    form_class = ReviewForm
    template_name = "review/review.html"
    success_url = "/update-review"

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not self.request.user.is_anonymous:
            obj.user = self.request.user
        form.save()
        self.success_url += ("/%s" % obj.pk)
        return super().form_valid(form)


class EditReviewView(LoginRequiredMixin, UpdateView):
    form_class = ReviewForm
    model = Review
    template_name = 'review/edit-review.html'
    success_url = "/update-review"
    login_url = '/login'
    redirect_field_name = "redirect_to"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["current_review_rating"] = "{:.2f}".format(
            (self.get_object().rating))
        rating = int(float(context["current_review_rating"]) * 10)
        context["rating_star_loop"] = [
            0 for i in range(settings.RATING_OUT_OF)]
        for i in range(rating):
            context["rating_star_loop"][i] = 1
        return context

    def get_success_url(self):
        url = super().get_success_url()
        obj = self.get_object()
        return url + ("/%s" % obj.pk)


class Histroy(LoginRequiredMixin, ListView):
    model = Review
    fields = "__all__"
    template_name = 'review/history.html'
    context_object_name = 'reviews'
    paginate_by = 10
    login_url = '/login'
    redirect_field_name = "redirect_to"

    def get_queryset(self):
        query_set = self.model.objects.filter(
            user=self.request.user).order_by("-date_created")
        return query_set
    