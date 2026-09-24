from rich import print
from time import sleep
import sys
import pygame

pygame.mixer.init()
pygame.mixer.music.load("chochut.mp3")
pygame.mixer.music.play()

lyrics = [
  ("Chờ anh chút thôi, khi mùa đông vừa sang",0.094),
  ("Xếp lại hết ngổn ngang",0.098),
  ("Chờ chút thôi, rồi anh sẽ tìm tới",0.133),
  ("Chờ anh chút thôi, đã phiền em phải đợi",0.096),
  ("Có anh ở đây rồi",0.122),
  ("Vẫn gần em thôi, dù xa cách khung trời",0.083),
]
delays = [0.0, 0.6, 0.5, 0.56, 0.65, 1]

for i,(line,char_delays) in enumerate(lyrics):
    for char in line:
        print(f"[bold green]{char}[/bold green]",end="")
        sys.stdout.flush()
        sleep(char_delays)
    print()
    sleep(delays[i])

while pygame.mixer.music.get_busy():
    sleep(0.1)