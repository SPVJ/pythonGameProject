import pygame
import time
import random
from abc import *



class theintro():
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.fps = pygame.time.Clock()
        self.intro = pygame.display.set_mode((self.width, self.height))
        self.intro.fill([0, 0, 0])
        self.ifont = pygame.font.SysFont(None, 60)
        self.font = pygame.font.SysFont(None, 50)
        self.stat = True
        self.howtoplaycheck = False
        self.introbg = pygame.image.load("introbg.png")
        self.intro.blit(self.introbg, [0, 0])
        self.screen_text = self.ifont.render('WELCOME TO SPACE SURVIVOR', True, [200, 200, 200])
        self.screen_text_box = self.screen_text.get_rect()
        self.screen_text_box.center = (self.width/2),(self.height/2-50)
        self.screen_text1 = self.font.render('Press A to play', True, [200, 200, 200])
        self.screen_text1_box = self.screen_text.get_rect()
        self.screen_text1_box.center = (self.width / 2), (self.height / 2+50)
        self.screen_text2 = self.font.render('Press H to view how to play', True, [200, 200, 200])
        self.screen_text2_box = self.screen_text.get_rect()
        self.screen_text2_box.center = (self.width / 2), (self.height / 2+100)
        self.screen_text3 = self.font.render('Press Q to Quit', True, [200, 200, 200])
        self.screen_text3_box = self.screen_text.get_rect()
        self.screen_text3_box.center = (self.width / 2), (self.height / 2 + 150)
        self.intro.blit(self.screen_text, self.screen_text_box)
        self.intro.blit(self.screen_text1,self.screen_text1_box)
        self.intro.blit(self.screen_text2, self.screen_text2_box)
        self.intro.blit(self.screen_text3, self.screen_text3_box)

        pygame.display.set_caption('Main Menu')
        while self.stat:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.stat=False
                    if event.key == pygame.K_h:
                        self.stat = False
                        self.howtoplaycheck = True
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
            pygame.display.update()

