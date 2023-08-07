from django.contrib import admin
from .models import Flat, Complain, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building',
                    'construction_year', 'town', )
    list_editable = ('new_building', )
    list_filter = ('new_building', 'rooms_number', 'has_balcony', )
    raw_id_fields = ('liked_by',)
    inlines = [
        OwnerInline
    ]
admin.site.register(Flat, FlatAdmin)


class ComplainAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'text',)
    list_filter = ('user', )
    raw_id_fields = ('flat',)
admin.site.register(Complain)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['flats']
admin.site.register(Owner)