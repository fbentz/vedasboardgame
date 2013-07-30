from django.views.generic import ListView

from .models import BoardGame


class BoardGameListView(ListView):
    model = BoardGame
    template_name = "boardgame/list.html"
