import random
import pygame
import os
import sys
pygame.init()

monetki = 0
visota = 0
helovek = 100
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


def load_level(filename):
    filename = "data/" + filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))
# где-то здесь расписывются классы


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = load_image('player.png', -1)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        # self.pos_x = self.rect.x
        # self.pos_y = self.rect.y
        player_group.add(self)# он ниче не умеет делать
        self.move_down = False# вверх
        self.move_up = 0
        self.usual_max = 250
        self.max = self.usual_max
        self.pressedRight, self.pressedLeft = False, False
        self.val = 10
        self.h = 70

    def update(self):
        global visota, level_now
        if self.move_down == True:
            gg = 0
            if pygame.sprite.spritecollideany(self, usual_blocks):
                block = pygame.sprite.spritecollide(self, usual_blocks, False)[0]
                print(block.rect.y, self.rect.y)
                if block.rect.y == self.rect.y + self.h:
                    self.move_down = False
                    self.max = self.usual_max
                    self.val = 10
                    visota = self.rect.y
                    level_now = block
                else:
                    self.val = 10
                    self.rect.y += self.val
                    gg = 1

            if pygame.sprite.spritecollideany(self, lomaet_blocks):
                block = pygame.sprite.spritecollide(self, lomaet_blocks, False)[0]
                if block.rect.y == self.rect.y + self.h:
                    level_now = block
                    if pygame.sprite.spritecollide(self, lomaet_blocks, True):
                        self.move_down = False
                        self.max = self.usual_max
                        self.val = 10
                else:
                    self.val = 10
                    self.rect.y += self.val
                    gg = 1

            if pygame.sprite.spritecollideany(self, dis_blocks):
                block = pygame.sprite.spritecollide(self, dis_blocks, False)[0]
                print(block.rect.y, self.rect.y)
                if block.rect.y == self.rect.y + self.h:
                    self.move_down = False
                    self.max = 560
                    self.val = 20
                    level_now = block
                else:
                    self.val = 10
                    self.rect.y += self.val
                    gg = 1

            elif gg == 0:
                self.val = 10
                self.rect.y += self.val

        else:
            if self.move_up == self.max:
                self.val = 10
                self.move_up = 0
                self.move_down = True
                self.rect.y -= self.val
            else:
                self.rect.y -= self.val
                self.move_up += self.val
        if self.pressedRight == True:
            self.rect.x += 0.75 * self.val
        if self.pressedLeft == True:
            self.rect.x -= 0.75 * self.val
        global monetki
        if pygame.sprite.spritecollide(self, moneta_blocks, True):
            monetki += 1


class Block_dis(pygame.sprite.Sprite):#просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(dis_blocks, all_sprites)
        self.image = load_image('block_dis.jpg')
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        dis_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


class Moneta(pygame.sprite.Sprite):# просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(moneta_blocks, all_sprites)
        self.image = load_image('ramen.png', -1)
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        moneta_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


class Block_lomaet(pygame.sprite.Sprite):# просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(lomaet_blocks, all_sprites)
        self.image = load_image('block_lom.png', -1)
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        lomaet_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


class Block(pygame.sprite.Sprite):#просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(usual_blocks, all_sprites)
        self.image = load_image('usual_block.jpg')
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        usual_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height

class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        global visota
        global helovek
        #helovek = obj.rect.y + self.dy
        #obj.rect.y = max(visota, helovek)
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - h // 2)



def generate_level(level):
    global last, level_now
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):# если в txt файле че то там, то такой то класс то-т

            if level[y][x] == 'B':
                if y == 1:
                    last = Block(tile_width * x, tile_height * y)
                elif y == len(level) - 1:
                    level_now = Block(tile_width * x, tile_height * y)
                else:

                    Block(tile_width * x, tile_height * y)

            elif level[y][x] == 'G':
                if y == 1:
                    last = Block_dis(tile_width * x, tile_height * y)
                else:
                    Block_dis(tile_width * x, tile_height * y)


            elif level[y][x] == 'L':
                Block_lomaet(tile_width * x, tile_height * y)

            elif level[y][x] == 'H':
                new_player = Player(x, y)
    return new_player, x, y


