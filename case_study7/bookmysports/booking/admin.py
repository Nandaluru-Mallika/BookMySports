from django.contrib import admin
from .models import Match, Invoice

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display = ["match_name", "match_venue"]

admin.site.register(Match, MatchAdmin)

admin.site.register(Invoice)
