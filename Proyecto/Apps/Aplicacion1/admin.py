from django.contrib import admin
from .models import Categoria, Producto

# Personalización para el modelo Categoria
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')  # Campos a mostrar en la lista de categorías
    search_fields = ('nombre',)  # Permite buscar por nombre de la categoría

# Personalización para el modelo Producto
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'stock')  # Campos a mostrar en la lista de productos
    list_filter = ('categoria',)  # Filtrar productos por categoría
    search_fields = ('nombre', 'descripcion')  # Buscar por nombre o descripción del producto

# Registro de los modelos en el Administrador
admin.site.register(Categoria)
admin.site.register(Producto)
