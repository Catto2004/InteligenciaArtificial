CSS = """
Screen {
    align: center middle;
}

.Titulo {
    color: yellow;
    text-style: bold;
    margin-bottom: 1;
    width: 100%;
    align-horizontal: center;
}

.Estatus {
    color: white;
    text-style: none;
    margin-bottom: 1;
    width: 100%;
    align-horizontal: center;
}

#Tablero {
    layout: grid;
    grid-size: 3 3;      /* 3 columnas x 3 filas */
    grid-gutter: 0 1;    /* separación entre botones */
    content-align: center middle;
}

#Tablero Button {
    width: 6;
    height: 3;
    color: white;
    border: solid gray;
}

#Controles{
    layout: horizontal;
    margin-top: 1;
    align-horizontal: center;
}

Button {
    width: 6;
    height: 3;
    text-style: bold;
}

"""
