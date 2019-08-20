from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.
# class PersonAdmin(admin.ModelAdmin):
#     form = PersonForm

# admin.site.register(Person, PersonAdmin)

class CountryAdmin(admin.ModelAdmin):
    form = CountryForm

admin.site.register(Country, CountryAdmin)


def user_gains_perms(request, user_id):
    permission = Permission.objects.get(name='Country')
    user.user_permissions.add(permission)