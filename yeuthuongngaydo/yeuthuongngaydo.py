from rich import print
from time import sleep
import sys
import pygame

pygame.mixer.init()
pygame.mixer.music.load("yeuthuongngaydo.mp3")
pygame.mixer.music.play()

lyrics = [
  ("Tình yêu đôi khi không như ta ước muốn",0.118),
  ("Có mấy ai khi yêu trao hết trọn con tim",0.095),
  ("Một người ra đi, một người hoen mi với bao lưu luyến",0.106),
  ("Giờ còn lại đây bao nhiêu câu hứa",0.08),
]

delays = [0.66, 0.16, 0.8, 1]

for i,(line,char_delay) in enumerate(lyrics):
    for char in line:
        print(f"[bold green]{char}[/bold green]",end="")
        sys.stdout.flush()
        sleep(char_delay)
    print()
    sleep(delays[i])

while pygame.mixer.get_busy():
    sleep(0.1)