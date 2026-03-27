"""Mapa del laberinto."""

from .constants import CELL_PATH, CELL_WALL, CELL_EXIT

# Mapa: 0 = camino, 1 = muro, 2 = salida
_RAW_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class GameMap:
    """Representa el laberinto del juego."""

    def __init__(self):
        """Inicializa el mapa."""
        self._map = [row[:] for row in _RAW_MAP]  # Copia independiente
        self.width = len(self._map[0])
        self.height = len(self._map)

    def get_tile(self, x: int, y: int) -> int:
        """
        Obtiene el tipo de celda en las coordenadas dadas.

        Args:
            x: Coordenada X (columna)
            y: Coordenada Y (fila)

        Returns:
            int: Tipo de celda (0: camino, 1: muro, 2: salida)
        """
        if 0 <= y < self.height and 0 <= x < self.width:
            return self._map[y][x]
        return CELL_WALL  # Fuera de límites se considera muro

    def is_wall(self, x: int, y: int) -> bool:
        """Verifica si una celda es un muro."""
        return self.get_tile(x, y) == CELL_WALL

    def is_exit(self, x: int, y: int) -> bool:
        """Verifica si una celda es la salida."""
        return self.get_tile(x, y) == CELL_EXIT

    def reset(self):
        """Reinicia el mapa a su estado original."""
        self._map = [row[:] for row in _RAW_MAP]