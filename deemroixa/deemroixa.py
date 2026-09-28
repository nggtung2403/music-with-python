from rich import print
from time import sleep
import sys
import pygame

pygame.mixer.init()
pygame.mixer.music.load("deemroixa.mp3")
pygame.mixer.music.play()

colors = ["green", "red", "yellow", "blue", "magenta", "cyan"]

lyrics = [
  ("Thì anh hãy cứ đi tìm một hạnh phúc mới",0.152),
  ("Tìm một người thay thế em trong những đêm",0.089),
  ("Để em một mình nhé anh anh cứ đi đi",0.137),
  ("Đập nát hết ngày tháng qua anh cứ đi đi",0.13),
]

delays = [1.75, 1.63, 1.98, 1]

for i,(line,delay_char) in enumerate(lyrics):
    for j,char in enumerate(line):
        color = colors[j % len(colors)]
        print(f"[bold {color}]{char}[/bold {color}]",end="")
        sys.stdout.flush()
        sleep(delay_char)
    print()
    sleep(delays[i])

while pygame.mixer.music.get_busy:
    sleep(0.1)
