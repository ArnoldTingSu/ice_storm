from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def guilds(request):
    return render(request, 'guilds.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def guild_roster(request, guild_id):
    return render(request, 'guild_roster.html')

def guild_roster_edit(request, guild_id):
    return render(request, 'guild_roster_edit.html')

def player_profile(request, guild_id, player_id):
    return render(request, 'player_profile.html')