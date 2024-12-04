from django.contrib import admin
from .models import Cliente, Doce, Pedido, DocesPedido
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Doce)
admin.site.register(Pedido)
admin.site.register(DocesPedido)