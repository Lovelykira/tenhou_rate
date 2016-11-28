from django.db import models
from django.contrib import admin


# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100, unique=True)
    total_rate = models.IntegerField(default=0)

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class GamePlayerScore(models.Model):
    player = models.ForeignKey(Player)
    game_score = models.IntegerField(default=0)


class Game(models.Model):
    date = models.DateTimeField(auto_now=True)
    game_id = models.IntegerField(default=0)
    game_player_scores = models.ForeignKey(GamePlayerScore, related_name='game', null=True)



class PlayerAdmin(admin.ModelAdmin):
    pass


class GameAdmin(admin.ModelAdmin):
    pass


class GamePlayerScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(GamePlayerScore, GamePlayerScoreAdmin)