class howtoplay():
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.fps = pygame.time.Clock()
        self.intro = pygame.display.set_mode((self.width, self.height))
        self.intro.fill([0, 0, 0])
        self.ifont = pygame.font.SysFont(None, 60)
        self.font = pygame.font.SysFont(None, 50)
        self.stat = True
        self.introbg = pygame.image.load("introbg.png")
        self.intro.blit(self.introbg, [0, 0])
        self.howto_text = self.ifont.render('HOW TO PLAY', True, [200, 200, 200])
        self.howto_text_box = self.howto_text.get_rect()
        self.howto_text_box.center = (150), (50)

        self.howto_text1 = self.font.render('Use "WASD" to navigate the ship', True, [200, 200, 200])
        self.howto_text1_box = self.howto_text1.get_rect()
        self.howto_text1_box.center = (280), (120)

        self.howto_text2 = self.font.render('This is you , you have 3 lives', True, [200, 200, 200])
        self.howto_text2_box = self.howto_text2.get_rect()
        self.howto_text2_box.center = (350), (190)

        self.howto_text4 = self.font.render('Your goal is to dodge enemy', True, [200, 200, 200])
        self.howto_text4_box = self.howto_text4.get_rect()
        self.howto_text4_box.center = (350), (250)

        self.howto_text5 = self.font.render('and use auto-gun to shoot them', True, [200, 200, 200])
        self.howto_text5_box = self.howto_text5.get_rect()
        self.howto_text5_box.center = (360), (310)

        self.howto_text6 = self.font.render('if they hit you, you lose 1 health', True, [200, 200, 200])
        self.howto_text6_box = self.howto_text6.get_rect()
        self.howto_text6_box.center = (360), (360)

        self.howto_textx = self.font.render('if you hit the edge, you also die', True, [200, 200, 200])
        self.howto_textx_box = self.howto_textx.get_rect()
        self.howto_textx_box.center = (360), (410)

        self.howto_text3 = self.font.render('Press Space Bar to continue or A to play', True, [200, 200, 200])
        self.howto_text3_box = self.howto_text3.get_rect()
        self.howto_text3_box.center = (self.width / 2), (self.height / 2+250)
        self.purple = pygame.image.load("face1.png")
        self.green = pygame.image.load("advancedE.png")
        self.black = pygame.image.load("missile1.png")
        self.player = pygame.image.load("player1.png")
        self.intro.blit(self.player, (10,130))
        self.intro.blit(self.howto_text, self.howto_text_box)
        self.intro.blit(self.howto_text1, self.howto_text1_box)
        self.intro.blit(self.howto_text2, self.howto_text2_box)
        self.intro.blit(self.howto_text3, self.howto_text3_box)
        self.intro.blit(self.howto_text4, self.howto_text4_box)
        self.intro.blit(self.howto_text5, self.howto_text5_box)
        self.intro.blit(self.howto_text6, self.howto_text6_box)
        self.intro.blit(self.howto_textx, self.howto_textx_box)

        while self.stat:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.intro.blit(self.introbg, [0, 0])
                        self.howto_text7 = self.font.render('This is the enemy', True, [200, 200, 200])
                        self.howto_text7_box = self.howto_text1.get_rect()
                        self.howto_text7_box.center = (280), (120)

                        self.howto_text8 = self.font.render('The purple one need 2 shots to kill', True, [200, 200, 200])
                        self.howto_text8_box = self.howto_text1.get_rect()
                        self.howto_text8_box.center = (400), (190)

                        self.howto_text9 = self.font.render('The green one need 3 shots to kill', True, [200, 200, 200])
                        self.howto_text9_box = self.howto_text1.get_rect()
                        self.howto_text9_box.center = (410), (300)

                        self.howto_text10= self.font.render('The black one cannot be killed', True, [200, 200, 200])
                        self.howto_text10_box = self.howto_text1.get_rect()
                        self.howto_text10_box.center = (410), (420)

                        self.howto_text11 = self.font.render('Press A to play', True, [200, 200, 200])
                        self.howto_text11_box = self.howto_text1.get_rect()
                        self.howto_text11_box.center = (550), (520)

                        self.intro.blit(self.black, (60, 390))
                        self.intro.blit(self.purple,(10,160))
                        self.intro.blit(self.green, (10, 260))
                        self.intro.blit(self.howto_text, self.howto_text_box)
                        self.intro.blit(self.howto_text7, self.howto_text7_box)
                        self.intro.blit(self.howto_text8, self.howto_text8_box)
                        self.intro.blit(self.howto_text9, self.howto_text9_box)
                        self.intro.blit(self.howto_text10, self.howto_text10_box)
                        self.intro.blit(self.howto_text11, self.howto_text11_box)

                    if event.key == pygame.K_a:
                        self.stat = False





            pygame.display.update()




class ending():
    def __init__(self):
        pygame.init()
        self.stat=True
        self.width = 800
        self.height = 600
        self.end = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load("endscreen.png")
        self.end.blit(self.background,[0,0])
        self.font = pygame.font.SysFont(None, 90)
        self.sfont = pygame.font.SysFont(None, 45)
        self.screen_text = self.font.render('GAME OVER', True, [0, 0, 0])
        self.screen_box = self.screen_text.get_rect()
        self.screen_box.center=(self.width/2),(self.height/2)

        self.screen_text2 = self.sfont.render('Press SPACEBAR to get back to main menu', True, [0, 0, 0])
        self.screen2_box = self.screen_text2.get_rect()
        self.screen2_box.center = (self.width / 2), (self.height / 2+100)

        self.screen_text3 = self.sfont.render('Press Q to Quit', True, [0, 0, 0])
        self.screen3_box = self.screen_text3.get_rect()
        self.screen3_box.center = (self.width / 2), (self.height / 2 + 200)


        self.end.blit(self.screen_text, self.screen_box)
        self.end.blit(self.screen_text2, self.screen2_box)
        self.end.blit(self.screen_text3, self.screen3_box)
        pygame.display.set_caption('Game Over')

        pygame.display.update()
        while self.stat:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.stat =False
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()



