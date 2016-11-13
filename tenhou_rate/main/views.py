from django.shortcuts import render

# Create your views here.
from django.views import View
from .models import Player


class MainView(View):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        return render(request, 'main.html', {'players':players})

class AddGame(View):
    def get(self, request, *args, **kwargs):
        players = Player.objects.all()
        return render(request, 'add.html', {'players':players})

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

        for i in range(4):
            try:
                player = Player.objects.get(name=names[i])
                # print(player.rate)
                player.rate += int(rates[i])
                # print(player.rate)
                player.save()
            except:
                break

        players = Player.objects.all()
        return render(request, 'add.html', {'players':players})
