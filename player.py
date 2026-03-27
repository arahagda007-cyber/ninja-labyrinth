"""Clase del jugador."""

from .constants import START_POSITION


class Player:
    """Representa al jugador en el laberinto."""

    def __init__(self):
        """Inicializa al jugador en la posición de inicio."""
        self._x = START_POSITION[0]
        self._y = START_POSITION[1]

    @property
    def x(self) -> int:
        """Posición X del jugador."""
        return self._x

    @property
    def y(self) -> int:
        """Posición Y del jugador."""
        return self._y

    @property
    def position(self) -> tuple:
        """Posición actual como tupla (x, y)."""
        return (self._x, self._y)

    def move(self, dx: int, dy: int, game_map) -> bool:
        """
        Intenta mover al jugador.

        Args:
            dx: Cambio en X (-1, 0, 1)
            dy: Cambio en Y (-1, 0, 1)
            game_map: Instancia del mapa para verificar colisiones

        Returns:
            bool: True si se movió, False si no
        """
        new_x = self._x + dx
        new_y = self._y + dy

        # Verificar que no sea un muro
        if not game_map.is_wall(new_x, new_y):
            self._x = new_x
            self._y = new_y
            return True
        return False

    def reset(self):
        """Reinicia al jugador a la posición inicial."""
        self._x = START_POSITION[0]
        self._y = START_POSITION[1]