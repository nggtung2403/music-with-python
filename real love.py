from rich import print
from time import sleep
import sys

lyrics = [
    ("Tay em với ra",0.15),
    ("Dù hai ta đứng xa",0.1),
    ("Anh đã đưa đôi tay mình",0.06),
    ("Cho em cầm",0.068),
    ("Dìu bước em qua chông gai",0.07),
    ("Oooh,em yêu sẽ thấy là",0.07),
    ("Tất cả vì yêu em đấy mà",0.08),
    ("Anh không biết nói ra sao",0.03),
    ("Để em có thể cảm nhận từng",0.052),
    ("Điều mà anh muốn nói",0.07),
    ("Là bình minh sương đêm",0.03),
    ("Tan nhanh trên lá",0.05),
    ("Anh mang ánh nắng về bên em",0.09),
    ("Là hoàng hôn in đôi môi em lên má",0.03),
    ("Yeah anh coi vết son như sắc màu",0.07),
    ("Làm cuộc sống thêm",0.05),
    ("Thật nhiều điều ấm êm",0.09),
    ("Với những khát khao buồn vui",0.05),
    ("Tựa trên bờ vai này",0.07),
    ("Bên anh thời gian ngừng trôi mãi...",0.03)

]
for line,char_delay in lyrics:
    for char in line:
        print(f"[bold green]{char}[/bold green]",end="")
        sys.stdout.flush()
        sleep(char_delay)
    print()
    sleep(0.05)
    