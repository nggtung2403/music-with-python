import sys
import pygame
from time import sleep

pygame.mixer.init()
pygame.init()

WIDTH,HEIGHT = 900,300
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Có Khi")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Segoe UI",32,bold=True)

pygame.mixer.music.load("cokhi.mp3")
pygame.mixer.music.play()

lyrics = [
  ("Phải yêu em nhiều bao nhiêu",0.15),
  ("Mong chờ bao nhiêu",0.066),
  ("Thì em mới hiểu thấu",0.117),
  ("Cớ sao em lại vô tâm",0.093),
  ("Hững hờ bỏ mặc riêng anh",0.116),
  ("Nếu như em là cơn mơ",0.128),
  ("Mỗi ngày anh mơ",0.088),
  ("Anh chẳng muốn thức giấc",0.078),
  ("Vì anh biết anh không thể",0.052),
  ("Quên đi một người",0.109),
  ("Anh đã yêu",0.15),
]

delays = [0.16, 0.42, 0.39, 0.32, 1.3, 0.55, 0.63, 0.27, 0.1, 0.23, 1]

current_line = 0
current_char = 0
last_time_update = pygame.time.get_ticks()
state = "typing"
wait_start_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    screen.fill((30,30,60))

    if current_line < len(lyrics):
        line,char_delay = lyrics[current_line]
        if state == "typing":
            if now - last_time_update >= char_delay * 1000:
                current_char += 1
                last_time_update = now
                if current_char >= len(line):
                    state = "waiting"
                    wait_start_time = now

        elif state == "waiting":
            if now - last_time_update >= delays[current_line] *1000:
                current_line += 1
                current_char = 0
                state = "typing"

        visible_text = line[:current_char]
        text_surface = font.render(visible_text,True,(0,255,0))
        x = (WIDTH - text_surface.get_width()) // 2
        y = HEIGHT // 2 - 20
        screen.blit(text_surface,(x,y))
    else:
        end_text = font.render("CÓ KHI - HOÀI LÂM")
        screen.blit(end_text,(WIDTH // 2 - end_text.get_width(),HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()


