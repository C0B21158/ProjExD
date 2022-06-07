
import pygame as pg
import sys
import random
import sys


score = 0


class Score:
    def __init__(self, ft,size, sc, co):        
        self.score = sc
        self.color = co                                 #生き延びていた時間を加算
        self.fonto = pg.font.Font(ft, size)                           #Scoreの時間を表示
        self.txt = "SCORE:" + str(self.score)
        self.text = self.fonto.render(self.txt, True, self.color)

    def update(self):
        self.score += 1
        self.txt = "SCORE:" + str(self.score)          #
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


class Reticle(pg.sprite.Sprite):

    def __init__(self, fn, xy ):
        super().__init__()
        self.image =pg.image.load(fn)                     #こうかとんの画像をロードする
        self.image.set_colorkey((255,255,255))            #白色を透明化する
        self.image = pg.transform.rotozoom(self.image, 0,1.0 )
        self.rect= self.image.get_rect()
        self.rect.center = xy   
        pg.mouse.set_visible(False)
       
    def update(self, pos):
        self.rect.center = pos


class Bomb(pg.sprite.Sprite):
    def __init__(self,cl,r,screen):
        super().__init__()
        self.image = pg.Surface((2*r,2*r))        #爆弾の大きさ
        self.image.set_colorkey((0,0,0))          
        pg.draw.circle(self.image, (cl), (r,r), r)   #円を描く
        self.rect = self.image.get_rect()                    
        self.rect.centerx = random.randint(0, screen.rect.width)
        self.rect.centery = random.randint(0, screen.rect.height)
                           # 爆弾用のSurfaceを画面用Surfaceに貼り付ける


def main():
    clock = pg.time.Clock()

    screen = Screen("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/pg_bg.jpg",(1600,900),"射的ゲーム")
    screen.disp.blit(screen.image,(0,0),screen.rect )

    Reticles = pg.sprite.Group()     #動くこうかとん用Surface
    Reticles.add(Reticle("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/5.png",pg.mouse.get_pos()))

    bombs =pg.sprite.Group()
    bombs.add(Bomb((0,0,255),30, screen))       # 爆弾用のSurface # 爆弾用のSurfaceを画面用Surfaceに貼り付ける

    score = Score(None, 70,0, "BLACK")        #Score用のSurface
    screen.disp.blit(score.text,(70,70))


    while True:
        screen.disp.blit(screen.image,(0,0),screen.rect )

        bombs.draw(screen.disp)

        Reticles.update(pg.mouse.get_pos())
        Reticles.draw(screen.disp)

        screen.disp.blit(score.text,(70,70))
        
        for event in pg.event.get():        #こうかとんが爆弾と接触しているか判定
            if event.type == pg.MOUSEBUTTONDOWN:
                if len(pg.sprite.groupcollide(Reticles,bombs, 0, 1)) != 0:
                    score.update()
                    bombs.add(Bomb((0,0,255), 30, screen))   #新しい爆弾を作る

            pg.display.update()
                # 画面の更新
            clock.tick(1000)
        
        

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