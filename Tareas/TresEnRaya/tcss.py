CSS = """
Screen {
    align: center middle;
}

.titulo {
    color: yellow;
    text-style: bold;
    margin-bottom: 2;
    width: 100%;
    align: center middle;
}

#Tablero {
    layout: grid;
    grid-size: 3 3;      /* 3 columnas x 3 filas */
    grid-gutter: 1 1;    /* separación entre botones */
    content-align: center middle;
}

#Controles{
    layout: horizontal;
    margin-top: 2;
    align-horizontal: center;
}

Button {
    width: 8;
    height: 3;
    text-style: bold;
}
"""
