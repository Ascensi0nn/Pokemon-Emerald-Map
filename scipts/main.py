import pygame
import classes

pygame.init()
WIDTH = 1200
HEIGHT = 700
FPS = 60
PX_PER_TILE = 318
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pokemon Emerald Map")

current_scene = 0       # 0=background, 1=route, 2=idk


def reset():
    pass

def draw_window(s):
    match s:
        case 0:
            background = classes.Tile("full_map.jpeg", 0, 0, WIDTH, HEIGHT)
            background.draw_image(background.get_path(), background.get_row, background.get_col, background.get_w, background.get_h)

    pygame.display.update()

def start_game():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    reset()
        draw_window(current_scene)


if __name__ == "__main__":
    start_game()