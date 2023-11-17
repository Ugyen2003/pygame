# Unit test for pygame

import unittest
import pygame
from unittest.mock import MagicMock
import unittest

def start_game(mode):
    global cells, cell_width, cell_height, show_start_screen

    if mode == 'normal':
        show_start_screen = False
    elif mode == 'demo':
        show_start_screen = True
    else:
        show_start_screen = False  

class TestPygame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        pygame.display.set_caption('Test Window')
class TestStartGame(unittest.TestCase):

    def tearDown(self):
        pygame.quit()
    def test_start_game_normal_mode(self):
        global show_start_screen
        start_game('normal')
        self.assertFalse(show_start_screen)

    def test_start_game(self):
        start_game(3)
        
    def test_start_game_demo_mode(self):
        global show_start_screen
        start_game('demo')
        self.assertTrue(show_start_screen)

    def test_handle_mouse_clicks(self):
        cells = [{'rect': pygame.Rect(0, 0, 100, 100), 'border': (255, 255, 255), 'order': 0, 'pos': 0},]
    def test_start_game_default_mode(self):
        global show_start_screen
        start_game('unknown')
        self.assertFalse(show_start_screen)  

        # Simulate a mouse click event
        pygame.mouse = MagicMock()
        pygame.mouse.get_pos.return_value = (50, 50)
        pygame.mouse.get_pressed.return_value = (1, 0, 0)

        # Call the function that handles mouse clicks
        # handle_mouse_clicks(cells)
if __name__ == '__main__':
    pygame.init()  

        # Perform assertions to check if the expected cell gets selected or not
    cells = None  
    cell_width = None  
    cell_height = None  
    show_start_screen = False  

if __name__ == '__main__':
    unittest.main()



