from django.conf.urls import patterns, url
from .views import BoardGameListView

urlpatterns = patterns(
    '',
    url(r'^$',
        BoardGameListView.as_view(),
        name='boardgamelist'),
)
