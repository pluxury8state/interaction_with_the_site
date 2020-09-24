from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    ordering = ['-id']  # порядок сортировки
    list_display = ('brand', 'model', 'review_count')
    list_filter = ('brand', 'model')
    search_fields = ('brand', 'model')


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ('car', 'title')
    search_fields = ('car__brand', 'car__model', 'title')

admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
