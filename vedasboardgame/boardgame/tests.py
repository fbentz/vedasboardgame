from django.test import TestCase
from .models import BoardGame, EditorGame


class BoardGameTest(TestCase):
    def test_create_a_board_game(self):
        editor = EditorGame(name="Iello")
        boardgame = BoardGame(name="Le village de tiercelieux", min_player=1,
                              max_player=18,
                              description="Lorem ipsum dolor sit amet",
                              editor=editor)
        self.assertEqual(boardgame.name, "Le village de tiercelieux")
        self.assertEqual(boardgame.min_player, 1)
        self.assertEqual(boardgame.max_player, 18)
        self.assertEqual(boardgame.description, "Lorem ipsum dolor sit amet")


class EditorGameTest(TestCase):
    def test_create_a_editor_game(self):
        editor = EditorGame(name="Iello")
        self.assertEqual(editor.name, 'Iello')
