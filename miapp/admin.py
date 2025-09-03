from django.contrib import admin

from .models import Cliente



# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cli_nombre', 'cli_direccion', 'cli_telefono')
    search_fields = ('cli_nombre', 'cli_telefono')
    list_filter = ('cli_nombre',)
    ordering = ('cli_nombre',)

admin.site.register(Cliente, ClienteAdmin)



