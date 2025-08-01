import flet as ft
import string


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BROWN_600
    
    cena = ft.Image(col=12, src='images/scene.png')
    
    vitima = ft.Image(
        data = 0,
        src = 'images/hangman_0.png',
        repeat = ft.ImageRepeat.NO_REPEAT,
        height = 300
        
        )
    
    escolha = 'flet'
    palavra = ft.Row(
        controls=[
            ft.Container(
                bgcolor=ft.Colors.AMBER,
                width=50,
                height=50,
                content=ft.Text(
                    value=letra,
                    color=ft.Colors.WHITE,
                    size=30,
                    text_align=ft.TextAlign.CENTER,
                    weight=ft.FontWeight.BOLD
                )
            ) for letra in escolha
        ]
    )
    

    
    jogo = ft.Container(
        col = {'xs': 12, 'lg': 6},
        padding = ft.padding.all(50),
        content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                vitima,
                palavra
            ]
        )
        
    )
    
    teclado = ft.Container(
        col = {'xs': 12, 'lg': 6},       
        image=ft.DecorationImage(src='images/keyboard.png', repeat=ft.ImageRepeat.NO_REPEAT, fit=ft.ImageFit.FILL),
        padding= ft.padding.only(top=150, left=80, right=80, bottom=50),
        content = ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5),
                    content=ft.Text(
                        value=letter,
                        color=ft.Colors.WHITE,
                        size=30,
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD
                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.Colors.AMBER, ft.Colors.DEEP_ORANGE]
                    )         
                ) for letter in string.ascii_uppercase
            ]
        )        
    )
    
    layout = ft.ResponsiveRow(
        columns=12,
        controls=[
            cena,
            jogo,
            teclado,
            cena           
        ],        
    )
    
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
