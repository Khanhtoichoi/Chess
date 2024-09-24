import pygame as p
import chess
chess_img = {}
width = height = 512
dim = 8
p_size = width // dim
FPS = 120
def load_images():
    chess_pieces = ['bR', 'bH', 'bB', 'bQ', 'bK', 'bP', 'wR', 'wH', 'wB', 'wQ', 'wK', 'wP']
    for piece in chess_pieces:
        chess_img[piece] = p.image.load("Images/" + piece + ".png")
        chess_img[piece] = p.transform.scale(chess_img[piece], (p_size, p_size))

def main():
    p.init()
    screen = p.display.set_mode((width, height))
    screen.fill(p.Color('white'))
    clock = p.time.Clock()
    game = chess.Game()
    load_images()
    while True:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                break
        draw_game(screen, game)
        clock.tick(FPS)
        p.display.flip()
def draw_game(screen, game):
    draw_board(screen)
    draw_pieces(screen, game.board)
def draw_board(screen):
    colors = [p.Color("#779455"), p.Color("#ebecd0")]
    for x in range(8):
        for y in range(8):
            color = colors[(x+y)%2]
            p.draw.rect(screen, color, p.Rect(x*p_size, y*p_size, p_size, p_size))
def draw_pieces(screen, board):
    for x in range(8):
        for y in range(8):
            piece = board[y][x]
            if piece != '':
                screen.blit(chess_img[piece], p.Rect(x*p_size, y*p_size, p_size, p_size))


if __name__ == '__main__':
    main()