from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Player, Game, GamePlayerScore


class MainView(View):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        return render(request, 'main.html', {'players':players})


class ViewGames(View):
    def get(self, request, *args, **kwargs):
        games = Game.objects.all()
        res_games = {}
        for game in games:
            if str(game.game_id) in res_games.keys():
                res_games[str(game.game_id)].append(game)
            else:
                res_games[str(game.game_id)] = [game]
        return render(request, 'games.html', {'games': res_games})

class AddGame(View):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        return render(request, 'add.html', {'players':players})

    def get_game_id(self):
        last_game = Game.objects.all().last()
        if last_game:
            return last_game.game_id + 1
        else:
            return 1


    def save_player_score(self, player, rate):
        player.total_rate += rate
        player.save()

    def post(self, request, *args, **kwargs):
        names = []
        rates = []
        names.append(request.POST.get('name_one', ''))
        names.append(request.POST.get('name_two', ''))
        names.append(request.POST.get('name_three', ''))
        names.append(request.POST.get('name_four', ''))
        rates.append(request.POST.get('rate_one', ''))
        rates.append(request.POST.get('rate_two', ''))
        rates.append(request.POST.get('rate_three', ''))
        rates.append(request.POST.get('rate_four', ''))

        if names[0] == names[1] or names[0] == names[2] or names[0] == names[3] or names[1] == names[2] or \
            names[1] == names[3] or names[2] == names[3]:
            players = Player.objects.all()
            error = "ERROR PLAYERS NAME"
            return render(request, 'add.html', {'players': players, 'error':error})

        if int(rates[0]) + int(rates[1]) + int(rates[2]) + int(rates[3]) != 0:
            players = Player.objects.all()
            error = "ERROR SUM OF POINTS MUST BE 0"
            return render(request, 'add.html', {'players': players, 'error':error})

        game_id = self.get_game_id()
        try:
            for i in range(4):
                player = Player.objects.get(name=names[i])
                self.save_player_score(player, int(rates[i]))
                player_score = GamePlayerScore.objects.create(player=player, game_score=rates[i])
                Game.objects.create(game_player_scores=player_score, game_id=game_id)

            # first_player = Player.objects.get(name=names[0])
            # self.save_player_score(first_player,int(rates[0]))
            # second_player = Player.objects.get(name=names[1])
            # self.save_player_score(second_player, int(rates[1]))
            # third_player = Player.objects.get(name=names[2])
            # self.save_player_score(third_player, int(rates[2]))
            # fourth_player = Player.objects.get(name=names[3])
            # self.save_player_score(fourth_player, int(rates[3]))
            #
            # game = Game.objects.create(first_player=first_player, second_player=second_player, third_player=third_player,
            #                            fourth_player=fourth_player, first_rate=rates[0], second_rate=rates[1],
            #                            third_rate=rates[2], fourth_rate=rates[3])


        except Exception as e:
            players = Player.objects.all()
            error = "ERROR " + str(e)
            return render(request, 'add.html', {'players': players, 'error': error})

        players = Player.objects.all()
        return render(request, 'add.html', {'players':players})
