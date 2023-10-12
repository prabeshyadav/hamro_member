from django.contrib import admin
from .models import CustomUser,Registration,Events,Member,Membership,Manager
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Registration)
admin.site.register(Events)
admin.site.register(Member)
admin.site.register(Membership)
admin.site.register(Manager)



