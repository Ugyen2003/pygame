# Unit test for pygame

import pygame
import unittest

def start_game(mode):
    global cells, cell_width, cell_height, show_start_screen
    
    if mode == 'normal':
        show_start_screen = False
    elif mode == 'demo':
        show_start_screen = True
    else:
        show_start_screen = False  


class TestStartGame(unittest.TestCase):

    def test_start_game_normal_mode(self):
        global show_start_screen
        start_game('normal')
        self.assertFalse(show_start_screen)

    def test_start_game_demo_mode(self):
        global show_start_screen
        start_game('demo')
        self.assertTrue(show_start_screen)

    def test_start_game_default_mode(self):
        global show_start_screen
        start_game('unknown')
        self.assertFalse(show_start_screen)  


if __name__ == '__main__':
    pygame.init()  

    cells = None  
    cell_width = None  
    cell_height = None  
    show_start_screen = False  

    unittest.main()


    