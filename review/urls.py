from django.urls import path
from review import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.ReviewView.as_view(), name="home"),
    path('register', views.RegisterView.as_view(), name="register"),
    path('logout', auth_views.LogoutView.as_view(
        template_name='review/logout.html'), name="logout"),
    path('login', auth_views.LoginView.as_view(
        template_name='review/login.html', 
        success_url="/home"), name="login"),
    path('update-review/<int:pk>', views.EditReviewView.as_view(), name="update-review"),
    path("history", views.Histroy.as_view(), name="history"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)