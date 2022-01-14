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



#где-то здесь расписывются классы



class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = load_image('player.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        # self.pos_x = self.rect.x
        # self.pos_y = self.rect.y
        player_group.add(self) #он ниче не умеет делать
        self.move_down = False # вверх
        self.move_up = 0
        self.max = 120
        self.pressedRight, self.pressedLeft = False, False
        self.val = 5
        self.h = 40
    def update(self):
        if self.move_down == True:
            self.rect.y += self.val
            if pygame.sprite.spritecollideany(self, usual_blocks):
                block = pygame.sprite.spritecollide(self, usual_blocks, False)[0]
                print(block.rect.y)
                print(self.rect.y)
                if block.rect.y == self.rect.y + self.h:
                    self.move_down = False
                    self.rect.y -= 1.5 * self.val
                    self.move_up += self.val
        else:
            if self.move_up == self.max:
                self.move_up = 0
                self.move_down = True
                self.rect.y -= 1.5 * self.val
            else:
                self.rect.y -= 1.5 * self.val
                self.move_up += self.val
        if self.pressedRight == True:
            self.rect.x += 1.5 * self.val
        if self.pressedLeft == True:
            self.rect.x -= 1.5 * self.val

class Block(pygame.sprite.Sprite): # просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(usual_blocks, all_sprites)
        self.image = load_image('usual_block.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        usual_blocks.add(self)
        all_sprites.add(self)

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
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])): #если в txt файле че то там, то такой то класс то-то
            if level[y][x] == 'B':
                Block(x, y)
            elif level[y][x] == 'H':
                new_player = Player(x, y)
    return new_player, x, y




if __name__ == '__main__':
    #какие то константы
    running = True
    tile_width = tile_height = 50
    size = w, h = 500, 400
    screen = pygame.display.set_mode(size)
    fps = 60
    clock = pygame.time.Clock()
    bg = load_image("screen.jpg")
    all_sprites = pygame.sprite.Group()
    usual_blocks = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    player, level_x, level_y = generate_level(load_level('fon.txt'))
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
        player_group.update()
        screen.blit(bg, (0, 0)) #вообще здесь должна быть картинка с фоном, но пока что так
        usual_blocks.draw(screen)
        player_group.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()

        clock.tick(fps)
        for sprites in all_sprites:
             camera.apply(sprites)
    pygame.quit()

