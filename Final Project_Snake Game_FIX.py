#import library
import pygame
import time
import random
 
pygame.init() #inisialisasi semua module berfungsi (tuple, modul, dan fungsi kodingan) berjalan dg baik atau tidak 

crash_sound = pygame.mixer.Sound("crash.mp3")
pygame.mixer.music.load("jazz.mp3")
snake_eat = pygame.mixer.Sound("eating.wav")


#kode warna pygame yang dipake
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#ukuran jendela game
dis_width = 1000
dis_height = 600

#caption pada toolbar jendela game
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')


clock = pygame.time.Clock() #mengupdate tampilan jendela game 

#ukuran ular dan kecepatan ular
snake_block = 10
snake_speed = 15
 
#font dari tulisan jendela game
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
yummy_font = pygame.font.SysFont("comicsansms", 15)
 
#definisi fungsi score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow) # fungsi tulisan skore tampil di layar
    dis.blit(value, [0, 0])  #untuk munculkan font di jendela game ketika ular memakan makanannya

def yummy(foodx, foody):
    value = yummy_font.render("Yummy", True, yellow)
    dis.blit(value, [foodx, foody])

#definisi warna dan bentuk ularnya

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) #menjelaskan kondisi ular posisi 0, jika memakan makanan selalu bertambah panjang 1 blok
 
#definisi tampilan tulisan ketika ular menabrak pinggir jendela game/memakan badannya sendiri 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
#definisi ketika game berjalan 
def gameLoop():
    pygame.mixer.music.load("jazz.mp3")
    pygame.mixer.music.play(-1)
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(30, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(30, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Keyboard \'C' for Play Again or \'Q' for Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.mixer.music.stop() 
            pygame.display.update()
            
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: #perulangan untuk tombol ketika ditekan ular berpindah tempat 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        #fungsi untuk menjalankan ular menggunakan tombol atas, bawah, kanan, kiri
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            
#fungsi perulangan ketika posisi ular melebihi batas ukuran jendela game
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  
            game_close = True
            pygame.mixer.Sound.play(crash_sound)
            
        #posisi ular berpindah
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) #tampilan layar game
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #fungsi untuk posisi makanan ular dan ketika ular makan makanannya, panjang ular bertambah
        
        #membentuk badan ular dengan menggunakan list, ketika ular makan makanan, badan ular bertambah di bagian belakang list
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
            
        #ketika ular makan badannya sendiri, value/list pada badan ular berkurang satu    
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        #memanggil fungsi untuk nambah panjang ular
        our_snake(snake_block, snake_List) 
        #memanggil fungsi kondisi score berkurang ketika ular nabrak badannya sendiri
        Your_score(Length_of_snake - 1)
 
        pygame.display.update() #tampilan display pygame berubah ketika ular makan makanan, buah berhasil di makan, dan nabrak badannya sendiri
        #fungsi makanan
        if x1 == foodx and y1 == foody:
            yummy(foodx, foody)
            pygame.display.update()
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_eat.play()
            

        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
