from django.contrib import admin

# Register your models here.
from reviewer.reviews.models import (Company,
                                     Review,
                                     )


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class ReviewAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Review._meta.fields]


admin.site.register(Company, CompanyAdmin)
admin.site.register(Review, ReviewAdmin)
