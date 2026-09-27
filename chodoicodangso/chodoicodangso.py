from rich import print
from time import sleep
import sys
import pygame

pygame.mixer.init()
pygame.mixer.music.load("chodoicodangso.mp3")
pygame.mixer.music.play()

sleep(12.5)
lyrics = [
  ("Đôi khi nhầm một chuyến xe lại đưa chúng ta về nơi muốn đến",0.111,"green"),
  ("Nhưng em lại chẳng muốn quay về về nơi chúng ta dừng lại",0.08,"red"),
  ("Anh gom từng vệt nắng cuối trời để thắp sáng hy vọng rằng em sẽ trở về",0.107,"blue"),
  ("Chờ đợi đâu đáng sợ chỉ là anh không biết chờ đến bao giờ",0.133,"yellow"),
]

delays = [0.79, 2.0, 0.61, 1]

for i,(line,delay_char,color) in enumerate(lyrics):
    for char in line:
        print(f"[bold {color}]{char}[/bold {color}]",end="")
        sys.stdout.flush()
        sleep(delay_char)
    print()
    sleep(delays[i])

while pygame.mixer.music.get_busy():
    sleep(0.1)