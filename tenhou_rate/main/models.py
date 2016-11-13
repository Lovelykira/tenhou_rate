from django.db import models
from django.contrib import admin

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rate = models.IntegerField(default=0)


class PlayerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Player, PlayerAdmin)