#!/usr/bin/env python3
"""Punto de entrada principal del juego."""

import sys
from .game import Game


def main():
    """Función principal que ejecuta el juego."""
    try:
        game = Game()
        game.run()
    except Exception as e:
        print(f"Error al ejecutar el juego: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())