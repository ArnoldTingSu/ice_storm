from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register', views.register),
    path('guilds', views.guilds),
    path('login', views.login),
    path('guild/<int:guild_id>/roster', views.guild_roster),
    path('guild/<int:guild_id>/edit', views.guild_roster_edit),
    path('guild/<int:guild_id>/member/<int:player_id>', views.player_profile),
    path('karazhan', views.karazhan)

]