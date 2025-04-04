# concerts/admin.py
from django.contrib import admin
from .models import Concert

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('artist', 'date', 'venue', 'price')
    search_fields = ('artist', 'venue')
    list_filter = ('date',)
