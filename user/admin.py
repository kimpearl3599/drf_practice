from user.models import User, UserCart, Market
from django.contrib import admin
from django.contrib.auth.models import Group

admin.site.unregister(Group)


class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'item')


admin.site.register(User)
admin.site.register(UserCart)
admin.site.register(Market, MarketAdmin)
