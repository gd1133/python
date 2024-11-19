from fasthtml.common import div h1, p

def gerar_titolo(titulo, subtitulo):
    return div(
        h1(titulo)
        p(subtitulo)
    )