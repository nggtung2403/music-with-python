from rich import print
from time import sleep
import sys
import pygame

pygame.mixer.init()
pygame.mixer.music.load("giumaiyeuthuongganke.mp3")
pygame.mixer.music.play()

lyrics = [
  ("Anh sẽ tới đây cùng cơn mưa",0.063),
  ("Em vẫn đứng trông ai đón đưa",0.05),
  ("Dẫu đã biết chỉ là lời hứa",0.05),
  ("Nhưng em vẫn luôn luôn đứng chờ",0.055),
  ("Vì ánh mắt ngọt ngào",0.079),
  ("Ấm áp dạt dào anh trao",0.093),
  ("Sẽ vẫn mãi luôn là như thế",0.048),
  ("Dẫu có những âu lo mãi mê",0.05),
  ("Thì anh vẫn không quên lối về",0.079),
  ("Là nơi có em bên mình",0.071),
  ("Giữ mãi yêu thương gần kề",0.114),
]

delays = [0.21, 0.53, 0.41, 0.35, 0.59, 2.5, 0.41, 1.13, 1.09, 0.72, 1]

for i,(line,char_delays) in enumerate(lyrics):
    for char in line:
        print(f"[bold bright_cyan]{char}[/bold bright_cyan]",end="")
        sys.stdout.flush()
        sleep(char_delays)
    print()
    sleep(delays[i])

while pygame.mixer.get_busy():
    sleep(0.1)