import random
import pygame
import os
import sys
pygame.init()


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
# здесь расписывются классы


# герой
class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.skin = 1
        self.image = load_image(f'player{self.skin}.png', -1)
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        player_group.add(self)
        self.move_down = False#вверх
        self.move_up = 0
        self.max = self.usual_max = 250
        self.pressedRight, self.pressedLeft = False, False
        self.val = self.usual_val = 10
        self.h = 70

    # смена скина героя
    def skin_change(self):
        global smoke_show
        if monetki / 10 == self.skin and self.skin < 5:
            self.skin += 1
            self.image = load_image(f'player{self.skin}.png', -1)
            self.rect = self.image.get_rect().move(
                self.rect.x, self.rect.y)
            smoke_show = True

    # движение героя
    def update(self):
        global level_now
        if self.move_down == True:
            # обычный блок
            if pygame.sprite.spritecollideany(self, usual_blocks):
                block = pygame.sprite.spritecollide(self, usual_blocks, False)[0]
                print(block.rect.y, self.rect.y)
                if block.rect.y == self.rect.y + self.h:
                    self.move_down = False
                    self.max = self.usual_max
                    self.val = self.usual_val
                    level_now = block
                else:
                    self.val = self.usual_val
                    self.rect.y += self.val

            # ломающийся блок
            elif pygame.sprite.spritecollideany(self, сloud_blocks):
                block = pygame.sprite.spritecollide(self, сloud_blocks, False)[0]
                if block.rect.y == self.rect.y + self.h:
                    level_now = block
                    self.move_down = False
                    self.max = self.usual_max * 10
                    self.val = self.usual_val * 1.25
                else:
                    self.val = self.usual_val
                    self.rect.y += self.val

            # батут
            elif pygame.sprite.spritecollideany(self, dis_blocks):
                block = pygame.sprite.spritecollide(self, dis_blocks, False)[0]
                print(block.rect.y, self.rect.y)
                if block.rect.y == self.rect.y + self.h:
                    self.move_down = False
                    self.max = self.usual_max * 2
                    self.val = self.usual_val * 2
                    level_now = block
                else:
                    self.val = 10
                    self.rect.y += self.val

            else:
                self.val = self.usual_val
                self.rect.y += self.val

        else:
            if self.move_up == self.max:
                self.val = self.usual_val
                self.move_up = 0
                self.move_down = True
                self.rect.y -= self.val
            else:
                self.rect.y -= self.val
                self.move_up += self.val
        if self.pressedRight == True:
            self.rect.x += self.usual_val
        if self.pressedLeft == True:
            self.rect.x -= self.usual_val
        global monetki
        if pygame.sprite.spritecollideany(self, moneta_blocks):
            block = pygame.sprite.spritecollide(self, moneta_blocks, False)[0]
            print(block.rect.y, "  ", self.rect.y)
            if self.rect.y < block.rect.y:
                monetki += 1
                pygame.sprite.spritecollide(self, moneta_blocks, True)

        if self.rect.x > w:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = w


