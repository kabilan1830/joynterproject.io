from django.contrib import admin
from.models import College, clgsignin, course, feedback, unisignin
from.models import stdsignin
from.models import stdregister
from.models import addstd
from.models import course
# Register your models here.
admin.site.register(feedback)
admin.site.register(stdsignin)
admin.site.register(clgsignin)
admin.site.register(unisignin)
admin.site.register(stdregister)
admin.site.register(addstd)
admin.site.register(course)
admin.site.register(College)
