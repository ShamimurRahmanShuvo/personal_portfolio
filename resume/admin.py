from django.contrib import admin
from resume.models import Summary, Education, Experience, JobResponsibility


# Register your models here.
class ResumeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Summary, ResumeAdmin)
admin.site.register(Education, ResumeAdmin)
admin.site.register(Experience, ResumeAdmin)
admin.site.register(JobResponsibility, ResumeAdmin)
