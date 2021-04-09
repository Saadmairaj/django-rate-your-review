from django import template
from datetime import datetime
from django.conf import settings
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def rating(obj=None):
    return 


@register.simple_tag
def limit_text(text, length=200):
    if len(text) >= length:
        return text[:length] + ' ...'
    return text

@register.filter
def time_ago(dateTime):
    current = datetime.now()
    diff = current - dateTime.replace(tzinfo=None)
    minutes = diff.total_seconds()/60
    hours = (diff.total_seconds()/60)/60
    if diff.seconds < 60:
        return "Last updated %s secs ago" %str(round(diff.seconds))
    if minutes < 60:
        return "Last updated %s mins ago" %str(round(minutes))
    if hours < 60:
        return "Last updated %s hrs ago" %str(round(hours))
    return "Last updated %s days ago" %str(diff.days)

@register.filter(is_safe=True)
def star_template(rv):
    current_review_rating = round(rv.rating, 2)
    rating = int(float(current_review_rating * 10))
    rating_star_loop = [0 for i in range(settings.RATING_OUT_OF)]
    for i in range(rating):
        rating_star_loop[i] = 1
    template = ""

    for star in rating_star_loop:
        if star:
            template += '<span class="fa fa-star checked"></span>'
        else:
            template += '<span class="fa fa-star"></span>'
    return mark_safe(template)