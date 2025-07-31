import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BROWN_600
    
    cena = ft.Image(col=12, src='images/scene.png')
    
    
    layout = ft.ResponsiveRow(
        controls=[
            cena,
            # jogo,
            # teclado,
            cena           
        ],        
    )
    
    page.add(layout)

if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
