from django.contrib import admin
from .models import Categoria, Tecnologia, Proyecto, Contacto

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Tecnologia)
admin.site.register(Proyecto)
admin.site.register(Contacto)
