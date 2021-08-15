from django.contrib import admin
from home.models import *
# Register your models here.

admin.site.register(Standard),
admin.site.register(Category),
admin.site.register(Subject),
admin.site.register(Question),
admin.site.register(Question2),
admin.site.register(UserDetails),
admin.site.register(LeaderBoard)