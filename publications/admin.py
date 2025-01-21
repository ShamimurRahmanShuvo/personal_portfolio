from django.contrib import admin
from publications.models import Publication


# Register your models here.
class PublicationAdmin(admin.ModelAdmin):
    pass


admin.site.register(Publication, PublicationAdmin)
