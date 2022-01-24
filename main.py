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
# где-то здесь расписывются классы


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = load_image('player.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        # self.pos_x = self.rect.x
        # self.pos_y = self.rect.y
        player_group.add(self)# он ниче не умеет делать
        self.move_down = False# вверх
        self.move_up = 0
        self.max = 160
        self.pressedRight, self.pressedLeft = False, False
        self.val = 10
        self.h = 40

    def update(self):
        if self.move_down == True:
            gg = 0
            if pygame.sprite.spritecollideany(self, usual_blocks):
                block = pygame.sprite.spritecollide(self, usual_blocks, False)[0]
                print(block.rect.y, self.rect.y)
                if block.rect.y == self.rect.y + self.h:
                    self.move_down = False
                    self.max = 160
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


class Block_dis(pygame.sprite.Sprite):#просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(dis_blocks, all_sprites)
        self.image = load_image('bl.jpg')
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        dis_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


class Moneta(pygame.sprite.Sprite):#просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(moneta_blocks, all_sprites)
        self.image = load_image('u.jpg')
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        moneta_blocks.add(self)
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

class Camera:import random
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
# где-то здесь расписывются классы


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = load_image('player.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        # self.pos_x = self.rect.x
        # self.pos_y = self.rect.y
        player_group.add(self)# он ниче не умеет делать
        self.move_down = False# вверх
        self.move_up = 0
        self.max = 160
        self.pressedRight, self.pressedLeft = False, False
        self.val = 10
        self.h = 40

    def update(self):
        if self.move_down == True:
            gg = 0
            if pygame.sprite.spritecollideany(self, usual_blocks):
                block = pygame.sprite.spritecollide(self, usual_blocks, False)[0]
                print(block.rect.y, self.rect.y)
                if block.rect.y == self.rect.y + self.h:
                    self.move_down = False
                    self.max = 160
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


class Block_dis(pygame.sprite.Sprite):#просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(dis_blocks, all_sprites)
        self.image = load_image('bl.jpg')
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        dis_blocks.add(self)
        all_sprites.add(self)
        self.y = pos_y // tile_height


class Moneta(pygame.sprite.Sprite):#просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(moneta_blocks, all_sprites)
        self.image = load_image('u.jpg')
        # self.rect = self.image.get_rect().move(
        #     tile_width * pos_x, tile_height * pos_y)
        self.rect = self.image.get_rect().move(pos_x, pos_y)
        moneta_blocks.add(self)
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
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - h // 2)


def generate_level(level):
    global last
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):# если в txt файле че то там, то такой то класс то-т
            if level[y][x] == 'B':
                if y == 0:
                    last = Block(tile_width * x, tile_height * y)
                else:
                    Block(tile_width * x, tile_height * y)

            elif level[y][x] == 'G':
                Block_dis(tile_width * x, tile_height * y)

            elif level[y][x] == '#':
                a = random.randint(1, 50)
                if a == 1:
                    Moneta(tile_width * x, tile_height * y)

            elif level[y][x] == 'H':
                new_player = Player(x, y)
                print("1", new_player.rect.y)
    return new_player, x, y


def generate_new_level(level):
    global last
    level_y = random.choice(level[6:0:-2])
    print(level_y)
    for x in range(len(level_y)):
        if level_y[x] == 'B':
            new = Block(tile_width * x, last.rect.y - 100)
        elif level_y[x] == '#':
            a = random.randint(1, 50)
            if a == 1:
                new = Moneta(tile_width * x, last.rect.y - 100)
        elif level_y[x] == 'G':
            new = Block_dis(tile_width * x, last.rect.y - 100)
    last = new

if __name__ == '__main__':
    #какие то константы
    running = True
    tile_width = tile_height = 50
    size = w, h = 500, 400
    screen = pygame.display.set_mode(size)
    fps = 30
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 500)
    clock = pygame.time.Clock()
    bg = load_image("screen.jpg")

    all_sprites = pygame.sprite.Group()
    usual_blocks = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    dis_blocks = pygame.sprite.Group()
    moneta_blocks = pygame.sprite.Group()

    player, level_x, level_y = generate_level(load_level('fon.txt'))
    generate_new_level(load_level('fon.txt'))
    camera = Camera()
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
                generate_new_level(load_level('fon.txt'))
        player_group.update()
        screen.blit(bg, (0, 0)) #вообще здесь должна быть картинка с фоном, но пока что так
        usual_blocks.draw(screen)
        player_group.draw(screen)
        dis_blocks.draw(screen)
        moneta_blocks.draw(screen)
        pygame.display.flip()

        clock.tick(fps)
        for sprites in all_sprites:
             camera.apply(sprites)
    pygame.quit()
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dy = -(target.rect.y + target.rect.h // 2 - h // 2)


def generate_level(level):
    global last
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):# если в txt файле че то там, то такой то класс то-т
            if level[y][x] == 'B':
                if y == 0:
                    last = Block(tile_width * x, tile_height * y)
                else:
                    Block(tile_width * x, tile_height * y)

            elif level[y][x] == 'G':
                Block_dis(tile_width * x, tile_height * y)

            elif level[y][x] == '#':
                a = random.randint(1, 15)
                if a == 1:
                    Moneta(tile_width * x, tile_height * y)

            elif level[y][x] == 'H':
                new_player = Player(x, y)
                print("1", new_player.rect.y)
    return new_player, x, y


def generate_new_level(level):
    global last
    level_y = random.choice(level[6:0:-2])
    print(level_y)
    for x in range(len(level_y)):
        if level_y[x] == 'B':
            new = Block(tile_width * x, last.rect.y - 100)
        elif level_y[x] == 'G':
            new = Block_dis(tile_width * x, last.rect.y - 100)
    last = new

if __name__ == '__main__':
    #какие то константы
    running = True
    tile_width = tile_height = 50
    size = w, h = 500, 400
    screen = pygame.display.set_mode(size)
    fps = 30
    MYEVENTTYPE = pygame.USEREVENT + 1
    pygame.time.set_timer(MYEVENTTYPE, 500)
    clock = pygame.time.Clock()
    bg = load_image("screen.jpg")

    all_sprites = pygame.sprite.Group()
    usual_blocks = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    dis_blocks = pygame.sprite.Group()
    moneta_blocks = pygame.sprite.Group()

    player, level_x, level_y = generate_level(load_level('fon.txt'))
    generate_new_level(load_level('fon.txt'))
    camera = Camera()
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
                generate_new_level(load_level('fon.txt'))
        player_group.update()
        screen.blit(bg, (0, 0)) #вообще здесь должна быть картинка с фоном, но пока что так
        usual_blocks.draw(screen)
        player_group.draw(screen)
        dis_blocks.draw(screen)
        moneta_blocks.draw(screen)
        pygame.display.flip()

        clock.tick(fps)
        for sprites in all_sprites:
             camera.apply(sprites)
    pygame.quit()