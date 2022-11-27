from django.contrib import admin
from .models import Fremmode, States, Medlemmer

# Register your models here.

class MedlemmerAdmin(admin.ModelAdmin):
    "medlems table"
    list_display = ('Medlemsnummer', 'Fornavn', 'Efternavn')

admin.site.register(Medlemmer, MedlemmerAdmin)

class FremmodeAdmin(admin.ModelAdmin):
    "fremmode table"
    list_display = ('Date', 'Medlem', 'State', 'Reason')

admin.site.register(Fremmode, FremmodeAdmin)

class StatesAdmin(admin.ModelAdmin):
    "Tilstande table"
    list_display = ('StateID', 'State', 'Image')

admin.site.register(States, StatesAdmin)
