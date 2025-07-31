import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BROWN_600
    
    cena = ft.Image(col=12, src='images/scene.png')
    
    vitima = ft.Image(
        data = 0,
        src = 'images/hangman_0.png',
        repeat = ft.ImageRepeat.NO_REPEAT,
        height = 300
        
        )
    
    jogo = ft.Container(
        col = {'xs': 12, 'lg': 6},
        padding = ft.padding.all(50),
        content = ft.Column(
            controls=[
                vitima,
                # palavra
            ]
        )
        
    )
    
    teclado = ft.Container(
        col = {'xs': 12, 'lg': 6},       
        image=ft.DecorationImage(src='images/keyboard.png', repeat=ft.ImageRepeat.NO_REPEAT, fit=ft.ImageFit.FILL),
        padding= ft.padding.only(top=150, left=80, right=80, bottom=50),
        content = ft.Row(
            controls=[
                ft.Container(
                    height=50,
                    width=50,
                    border_radius=ft.border_radius.all(5)
                )
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
