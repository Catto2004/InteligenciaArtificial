# Inteligencia Artificial: Tarea #1: Tres en Raya en Python by JDRB
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Button, Label

import tcss
import os

class TresEnRaya(App):
    # ################## Declaración De Variables ##################
    CSS = tcss.CSS
    Jugar = True
    Turno = "X"
    Tablero = [["", "", ""],
               ["", "", ""],
               ["", "", ""]]
    

    # ################## Configuración de la Interface ##################
    def on_mount(self) -> None:
        self.Turno = "X"        # Turno: X -> Jugador 1 / O -> Jugador 2.
        self.Tablero

    def compose(self) -> ComposeResult:
        yield Label("Tres en Raya",        classes="Titulo", expand=False)
        yield Label(f"Turno de {self.Turno}", classes="Estatus")

        # Tablero 3x3
        with Container(id="Tablero"):
            for i in range(9):  # 9 botones
                yield Button("", id=f"cell_{i}")  # botones vacíos

        # Controles:
        with Container(id="Controles"):
            yield Button("Reset", id="BotonReset")
            yield Button("Salir", id="BotonSalir")

    # ################## Implementación de la Logica ##################
    def on_button_pressed(self, event: Button.Pressed) -> None:
        boton = event.button
        # self.notify(f"Hiciste clic en {boton.id}")  # solo debug

        # No permite jugar si ya se terminó
        if not self.Jugar:
            self.notify("El juego ya terminó, presiona Reset.", severity="info")

        # Evitar sobreescribir un botón ya jugado
        if boton.label != "" and boton.label != "Reset" and boton.label != "Salir":
            self.notify("Esa casilla ya está ocupada!", severity="warning")

        # Colocar la marca según el turno
        if boton.label == "":
            boton.label = self.Turno

        # Cambiar turno
        if self.Turno == "O":
            self.Turno = "X"    
            self.query_one(".Estatus", Label).update("Turno de X")
        else:
            self.Turno = "O"
            self.query_one(".Estatus", Label).update("Turno de O")

        # Actualiza la matriz del tablero
        idx = int(boton.id.split("_")[1])  # seguro, ya que empieza con "cell_"
        fila, col = divmod(idx, 3)
        self.Tablero[fila][col] = self.Turno

        # Revisa las condiciones para ganar o empate
        Estado = self.RevisionTablero(self.Tablero)
        if Estado == 1:      # Gana X
            self.query_one(".Estatus", Label).update("¡Victoria de O!")
            self.juego_activo = False

        elif Estado  == 2:    # Gana O
            self.query_one(".Estatus", Label).update("¡Victoria de X!")
            self.juego_activo = False

        elif Estado == 3:    # Empate
            self.query_one(".Estatus", Label).update("¡Empate!")
            self.juego_activo = False

        # Reiniciar las casillas
        if boton.id == "BotonReset":
            for cell in self.query("#Tablero Button"):
                cell.label = ""
            for Casilla in self.Tablero:
                self.Tablero[Casilla] = ""
            self.Turno = "X"
            self.Jugar = True
            self.query_one(".Estatus", Label).update("Turno de X")
            return

        # Cierra el juego
        elif boton.id == "BotonSalir":
            self.exit()
            return

    def RevisionTablero(self, Tablero) -> int:
        # Revisar filas
        for fila in Tablero:
            if fila[0] == fila[1] == fila[2] != "":
                return 1 if fila[0] == "X" else 2

        # Revisar columnas
        for col in range(3):
            if Tablero[0][col] == Tablero[1][col] == Tablero[2][col] != "":
                return 1 if Tablero[0][col] == "X" else 2

        # Revisar diagonales
        if Tablero[0][0] == Tablero[1][1] == Tablero[2][2] != "":
            return 1 if Tablero[0][0] == "X" else 2
        if Tablero[0][2] == Tablero[1][1] == Tablero[2][0] != "":
            return 1 if Tablero[0][2] == "X" else 2

        # Revisar empate
        if all(cell != "" for fila in Tablero for cell in fila):
            return 3

        return 0  # Juego sigue

    def Min():
        pass

    def Max():
        pass

if __name__ == "__main__":
    TresEnRaya().run()
    #os.system("cls")
