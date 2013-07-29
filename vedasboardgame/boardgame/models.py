# -*- coding: utf-8 -*-
from django.db import models
#from django.contrib.auth.models import User


class EditorGame(models.Model):
    """
    This class represents a game editor
    """
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = 'editor_game'


class BoardGame(models.Model):
    """
    This class represents a boardgame
    """
    name = models.CharField(max_length=255)
    min_player = models.IntegerField()
    max_player = models.IntegerField()
    description = models.TextField()
    editor = models.ForeignKey(EditorGame, verbose_name="Edité par")

    def __unicode__(self):
        return u'%s' % (self.name)

    class Meta:
        db_table = 'board_game'