# анимация смены героя
class Smoke_Animation(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows):
        super().__init__(smoke_group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        global smoke_show
        self.rect.x, self.rect.y = player.rect.x, player.rect.y
        print(self.rect.x, self.rect.y, "!!!")
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        if self.cur_frame == 9:
            smoke_show = False

# рамен
class Ramen(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(moneta_blocks, all_sprites)
        self.image = load_image('ramen.png', -1)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        moneta_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


# батут
class Block_trampoline(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(dis_blocks, all_sprites)
        self.image = load_image('block_trampoline.jpg')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        dis_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


# блок- полёт
class Сloud_block(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(сloud_blocks, all_sprites)
        self.image = load_image('сloud_block.png', -1)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        сloud_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


# просто блок
class Block(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(usual_blocks, all_sprites)
        self.image = load_image('usual_block.jpg')
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        usual_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


# слежение камеры за героем
class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.y += self.dy + 80

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - h // 2)



def generate_level(level):
    global last, level_now
    new_player, x, y = None, None, None
    for y in range(len(level)):
        pop = 0
        for x in range(len(level[y])):
            # просто блок
            if level[y][x] == 'B':
                if y == 1:
                    last = Block(tile_width * x, tile_height * y)
                elif y == len(level) - 1:
                    level_now = Block(tile_width * x, tile_height * y)
                else:

                    Block(tile_width * x, tile_height * y)

            # батут
            elif level[y][x] == 'G':
                if y == 1:
                    last = Block_trampoline(tile_width * x, tile_height * y)
                else:
                    Block_trampoline(tile_width * x, tile_height * y)

            # Облако(ломающийся блок)
            elif level[y][x] == 'L':
                a = random.randint(1, 5)
                if a == 1 and pop == 0:
                    Сloud_block(tile_width * x, tile_height * y)
                    pop = 1
                else:
                    if y == 1:
                        last = Block(tile_width * x, tile_height * y)
                    elif y == len(level) - 1:
                        level_now = Block(tile_width * x, tile_height * y)
                    else:

                        Block(tile_width * x, tile_height * y)
            # герой
            elif level[y][x] == 'H':
                new_player = Player(x, y)
    return new_player, x, y


def generate_new_level(level, old_lvl1, old_lvl2):
    global last
    gg = 0
    pop = 0
    level_y = random.choice(level[len(level) - 5:0:-3])
    while old_lvl1 == level_y or old_lvl2 == level_y:
        level_y = random.choice(level[len(level) - 5:0:-3])

    old_lvl2 = old_lvl1
    old_lvl1 = level_y
    for x in range(len(level_y)):
        # просто блок
        if level_y[x] == 'B':
            # рамен
            a = random.randint(1, 5)
            if a == 1 and gg == 0:
                Ramen(tile_width * x, last.rect.y - 250)
                gg = 1
            new = Block(tile_width * x, last.rect.y - 200)

        # батут
        elif level_y[x] == 'G':
            # рамен
            a = random.randint(1, 5)
            if a == 1 and gg == 0:
                Ramen(tile_width * x, last.rect.y - 250)
                gg = 1

            new = Block_trampoline(tile_width * x, last.rect.y - 200)


        # Облако(ломающийся блок)
        elif level_y[x] == 'L':
            a = random.randint(1, 5)
            if a == 1 and pop == 0:
                new = Сloud_block(tile_width * x, last.rect.y - 200)
                pop = 1
            else:
                new = Block(tile_width * x, last.rect.y - 200)
    last = new
    return old_lvl1, old_lvl2


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    screen.blit(bg, (0, 0))
    start = load_image("start.png", -1)
    screen.blit(start, (10, 150))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()


def finish_screen():
    screen.blit(bg, (0, 0))
    start = load_image("game over.jpg", -1)
    screen.blit(start, (10, 120))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
                # начинаем игру
        pygame.display.flip()


if __name__ == '__main__':
    #какие то константы
    running = True
    tile_width = tile_height = 50
    size = w, h = 500, 400
    pygame.display.set_caption("Naruto and ramen")
    screen = pygame.display.set_mode(size)
    fps = 30
    n = 1
    monetki = 0
    old_lvl1, old_lvl2 = -1, -1
    MYEVENTTYPE = pygame.USEREVENT + 1
    fps_change = pygame.USEREVENT + 2
    pygame.time.set_timer(MYEVENTTYPE, 100)
    pygame.time.set_timer(fps_change, 5000)
    clock = pygame.time.Clock()
    bg = load_image("screen.jpg")
    pygame.mixer.music.load('naruto.mp3')
    pygame.mixer.music.play()
    smoke_show = False


    all_sprites = pygame.sprite.Group()
    usual_blocks = pygame.sprite.Group()
    сloud_blocks = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    smoke_group = pygame.sprite.Group()
    dis_blocks = pygame.sprite.Group()
    moneta_blocks = pygame.sprite.Group()
    player, level_x, level_y = generate_level(load_level('fon.txt'))
    smoke = Smoke_Animation(load_image("smoke.png"), 10, 1)
    font = pygame.font.Font(None, 40)
    camera = Camera()
    start_screen()
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
            if event.type == fps_change:
                if fps <= 60:
                    fps += 0.5
                    print(fps)

        screen.blit(bg, (0, 0))
        usual_blocks.draw(screen)
        dis_blocks.draw(screen)
        сloud_blocks.draw(screen)
        moneta_blocks.draw(screen)
        if smoke_show:
            smoke_group.update()
            smoke_group.draw(screen)
        else:
            player_group.update()
            player.skin_change()
            player_group.draw(screen)
        screen.blit(font.render("Чашек рамена: " + str(monetki), True, (255, 0, 0)), (250, 0))
        pygame.display.flip()
        clock.tick(fps)
        for sprites in all_sprites:
             camera.apply(sprites)
        if player.rect.y + 50 > level_now.rect.y:
            finish_screen()
    pygame.quit()