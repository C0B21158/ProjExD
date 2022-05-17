import pygame as pg
import sys
import random 
#練習４
key_delta = {pg.K_UP     : [0 , -1],
             pg.K_DOWN   : [0 , +1],
             pg.K_LEFT   : [-1,  0],
             pg.K_RIGHT  : [+1,  0]
             }

sc = 0
def main():
    global sc
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
    vx, vy = +1, +1

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
                if check_bound(sc_rect, tori_rect) !=(1,1):
                    tori_rect.centerx -= delta[0]
                    tori_rect.centery -= delta[1]
        screen.blit(tori_img, tori_rect)

        #練習６
        
        bomb_rect.move_ip(vx,vy)
        screen.blit(bomb,bomb_rect)
        ret = check_bound(sc_rect,bomb_rect)
        #練習７
        vx *= ret[0] #横方向に画面外なら、符号転換
        vy *= ret[1] #縦方向

        sc += 1
        fonto = pg.font.Font(None, 80)
        txt = fonto.render(str(sc), True, "BLACK")
        screen.blit(txt,(1400,30))

        HARD_fonto = pg.font.Font(None, 50)
        HARD_txt = HARD_fonto.render("HARDmode: i", True, "BLACK")
        screen.blit(HARD_txt,(1300,100))

        key_inc = pg.key.get_pressed()
        if key_inc[pg.K_i]:    #早くなる
            vx *= 1.15
            vy *= 1.15


        #練習８
        if tori_rect.colliderect(bomb_rect):
            Game_Over()
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(sc_r, obj_r):
    x ,y = +1, +1
    if obj_r.left < sc_r.left or sc_r.right < obj_r.right: x = -1#画面外
    if obj_r.top < sc_r.top or sc_r.bottom < obj_r.bottom: y = -1
    return x , y



def Game_Over():    #GameOver画面
    while True:
        pg.display.set_caption("Game_Over")
        go_screen = pg.display.set_mode((1600,900)) 
        
        GameOV1 = pg.font.Font(None, 80)
        GameOV2 = pg.font.Font(None, 80)
        GameOV3 = pg.font.Font(None, 80)
        
        SCORE_OV = "SCORE:" + str(sc)
        GOtxt1 = GameOV1.render("Game_Over", True, "RED")
        GOtxt2 = GameOV2.render(SCORE_OV, True, "WHITE")
        GOtxt3 = GameOV3.render("FINISH: Q", True, "WHITE")

        go_screen.blit(GOtxt1,(600,400))
        go_screen.blit(GOtxt2,(600,500))
        go_screen.blit(GOtxt3,(600,600))

        pg.display.update()

        key_fi = pg.key.get_pressed()
        if key_fi[pg.K_q]:
            break

if __name__ == "__main__":
    pg.init()       #モジュールを初期化する
    main()
    pg.quit()       #モジュールの初期化をかいじょする
    sys.exit()      #プログラミングを終了する
    