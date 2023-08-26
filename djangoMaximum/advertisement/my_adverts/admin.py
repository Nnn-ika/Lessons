from django.contrib import admin
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'price', 'location', 'created_date', 'updated_date', 'auction']
    list_filter = ['price', 'location', 'auction']
    actions = ['forbid_the_action', 'permit_the_action']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'description', 'location', 'category')
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes' : ['collapse']
        }),
    )

    @admin.action(description="Убрать возможность торга")
    def forbid_the_action(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def permit_the_action(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)