def generate_new_level(level, old_lvl1, old_lvl2):
    global last
    gg = 0
    level_y = random.choice(level[len(level) - 5:0:-3])
    while old_lvl1 == level_y or old_lvl2 == level_y:
        level_y = random.choice(level[len(level) - 5:0:-3])

    old_lvl2 = old_lvl1
    old_lvl1 = level_y
    for x in range(len(level_y)):
        if level_y[x] == 'B':
            a = random.randint(1, 10)
            if a == 1 and gg == 0:
                Moneta(tile_width * x, last.rect.y - 250)
                gg = 1
            new = Block(tile_width * x, last.rect.y - 200)

        elif level_y[x] == 'G':
            a = random.randint(1, 10)
            if a == 1 and gg == 0:
                Moneta(tile_width * x, last.rect.y - 250)
                gg = 1
            new = Block_dis(tile_width * x, last.rect.y - 200)

        elif level_y[x] == 'L':
            new = Block_lomaet(tile_width * x, last.rect.y - 200)
    last = new
    return old_lvl1, old_lvl2


FPS = 50


def terminate():
    pygame.quit()
    sys.exit()


def start_screen(WIDTH, HEIGHT):
    screen.blit(bg, (0, 0))
    start = load_image("start.png", -1)
    screen.blit(start, (10, 150))
    # font = pygame.font.Font(None, 30)
    # text_coord = 50
    # for line in intro_text:
    #     string_rendered = font.render(line, 1, pygame.Color('red'))
    #     intro_rect = string_rendered.get_rect()
    #     text_coord += 10
    #     intro_rect.top = text_coord
    #     intro_rect.x = 10
    #     text_coord += intro_rect.height
    #     screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def finish_screen(w,h):
    screen.blit(bg, (0, 0))
    start = load_image("game over.jpg", -1)
    screen.blit(start, (10, 120))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
if __name__ == '__main__':
    #какие то константы
    running = True
    tile_width = tile_height = 50
    size = w, h = 500, 400
    screen = pygame.display.set_mode(size)
    fps = 30
    old_lvl1, old_lvl2 = -1, -1
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 500)
    clock = pygame.time.Clock()
    bg = load_image("screen.jpg")
    pygame.mixer.music.load('naruto.mp3')
    pygame.mixer.music.play()

    all_sprites = pygame.sprite.Group()
    usual_blocks = pygame.sprite.Group()
    lomaet_blocks = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    dis_blocks = pygame.sprite.Group()
    moneta_blocks = pygame.sprite.Group()
    player, level_x, level_y = generate_level(load_level('fon.txt'))
    font = pygame.font.Font(None, 40)
    camera = Camera()
    start_screen(w,h)
    while running:
        camera.update(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:  # правая стрелка
                if event.key == pygame.K_RIGHT:
                    player.pressedRight = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    player.pressedRight = False

            if event.type == pygame.KEYDOWN:  # левая стрелка
                if event.key == pygame.K_LEFT:
                    player.pressedLeft = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.pressedLeft = False
            if event.type == MYEVENTTYPE:
                old_lvl1, old_lvl2 = generate_new_level(load_level('fon.txt'), old_lvl1, old_lvl2)

        player_group.update()
        screen.blit(bg, (0, 0))
        # вообще здесь должна быть картинка с фоном, но пока что так
        usual_blocks.draw(screen)
        dis_blocks.draw(screen)
        lomaet_blocks.draw(screen)
        moneta_blocks.draw(screen)
        player_group.draw(screen)
        screen.blit(font.render("Чашек рамена: " + str(monetki), True, (255, 0, 0)), (250, 0))
        pygame.display.flip()

        clock.tick(fps)
        for sprites in all_sprites:
             camera.apply(sprites)
        if player.rect.y > level_now.rect.y:
            finish_screen(w,h)
            running = False
    pygame.quit()