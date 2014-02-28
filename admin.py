from hashlib import md5
from config import app
from config import db
from config import auth
from database import *
from flask import request
from flask import redirect
from flask_peewee.admin import Admin
from flask_peewee.admin import AdminPanel
from flask_peewee.admin import ModelAdmin


class ProductoAdmin(ModelAdmin):
    columns = ("nombre", "precio", "cant",)


class ConsumoAdmin(ModelAdmin):
    columns = ("producto", "usuario", "fecha",
               "cantidad", "precio", "activo",)
    filter_fields = ("fecha",)


class UsuarioAdmin(ModelAdmin):
    columns = ("nombre", "email",)


admin = Admin(app, auth, branding="Drinklogger")
admin.register(Producto, ProductoAdmin)
admin.register(Consumo, ConsumoAdmin)
