from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('isim','user','slug','id')
    list_display_links = ('id','user')
    search_fields = ('isim',)
    list_editable = ('isim',)
    list_per_page = 5 #sayfa başı gösterilecek olan eleman sayısı
    list_filter = ('isim','user')
    readonly_fields = ('slug',)
    
# Register your models here.
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Account)