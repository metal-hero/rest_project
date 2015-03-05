from django.contrib import admin
from question.models import *

admin.site.register(Question)
admin.site.register(Post)
admin.site.register(Comment)


from django.contrib.auth.models import User, Group
admin.site.unregister(User)
admin.site.unregister(Group)

# Register your models here.
