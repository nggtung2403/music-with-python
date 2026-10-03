import pygame
import sys

# ==== KHỞI TẠO ====
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lyrics Player")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Segoe UI", 32, bold=True)

# ==== PHÁT NHẠC ====
pygame.mixer.music.load("chochut.mp3")
pygame.mixer.music.play()

# ==== DỮ LIỆU LYRICS ====
lyrics = [
    ("Chờ anh chút thôi, khi mùa đông vừa sang", 0.094),
    ("Xếp lại hết ngổn ngang", 0.098),
    ("Chờ chút thôi, rồi anh sẽ tìm tới", 0.133),
    ("Chờ anh chút thôi, đã phiền em phải đợi", 0.096),
    ("Có anh ở đây rồi", 0.122),
    ("Vẫn gần em thôi, dù xa cách khung trời", 0.083),
]
delays = [0.6, 0.5, 0.56, 0.65, 1, 1]

# ==== BIẾN TRẠNG THÁI ====
current_line_index = 0
current_char_index = 0
last_update_time = pygame.time.get_ticks()
state = "typing"
wait_start_time = 0

# ==== VÒNG LẶP CHÍNH ====
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    screen.fill((0, 0, 0))

    if current_line_index < len(lyrics):
        line, char_delay = lyrics[current_line_index]

        if state == "typing":
            if now - last_update_time >= char_delay * 1000:
                current_char_index += 1
                last_update_time = now
                if current_char_index >= len(line):
                    state = "waiting"
                    wait_start_time = now

        elif state == "waiting":
            if now - wait_start_time >= delays[current_line_index] * 1000:
                current_line_index += 1
                current_char_index = 0
                state = "typing"

        visible_text = line[:current_char_index]
        text_surface = font.render(visible_text, True, (255, 255, 255))
        x = (WIDTH - text_surface.get_width()) // 2
        y = HEIGHT // 2 - 20
        screen.blit(text_surface, (x, y))
    else:
        end_text = font.render("Hết bài hát", True, (255, 255, 255))
        screen.blit(end_text, (WIDTH//2 - end_text.get_width()//2, HEIGHT//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()