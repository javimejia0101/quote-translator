import flet as ft
 
def main(page: ft.Page):
 
    def cambiar(e):
        if idioma.value == "English":
            quote.value = "Football is not just a game; it’s passion, discipline, and the art of never giving up even when the score is against you."
 
        if idioma.value == "Spanish":
            quote.value = "El fútbol no es solo un juego, es pasión, disciplina y el arte de nunca rendirse aunque el marcador vaya en contra."
 
        if idioma.value == "Brasil":
            quote.value = "O futebol não é apenas um jogo; é paixão, disciplina e a arte de nunca desistir, mesmo quando o placar está contra você."
 
        page.update()
 
    quote = ft.Text("El fútbol no es solo un juego, es pasión, disciplina y el arte de nunca rendirse aunque el marcador vaya en contra.")
 
    idioma = ft.RadioGroup(
        content=ft.Column([
            ft.Radio(value="English", label="English"),
            ft.Radio(value="Spanish", label="Spanish"),
            ft.Radio(value="Brasil", label="Brasil")
        ]),
        on_change=cambiar
    )
 
    page.add(
        quote,
        idioma
    )
 
ft.run(main=main)