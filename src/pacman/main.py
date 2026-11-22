import pygame
from pathlib import Path
from pacman.board import Board

LEVELS_DIR = Path(__file__).parent / "levels"

SPEED = 4
FPS = 60
TILE = 30



def load_layout(name):
    return (LEVELS_DIR / name).read_text().splitlines()


def draw_board(board, screen):
    for r_i, row in enumerate(board.grid):
        for c_i, tile in enumerate(row):
            x = c_i * TILE
            y = r_i * TILE
            if tile == "#":
                pygame.draw.rect(screen, (0, 255, 0), (x, y, TILE, TILE))
            elif tile == ".":
                pygame.draw.circle(screen, (255, 0, 0), (x + TILE // 2, y + TILE // 2), 3)

def game_win(score , dots):
    if score == dots:
        return True
    return False

def collect_points(board, score, r_i, c_i):
   
    if board.grid[r_i][c_i] == ".":
        board.grid[r_i][c_i] = " "
        score += 1
    return score



def main():
    layout = load_layout("level1.txt")
    board = Board(layout)

    WIDTH = len(board.grid[0]) * TILE
    HEIGHT = len(board.grid) * TILE
    SCORE = -1
    MAX_SCORE = board.dots_count() - 1

    pygame.init()
    score_d = pygame.font.SysFont(None, 36)
    win_d = pygame.font.SysFont(None, 72)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman")
    clock = pygame.time.Clock()

    x, y = WIDTH // 2, HEIGHT // 2
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            next_x = x - SPEED
            if not board.is_wall(y//TILE,next_x//TILE):
                x = next_x
        if keys[pygame.K_RIGHT]:
            next_x = x + SPEED
            if not board.is_wall(y//TILE,next_x//TILE):
                x = next_x
        if keys[pygame.K_UP]:
            next_y = y - SPEED
            if not board.is_wall(next_y//TILE,x//TILE):
                y = next_y
        if keys[pygame.K_DOWN]:
            next_y = y + SPEED
            if not board.is_wall(next_y//TILE,x//TILE):
                y = next_y

        SCORE = collect_points(board,SCORE,y//TILE,x//TILE)

        screen.fill((0, 0, 0))
        draw_board(board, screen)
        pygame.draw.circle(screen, (255, 255, 0), (x, y), 10)
        score_surface = score_d.render(f"Score: {SCORE}", True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))
        if game_win(SCORE,MAX_SCORE):
            message = win_d.render("YOU WIN", True, (212, 175, 55))
            screen.blit(message, message.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()
        

        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()