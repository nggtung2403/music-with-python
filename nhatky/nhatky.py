import sys
import pygame
from time import sleep

pygame.mixer.init()
pygame.init()

WIDTH,HEIGH = 1500,500
screen = pygame.display.set_mode((WIDTH,HEIGH))
pygame.display.set_caption("Nhật ký ")
clock = pygame.time.Clock()

font = pygame.font.SysFont("Segoe UI",40,bold=True)

pygame.mixer.music.load("nhatky.mp3")
pygame.mixer.music.play()

sleep(13.7)
lyrics = [
  ("Im far from home",0.141),
  ("Im far from home",0.099),
  ("Im far from home",0.143),
  ("And Im far from home",0.08),
  ("Đống suy tư vẫn đang dìm mình, không biết làm gì để tiền chất ví",0.045),
  ("Ngồi bên cửa sổ phòng trọ lệ hoen mi và viết nhật ký",0.051),
  ("Cuộc sống những lúc xa nhà, có lúc ngã thì phải đứng lên",0.041),
  ("Ông chú em ruột của bố muốn chiếm căn nhà mà bố đứng tên",0.047),
  ("Mẹ nằm đau ốm một mình với căn bệnh không thể gắng gượng",0.047),
  ("Sinh tử như một trò chơi mà một người phàm không thể thắng được",0.043),
  ("Con ước mình là vì sao ở trên trời cho con tỏa sáng",0.052),
  ("Con mong bố về với mẹ để cho hạnh phúc gia đình viên mãn",0.05),
  ("Ông nội luôn trông ở cửa đứng chống gậy và chờ bố về",0.058),
  ("Gia đình thiếu vắng đàn ông cũng chỉ là vì con ma số đề",0.048),
  ("Thời gian trôi qua thật nhanh năm nay mẹ cũng đã bạc tóc",0.046),
  ("Mẹ ngồi kia đầu giường nhìn vu vơ rồi lại bật khóc",0.052),
  ("Ông bà dần dần nằm xuống không còn ai trụ cột gia đình",0.051),
  ("Con vẫn luôn mong bố về chứ không muốn phải ôm hận cha mình",0.046),
  ("Con mong bố sống mạnh khỏe bên phương trời kia không còn lo âu",0.042),
  ("Còn con với mẹ bên này hằng ngày tự nhủ vẫn không sao đâu",0.047),
  ("Bố sắp về rồi con ơi con hãy đợi bố thêm một chút",0.049),
  ("10 năm thấm thoát trôi qua tựa lời mẹ nói chỉ trong một phút",0.044),
  ("Cây sung mà bố đã trồng ngày ấy giờ lớn đã mọc qua đầu",0.05),
  ("Xã hội muôn vàn đa cảnh tạo nên một bức tranh đa màu",0.051),
  ("Muôn vàn cảm xúc trôi qua để lại cho ta những vết chai sạn",0.043),
  ("Cuộc đời mình từ khi bố đi chia hai giai đoạn",0.058),
  ("Ông bà nhắm mắt xuôi tay khiến cho nhà mình vơi phần sung túc",0.044),
  ("Cô chú trong họ gần xa chỉ đến chơi nhà vì tờ di chúc",0.048),
  ("Muốn lấy mảnh đất cỏn con anh em họ hàng ra tòa đòi tố",0.051),
  ("Con chỉ biết nằm ở nhà ước đổi đất đai để có lại người bố",0.046),
  ("Ngày mà nhà mình bị cướp mất không mẹ ôm đồ đạc và ngồi chỉnh áo",0.045),
  ("Dù con biết mẹ khóc rất nhiều thêm bệnh thiếu ngủ nên mẹ không tỉnh táo",0.037),
  ("Ngày đó chỉ vì kiệt sức mà mẹ đã về với cõi vĩnh hằng",0.058),
  ("Con ngồi bên kia vỉa hè nhìn mẹ đắp chiếu và ngồi tĩnh lặng",0.043),
  ("Dòng người lướt qua xô bồ ai ai đi qua thả vài tờ tiền",0.053),
  ("Đưa mẹ về nơi cuối cùng an nghỉ thanh thản quay về với tổ tiên",0.043),
  ("Vào lễ cúng tuần con thấy bố về cầm theo trên tay hai túi trái cây",0.049),
  ("Trong màn đêm lờ mờ sương phủ bố với tay để kéo lấy cái dây",0.046),
  ("Tấm màn che lộ ra hình di ảnh người con gái mà bố đã từng thương",0.045),
  ("Nuối tiếc quá muộn bên trong căn phòng chỉ còn nước mắt với trầm hương..",0.043),
]

delays = [1.25, 1.01, 1.61, 0.1, 0.58, 0.51, 0.95, 0.56, 0.34, 0.62, 0.49, 0.16, 0.56, 0.56, 0.57, 0.49, 0.54, 0.52, 0.54, 0.82, 0.51, 0.53, 0.58, 0.71, 0.64, 0.49, 0.6, 0.59, 0.52, 0.27, 0.64, 0.11, 0.57, 0.52, 0.43, 0.12, 0.31, 0.22, 0.31, 1]


current_line = 0
current_char = 0
last_update = pygame.time.get_ticks()
state = "typing"
wait_start_time = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    screen.fill((0,0,0))

    if current_line < len(lyrics):
        line,char_delay = lyrics[current_line]

        if state == "typing":
            if now - last_update >= char_delay * 1000:
                current_char += 1
                last_update = now
                if current_char >= len(line):
                    state = "waiting"
                    wait_start_time = now

        elif state == "waiting":
            if now - wait_start_time >= delays[current_line] * 1000:
                current_line += 1
                current_char = 0
                state = "typing"

        visible_text = line[:current_char]
        text_surface = font.render(visible_text,True,(255,255,255))
        x = (WIDTH - text_surface.get_width()) // 2
        y = HEIGH // 2 - 20
        screen.blit(text_surface,(x,y))

    else:
        end_text = font.render("Nhat Ky - DLOW",True,(255,255,255))
        screen.blit(end_text,(WIDTH // 2 - end_text.get_width(),HEIGH//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()