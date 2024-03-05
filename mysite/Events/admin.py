from django.contrib import admin

# Register your models here.
from .models import Venue, MyclubUser, Events


# admin.site.register(venue)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):

    list_display = ('name', 'address', 'phone')
    ordering = ('-name',)
    search_fields = ('name', 'address')
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': ('name', 'address', 'zip_code', 'phone')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('web', 'email_address')
        }),
    )


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    # fields = (('name','venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('event_date', 'venue')
    ordering = ('-event_date',)
    fieldsets = (
        ('Required Information', {
            'description': "These fields are required for each event.",
            'fields': (('name', 'venue'), 'event_date')
        }),
        ('Optional Information', {
            'classes': ('collapse',),
            'fields': ('description', 'manager')

        }),
    )

admin.site.register(MyclubUser)
# admin.site.register(Events)
