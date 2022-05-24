
import pygame as pg
import sys
import random

score = 0

class Score:
    def __init__(self, ft,size, sc, co):        
        self.score = sc
        self.color = co                                 #生き延びていた時間を加算
        self.fonto = pg.font.Font(ft, size)                           #Scoreの時間を表示
        self.txt = "SCORE" + str(self.score)
        self.text = self.fonto.render(self.txt, True, self.color)

    def update(self):
        self.score += 1
        self.txt = "SCORE" + str(self.score)
        self.text = self.fonto.render(self.txt, True, self.color)

class Screen:
    def __init__(self,fn, wh, title):
        #fn:背景画像のパス、 wh:幅高さのタプル 、title:画面のタイトル
        pg.display.set_caption(title)
        self.width, self.height = wh #(1600,900)
        self.disp= pg.display.set_mode((self.width,self.height)) #Sureface
        self.rect= self.disp.get_rect()  #Rect
        self.image = pg.image.load(fn)  # Sureface
        #self.rect = self.img.get_rect()


class Bird(pg.sprite.Sprite):
    key_delta = {pg.K_UP   : [0, -1],
             pg.K_DOWN : [0, +1],
             pg.K_LEFT : [-1, 0],
             pg.K_RIGHT: [+1, 0],}


    def __init__(self, fn, r, xy ):
        super().__init__()
        self.image =pg.image.load(fn)
        self.image = pg.transform.rotozoom(self.image, 0, r)
        self.rect= self.image.get_rect()
        self.rect.center = xy   
       

    def update(self, screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key] == True:
                self.rect.centerx += delta[0]
                self.rect.centery += delta[1]
                # 練習7
                if check_bound(screen.rect, self.rect) != (1,1): 
                    self.rect.centerx -= delta[0]
                    self.rect.centery -= delta[1]        


class Bomb(pg.sprite.Sprite):
    def __init__(self,cl,r,sp,screen):
        #cl:爆弾円の色
        # hf：爆弾円の半径
        # sp：爆弾円の速度のタプル
        # screen：爆弾円のSureface
        super().__init__()
        self.image = pg.Surface((2*r,2*r))
        self.image.set_colorkey((0,0,0))
        pg.draw.circle(self.image, (cl), (r,r), r)   
        self.rect = self.image.get_rect()                    
        self.rect.centerx = random.randint(0, screen.rect.width)
        self.rect.centery = random.randint(0, screen.rect.height)
                           # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
        self.vx, self.vy = sp

    def update(self,screen):
        self.rect.move_ip(self.vx, self.vy)
        x, y = check_bound(screen.rect, self.rect)
        self.vx *= x 
        self.vy *= y 


def main():
    clock = pg.time.Clock()
    
    # 練習1
    screen = Screen("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/pg_bg.jpg",(1600,900),"にげろ！こうかとん")
    screen.disp.blit(screen.image,(0,0),screen.rect )

    
    # 練習3
    tori = pg.sprite.Group()
    tori.add(Bird("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/5.png",1 ,(900,400)))
   
       

    # 練習5
    bomb = Bomb((255,0,0),10,(+2,+2), screen)                     # 爆弾用のSurface
    screen.disp.blit(bomb.image, bomb.rect)                   # 爆弾用のSurfaceを画面用Surfaceに貼り付ける
    bombs =pg.sprite.Group()
    for _ in range(5):
        bombs.add(Bomb((255,0,0),10*(_+1),(+2,+2), screen))

    score = Score(None, 70,0, "BLACK")
    screen.disp.blit(score.text,(70,70))

    while True:
        # 練習2
        screen.disp.blit(screen.image,(0,0),screen.rect )
        for event in pg.event.get():
            if event.type == pg.QUIT: return       

        # 練習4
        tori.update(screen)
        tori.draw(screen.disp)

        # 練習6
        bombs.update(screen)      
        bombs.draw(screen.disp)

        score.update()
        screen.disp.blit(score.text,(70,70))


        # 練習8      
        if len(pg.sprite.groupcollide(tori,bombs, False, False)) != 0:
            return
         # こうかとん用のRectが爆弾用のRectと衝突していたらreturn
         # collide_rect(sprite)
        
        pg.display.update()
          # 画面の更新
        clock.tick(1000)

    
# 練習7
def check_bound(sc_r, obj_r): # 画面用Rect, ｛こうかとん，爆弾｝Rect
    # 画面内：+1 / 画面外：-1
    x, y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right  < obj_r.right : x = -1
    if obj_r.top  < sc_r.top  or sc_r.bottom < obj_r.bottom: y = -1
    return x, y


if __name__ == "__main__":
    pg.init() 
    main()
    pg.quit()
    sys.exit()