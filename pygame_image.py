import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    cr_img = pg.image.load("fig/3.png")
    bgr_imp = pg.transform.flip(bg_img, True ,False)
    cr_imag= pg.transform.flip(cr_img ,True ,False)
    cr_rct = cr_img.get_rect()  
    cr_rct.center = 300, 200    
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        #描画
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bgr_imp,[-x+1600,0])
        screen.blit(bg_img,[-x+3200,0])
        screen.blit(bgr_imp,[-x+4800,0])

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            cr_rct.move_ip(0,-1)
        if key_lst[pg.K_DOWN]:
            cr_rct.move_ip(0,1)
        if key_lst[pg.K_RIGHT]:
            cr_rct.move_ip(1,0)
        if key_lst[pg.K_LEFT]:
            cr_rct.move_ip(-1,0)   
        screen.blit(cr_imag, cr_rct)
  
  
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()