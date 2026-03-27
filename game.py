"""Lógica principal del juego."""

import pygame
from .constants import (
    WIDTH, HEIGHT, TILE_SIZE, FPS,
    WHITE, BLACK, GREEN, RED, PLAYER_COLOR,
    CELL_WALL, CELL_EXIT
)
from .map import GameMap
from .player import Player


class Game:
    """Controla el estado y la ejecución del juego."""

    def __init__(self):
        """Inicializa el juego."""
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ninja of the Lost Labyrinth")
        self.clock = pygame.time.Clock()

        self.game_map = GameMap()
        self.player = Player()
        self.won = False
        self.running = True

    def _handle_events(self):
        """Procesa los eventos de entrada."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset()

                if not self.won:
                    if event.key == pygame.K_UP:
                        self.player.move(0, -1, self.game_map)
                    elif event.key == pygame.K_DOWN:
                        self.player.move(0, 1, self.game_map)
                    elif event.key == pygame.K_LEFT:
                        self.player.move(-1, 0, self.game_map)
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(1, 0, self.game_map)

    def _update(self):
        """Actualiza el estado del juego."""
        if not self.won:
            if self.game_map.is_exit(self.player.x, self.player.y):
                self.won = True

    def _draw_map(self):
        """Dibuja el laberinto."""
        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                tile = self.game_map.get_tile(x, y)
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

                if tile == CELL_WALL:
                    pygame.draw.rect(self.screen, GREEN, rect)
                elif tile == CELL_EXIT:
                    pygame.draw.rect(self.screen, RED, rect)

    def _draw_player(self):
        """Dibuja al jugador."""
        pygame.draw.rect(
            self.screen,
            PLAYER_COLOR,
            (self.player.x * TILE_SIZE, self.player.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

    def _draw_victory_text(self):
        """Dibuja el mensaje de victoria."""
        font = pygame.font.SysFont(None, 48)
        text = font.render("¡ESCAPASTE!", True, WHITE)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.screen.blit(text, text_rect)

        font_small = pygame.font.SysFont(None, 24)
        restart_text = font_small.render("Presiona R para reiniciar", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
        self.screen.blit(restart_text, restart_rect)

    def _draw(self):
        """Dibuja todos los elementos en pantalla."""
        self.screen.fill(BLACK)
        self._draw_map()
        self._draw_player()

        if self.won:
            self._draw_victory_text()

        pygame.display.flip()

    def reset(self):
        """Reinicia el juego."""
        self.game_map.reset()
        self.player.reset()
        self.won = False

    def run(self):
        """Bucle principal del juego."""
        while self.running:
            self._handle_events()
            self._update()
            self._draw()
            self.clock.tick(FPS)

        pygame.quit()

    def quit(self):
        """Finaliza el juego."""
        pygame.quit()