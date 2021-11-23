from django.contrib import admin
from .models import Review, Consent

# Register your models here.


@admin.register(Consent)
class ConsentAdmin(admin.ModelAdmin):
    list_display = ('status', 'user')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'rating', 'date_created', 'last_updated')
    readonly_fields = ('rating', )
