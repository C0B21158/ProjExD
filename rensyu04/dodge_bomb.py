import pygame as pg
import sys
import random 
#練習４
key_delta = {pg.K_UP     : [0 , -1],
             pg.K_DOWN   : [0 , +1],
             pg.K_LEFT   : [-1,  0],
             pg.K_RIGHT  : [+1,  0]
             }

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！工科豚")  #タイトルバーに「初めての…」を表示する
    screen = pg.display.set_mode((1600,900)) #画面用Surface
    sc_rect = screen.get_rect()
    bg_img =pg.image.load("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/pg_bg.jpg")
    bg_rect = bg_img.get_rect()
    screen.blit(bg_img, bg_rect)

    #練習３
    tori_img = pg.image.load("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/6.png")
    tori_img = pg.transform.rotozoom(tori_img,0,2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900,400
    screen.blit(tori_img,tori_rect)

    #練習５
    bomb = pg.Surface((20,20))     #爆弾用Surface 
    bomb.set_colorkey((0,0,0))
    pg.draw.circle(bomb, (255,0, 0), (10,10),10)
    bomb_rect = bomb.get_rect()
    bomb_rect.centerx = random.randint(0,sc_rect.width)
    bomb_rect.centery = random.randint(0,sc_rect.height)
    screen.blit(bomb, bomb_rect)    #爆弾用のSurfaceを画面用に貼り付け

    while True:
        #練習２
        screen.blit(bg_img, bg_rect)
        for  event in pg.event.get():
            if event.type == pg.QUIT : return

        key_states = pg.key.get_pressed()
        for key, delta in key_delta.items():
            if key_states[key] == True:
                tori_rect.centerx += delta[0]
                tori_rect.centery += delta[1]
        screen.blit(tori_img, tori_rect)

        #練習６
        vx, vy = +1, +1
        bomb_rect.move_ip(vx,vy)
        screen.blit(bomb,bomb_rect)

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()       #モジュールを初期化する
    main()
    pg.quit()       #モジュールの初期化をかいじょする
    sys.exit()      #プログラミングを終了する
    