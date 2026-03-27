"""Constantes globales del juego."""

import pygame

# --- Configuración de pantalla ---
WIDTH, HEIGHT = 800, 600
TILE_SIZE = 40
FPS = 60

# --- Colores (RGB) ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

# --- Tipos de celdas ---
CELL_PATH = 0
CELL_WALL = 1
CELL_EXIT = 2

# --- Configuración del jugador ---
START_POSITION = [1, 1]
PLAYER_COLOR = BLUE