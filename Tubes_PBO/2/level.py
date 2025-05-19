import pygame
from support import import_csv_file

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface

        terrain_layout = import_csv_file(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')
        
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell != '-1':
                    x = col_index * 64
                    y = row_index * 64
                    sprite = pygame.sprite.Sprite()
                    sprite.image = pygame.Surface((64, 64))
                    sprite.rect = sprite.image.get_rect(topleft=(x, y))
                    sprite_group.add(sprite)
        return sprite_group

    def run(self):
        pass