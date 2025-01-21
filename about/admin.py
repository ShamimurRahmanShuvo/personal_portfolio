from django.contrib import admin
from about.models import Biography, Skill


# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    pass


admin.site.register(Biography, AboutAdmin)
admin.site.register(Skill, AboutAdmin)
