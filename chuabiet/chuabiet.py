from time import sleep
import pygame
import sys

pygame.mixer.init()
pygame.init()

WIDTH,HEIGH = 900,300
screen = pygame.display.set_mode((WIDTH,HEIGH))
pygame.display.set_caption("Chua dat ten")
clock = pygame.time.Clock
font = pygame.font.SysFont("Seoge UI",32,bold=True)

pygame.mixer.music.load("ten bai hat")
pygame.mixer.music.play()

lyrics = [
    ("Chờ anh chút thôi, khi mùa đông vừa sang", 0.094),
    ("Xếp lại hết ngổn ngang", 0.098),
    ("Chờ chút thôi, rồi anh sẽ tìm tới", 0.133),
    ("Chờ anh chút thôi, đã phiền em phải đợi", 0.096),
    ("Có anh ở đây rồi", 0.122),
    ("Vẫn gần em thôi, dù xa cách khung trời", 0.083),
]
delays = [0.6, 0.5, 0.56, 0.65, 1, 1]

current_line = 0
current_char = 0
last_update_time = pygame.time.get_ticks()
state = "typing"
wait_start = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    screen.fill(0,0,0)

    if current_line <= len(lyrics):
        line,char_delays = lyrics[current_line]

        if state == "typing":
            if now - last_update_time >= char_delays * 1000:
                current_char += 1
                last_update_time = now
                if current_char >= len(line):
                    state = "waiting"
                    wait_start = now

        elif state == "waiting":
            if now - wait_start >= delays[current_line] * 1000:
                current_line += 1
                current_char = 0
                state = "typing"

        visible_text = line[:current_char]
        text_surface = font.render(visible_text,True,(30,60,30))
        x = (WIDTH - text_surface.get_width()) // 2
        y = HEIGH // 2 -20
        screen.blit(text_surface,(x,y))

    else:
        end_text = font.render("Het nhac",True,(30,60,30))
        screen.blit(end_text,((WIDTH - end_text.get_width()) // 2,HEIGH // 2))

    pygame.display.flip()
    clock.tick(50)

pygame.quit()
sys.exit()



