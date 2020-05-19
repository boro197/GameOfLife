from view import Window
from view import PG_COLORS

def main():
    main_window = Window(width=1024, height=768, title="Game of life", color = PG_COLORS.get('deepskyblue4'))
    main_window.show()


if __name__ == '__main__':
    main()
