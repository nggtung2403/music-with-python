from rich import print
from time import sleep
import sys
import pygame

pygame.mixer.init()
pygame.mixer.music.load("diudangyeu.mp3")
pygame.mixer.music.play()

lyrics = [
  ("Bây giờ ta sẽ đi chung đến cuối cuộc đời",0.081),
  ("Dù bận đến mấy cũng vui những phút thảnh thơi",0.081),
  ("Bao nhiêu mộng mơ ta nên gói gém cho nhau",0.076),
  ("Để khi về nhà, ta sẽ nếm yêu thương thật lâu",0.057),
  ("Nếu như sau này hai chúng ta có ra sao",0.066),
  ("Anh sẽ nói cho em nghe tại vì sao đôi ta bắt đầu",0.065),
]

delays = [0.0, 0.52, 0.27, 0.67, 0.49, 1]
for i,(line,delay_char) in enumerate(lyrics):
    for char in line:
        print(f"[bold green]{char}[/bold green]",end="")
        sys.stdout.flush()
        sleep(delay_char)
    print()
    sleep(delays[i])

while pygame.mixer.music.get_busy():
    sleep(0.1)
