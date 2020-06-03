from django.contrib import admin
from accounts import models as accounts_models
from groups import models as groups_models
from posts import models as posts_models

# Register your models here.
admin.site.register(accounts_models.User)
admin.site.register(groups_models.Group)
admin.site.register(groups_models.GroupMember)
admin.site.register(posts_models.Post)
