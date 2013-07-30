from django.test import TestCase, Client
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


class BoardGameView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_board_game(self):
        response = self.client.get('/boardgames/')
        self.assertEqual(response.status_code, 200)


class EditorGameTest(TestCase):
    def test_create_a_editor_game(self):
        editor = EditorGame(name="Iello")
        self.assertEqual(editor.name, 'Iello')
