from django.urls import path
from . import issue,player

urlpatterns = [
    path('issue', issue.issue.as_view()),
    path('player', player.player.as_view()),
]