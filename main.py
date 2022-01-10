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
        self.pos_x = self.rect.x
        self.pos_y = self.rect.y
        player_group.add(self) #он ниче не умеет делать


class Block(pygame.sprite.Sprite): # просто блок
    def __init__(self, pos_x, pos_y):
        super().__init__(usual_blocks, all_sprites)
        self.image = load_image('usual_block.jpg')
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        usual_blocks.add(self)
        all_sprites.add(self)


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])): #если в txt файле че то там, то такой то класс то-то
            if level[y][x] == 'B':
                Block(x, y)
            elif level[y][x] == 'H':
                Player(x, y)
    return new_player, x, y




if __name__ == '__main__':
    #какие то константы
    running = True
    tile_width = tile_height = 50
    size = w, h = 500, 400
    screen = pygame.display.set_mode(size)
    FPS = 50
    clock = pygame.time.Clock()




    player = None
    all_sprites = pygame.sprite.Group()
    usual_blocks = pygame.sprite.Group()
    player_group = pygame.sprite.Group()

    player, level_x, level_y = generate_level(load_level('fon.txt'))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                player_group.update(event) #пока что не написано
        screen.fill((0, 0, 0)) #вообще здесь должна быть картинка с фоном, но пока что так
        usual_blocks.draw(screen)
        player_group.draw(screen)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()