class themaingame():
    def __init__(self):
        pygame.init()
        self.display_width =800
        self.display_height=600
        self.main1 = pygame.display.set_mode((self.display_width, self.display_height))
        self.font = pygame.font.SysFont(None,50)
        pygame.display.set_caption('Space Survivor')
        self.FPS =60
        self.black = [0, 0, 0]
        self.blue=[0,0,255]
        self.white=[255,255,255]
        self.cyan=[0,255,255]
        self.enemy = Ebasic()
        self.enemy2 = Eadvanced()
        self.enemy3 = Emissile()
        self.score = 0
        self.live = 3

        self.fps = pygame.time.Clock()
        self.gamestat = True
        self.xchange = 0
        self.ychange = 0
        self.exhange2=0
        self.eychange2=0
        self.eychange3 =0
        self.exchange = 0
        self.eychange = 3


        self.xpos = self.display_width / 2
        self.ypos = self.display_height / 2
        self.bullet = bullet1(400, 300, 30)

    def message(self,msg,color):
        self.screen_text=self.font.render(msg,True,color)
        self.main1.blit(self.screen_text,[self.display_width/2-50,self.display_height/2])

    def background(self):
        self.bg=pygame.image.load("bg2.jpg")
        self.main1.blit(self.bg,[0,0])

    def enemyFace(self):
        self.Face1=pygame.image.load("face1.png")
        self.main1.blit(self.Face1,[self.enemy.spawnx-50,self.enemy.spawny-50])
        self.Face2 =pygame.image.load("advancedE.png")
        self.main1.blit(self.Face2,[self.enemy2.spawnx-70,self.enemy2.spawny-50])
        self.Face3 = pygame.image.load("missile1.png")
        self.main1.blit(self.Face3, [self.enemy3.spawnx, self.enemy3.spawny])

    def endscreen(self):
        self.end = pygame.image.load("endscreen.png")
        self.main1.blit(self.end,[0,0])
    def playerface(self):
        self.ship=pygame.image.load("player1.png")
        self.main1.blit(self.ship,[self.xpos,self.ypos])

    def bulletface(self):
        self.ammu=pygame.image.load("bullet.png")
        self.main1.blit(self.ammu,[self.bullet.xpos-10,self.bullet.ypos-10])

    def boom(self):
        self.bomb=pygame.image.load("boom1.png")
        self.main1.blit(self.bomb,[self.bullet.xpos,self.bullet.ypos])

    def scoreshow(self):
        self.scoretext = self.font.render("Score : "+str(self.score), True, [255,255,255])
        self.main1.blit(self.scoretext, [10, 10])

    def liveshow(self):
        self.hptext = self.font.render("Live(s) : " + str(self.live), True, [255, 255, 255])
        self.main1.blit(self.hptext, [610, 10])


    def gameloop(self):

        while self.gamestat:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestat = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.xchange = -8
                        self.ychange = 0
                    if event.key == pygame.K_d:
                        self.xchange = 8
                        self.ychange = 0
                    if event.key == pygame.K_w:
                        self.ychange = -6
                        self.xchange = 0
                    if event.key == pygame.K_s:
                        self.ychange = 6
                        self.xchange = 0


            if self.xpos+50 <=0 or self.xpos >= self.display_width or self.ypos <=10 or self.ypos >= self.display_height-70:
                        self.gamestat = False

            if self.bullet.ypos <= 0 or self.bullet.ypos >= self.display_height:
                self.bullet.ypos = self.ypos
                self.bullet.xpos = self.xpos

            if self.enemy.spawnx > self.xpos:
                if self.score >= 5:
                    self.exchange = -8
                    self.eychange = 8
                elif self.score >= 10:
                    self.exchange = -14
                    self.eychange = 16
                elif self.score >= 20:
                    self.exchange = -20
                    self.eychange = 22

                else:
                    self.exchange = -3
                    self.eychange = 4
            else:
                if self.score >= 5:
                    self.exchange = 8
                    self.eychange = 8
                elif self.score >= 10:
                    self.exchange = 14
                    self.eychange = 16
                elif self.score >= 20:
                    self.exchange = 20
                    self.eychange = 22
                else:
                    self.exchange = 3
                    self.eychange = 4

            if self.enemy2.spawnx > self.xpos:
                if self.score >= 5:
                    self.exchange2 = -5
                    self.eychange2 = 8
                elif self.score >= 10:
                    self.exchange2 = -14
                    self.eychange2 = 18
                elif self.score >= 20:
                    self.exchange2 = -18
                    self.eychange2 = 25

                else:
                    self.exchange2 = -2
                    self.eychange2 = 4
            else:
                if self.score >= 5:
                    self.exchange2 = 5
                    self.eychange2 = 8
                elif self.score >= 10:
                    self.exchange2 = 14
                    self.eychange2 = 18
                elif self.score >= 20:
                    self.exchange2 = 18
                    self.eychange2 = 25
                else:
                    self.exchange2 = 2
                    self.eychange2 = 4

            if self.enemy.spawnx == self.xpos:
                self.exchange = 0

            if self.enemy2.spawnx == self.xpos:
                self.exchange2 = 0

            if self.score >= 5:
                self.eychange3 = 15
            elif self.score >= 10:
                self.eychange3 = 30
            elif self.score >= 10:
                self.eychange3 = 40
            else:
                self.eychange3 = 10



            if self.enemy.spawnx <= 0 or self.enemy.spawnx >= self.display_width or self.enemy.spawny <= 0 or self.enemy.spawny >= self.display_height or self.enemy.hp==0:
                self.enemy.spawny =10
                self.enemy.spawnx = random.randrange(1,799)
                self.enemy.hp = 50

            if self.enemy2.spawnx <= 0 or self.enemy2.spawnx >= self.display_width or self.enemy2.spawny <= 0 or self.enemy2.spawny >= self.display_height or self.enemy2.hp == 0:
                self.enemy2.spawny =10
                self.enemy2.spawnx = random.randrange(1,799)
                self.enemy2.hp = 75

            if self.enemy3.spawnx <= 0 or self.enemy3.spawnx >= self.display_width or self.enemy3.spawny <= 0 or self.enemy3.spawny >= self.display_height or self.enemy3.hp == 0:
                self.enemy3.spawny = 10
                self.enemy3.spawnx = self.xpos
                self.enemy3.hp = 1000000


            if self.bullet.xpos > self.enemy.spawnx-30 and self.bullet.xpos < self.enemy.spawnx +30:
                if self.bullet.ypos > self.enemy.spawny-30 and self.bullet.ypos < self.enemy.spawny +30:
                    self.bullet.ypos = self.ypos
                    self.bullet.xpos = self.xpos
                    self.enemy.hp -= 25
                    if self.enemy.hp == 0:
                        self.score +=1
            if self.bullet.xpos > self.enemy2.spawnx-50 and self.bullet.xpos < self.enemy2.spawnx +50:
                if self.bullet.ypos > self.enemy2.spawny-30 and self.bullet.ypos < self.enemy2.spawny +30:
                    self.bullet.ypos = self.ypos
                    self.bullet.xpos = self.xpos
                    self.enemy2.hp -= 25
                    if self.enemy2.hp == 0:
                        self.score +=1


            if self.enemy.spawnx >= self.xpos and self.enemy.spawnx <= self.xpos +60 :
                if self.enemy.spawny >= self.ypos and self.enemy.spawny <= self.ypos + 100:
                    self.enemy.spawny = 10
                    self.enemy.spawnx = random.randrange(1, 799)
                    self.enemy.hp = 50
                    self.live -=1

            if self.enemy2.spawnx >= self.xpos and self.enemy2.spawnx <= self.xpos +60 :
                if self.enemy2.spawny >= self.ypos and self.enemy2.spawny <= self.ypos + 100:
                    self.enemy2.spawny = 10
                    self.enemy2.spawnx = random.randrange(1, 799)
                    self.enemy2.hp = 75
                    self.live -=1


            if self.enemy3.spawny+80 >= self.ypos and self.enemy3.spawny +80 <= self.ypos + 100:
                if self.enemy3.spawnx >= self.xpos and self.enemy3.spawnx <= self.xpos + 60 or self.enemy3.spawnx + 50 >= self.xpos and self.enemy3.spawnx + 50 <= self.xpos + 60:
                    self.enemy3.spawny = 10
                    self.enemy3.spawnx = self.xpos
                    self.enemy2.hp = 1000000
                    self.live -=1

            self.bullet.ypos -= 18

            self.eychange2 = 8
            self.enemy3.spawny += self.eychange3
            self.enemy3.spawnx +=0
            self.enemy2.spawnx += self.exchange2
            self.enemy2.spawny += self.eychange2
            self.xpos += self.xchange
            self.ypos += self.ychange
            self.enemy.spawnx += self.exchange
            self.enemy.spawny += self.eychange

            pygame.draw.circle(self.main1, self.white, [self.enemy.spawnx, self.enemy.spawny], self.enemy.radius)
            pygame.draw.circle(self.main1, self.white, [self.enemy2.spawnx, self.enemy2.spawny], self.enemy2.radius)
            pygame.draw.rect(self.main1, self.white, [self.xpos, self.ypos, 60, 100])
            pygame.draw.rect(self.main1, self.white, [self.bullet.xpos, self.bullet.ypos, 20, 20])
            pygame.draw.rect(self.main1, self.white,[self.enemy3.spawnx, self.enemy3.spawny, self.enemy3.width, self.enemy3.height])

            self.background()
            self.scoreshow()
            self.liveshow()
            self.playerface()
            self.bulletface()
            self.enemyFace()


            if self.live == 0:
                self.gamestat = False

            if self.bullet.xpos > self.enemy.spawnx-30 and self.bullet.xpos < self.enemy.spawnx +30:
                if self.bullet.ypos > self.enemy.spawny-30 and self.bullet.ypos < self.enemy.spawny +30:
                    self.boom()
            if self.bullet.xpos > self.enemy2.spawnx-60 and self.bullet.xpos < self.enemy2.spawnx +60:
                if self.bullet.ypos > self.enemy2.spawny-30 and self.bullet.ypos < self.enemy2.spawny +30:
                    self.boom()
            self.fps.tick(self.FPS)


            pygame.display.update()

        time.sleep(1)



class enemy(metaclass=ABCMeta):
    def __init__(self,hp):
        self.spawnx=random.randrange(0,799)
        self.spawny=10
        self.hp = hp


class Ebasic(enemy):
    def __init__(self):
        super().__init__(50)
        self.radius = 35

class Eadvanced(enemy):
    def __init__(self):
        super().__init__(75)
        self.radius = 40

class Emissile(enemy):
    def __init__(self):
        super().__init__(1000000)
        self.width = 50
        self.height = 80

class Bullet(metaclass=ABCMeta):
    def __init__(self,xpos,ypos,damage):
        self.xpos=xpos
        self.ypos = ypos
        self.damage=damage

class bullet1(Bullet):
    def __init__(self,xpos,ypos,damage):
        super().__init__(xpos,ypos,damage)
        self.size = 20

def main():
    game = True

    while game:
        intro = theintro()
        if intro.howtoplaycheck == True:
            howtoplay()
        maingame=themaingame()
        maingame.gameloop()
        end=ending()

main()