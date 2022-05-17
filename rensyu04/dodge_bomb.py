import pygame as pg
import sys

def main():
    clock = pg.time.Clock()

    pg.display.set_caption("逃げろ！工科豚")  #タイトルバーに「初めての…」を表示する
    screen = pg.display.set_mode((1600,900)) #画面用Surface
    sc_rect = screen.get_rect()
    bg_img =pg.image.load("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/pg_bg.jpg")
    bg_rect = bg_img.get_rect()
    screen.blit(bg_img, bg_rect)

    #練習３
    tori_img = pg.image.load("c:/Users/admin/Documents/二年生　前期/プロジェクト/ProjExD2022/ProjExD_pub/fig/")
    tori_img = pg.transform.rotozoom(tori_img,0,2.0)
    tori_rect = tori_img.get_rect()
    tori_rect.center = 900,400
    screen.blit(tori_img,tori_rect)


    while True:
        #練習２
        screen.blit(bg_img, bg_rect)
        for  event in pg.event.get():
            if event.type == pg.QUIT : return

        pg.display.update()
        clock.tick(0.5)



if __name__ == "__main__":
    pg.init()       #モジュールを初期化する
    main()
    pg.quit()       #モジュールの初期化をかいじょする
    sys.exit()      #プログラミングを終了する
    