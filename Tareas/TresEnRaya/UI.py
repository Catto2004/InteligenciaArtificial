# 
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Label

import tcss
import os

class TresEnRaya(App):
    CSS = tcss.CSS
    Turno = "X"

    def on_mount(self) -> None:
        self.Turno = "X"        # Turno: X -> Jugador 1 / O -> Jugador 2.

    def compose(self) -> ComposeResult:
        yield Label(f"Tres en Raya",        classes="titulo", expand=True)

        # Tablero 3x3
        with Container(id="Tablero"):
            for i in range(9):  # 9 botones
                yield Button("", id=f"cell_{i}")  # botones vacíos

        # Controles:
        with Container(id="Controles"):
            yield Button("Reset", id="BotonReset")
            yield Button("Salir", id="BotonSalir")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        boton = event.button
        # self.notify(f"Hiciste clic en {boton.id}")  # solo debug

        # Evitar sobreescribir un botón ya jugado
        if boton.label != "" and boton.label != "Reset" and boton.label != "Salir":
            self.notify("Esa casilla ya está ocupada!", severity="warning")

        # Colocar la marca según el turno
        if boton.label == "":
            boton.label = self.Turno

        # Cambiar turno
        self.Turno = "O" if self.Turno == "X" else "X"

        # Reiniciar las casillas
        if boton.id == "BotonReset":
            for cell in self.query("#Tablero Button"):
                cell.label = ""
                
        elif boton.id == "BotonSalir":
            self.exit()


if __name__ == "__main__":
    TresEnRaya().run()
    #os.system("cls")
