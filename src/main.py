import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.Colors.BROWN_600
    
    
    page.update()
if __name__ == '__main__':
    ft.app(target=main)
