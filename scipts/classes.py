import pygame
import main

PX_PER_TILE = main.PX_PER_TILE

class Tile:
    # INIT
    def __init__(self, path, row, col, w, h):
        self.path = path
        self.row = row
        self.col = col
        self.w = w
        self.h = h
    # SET
    def set_path(self, path):
        self.path = path
    def set_row(self, row):
        self.row = row
    def set_col(self, col):
        self.col = col
    def set_w(self, w):
        self.w = w
    def set_h(self, h):
        self.h = h
    
    # GET
    def get_path(self):
        return self.path
    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    def get_w(self):
        return self.w
    def get_h(self):
        return self.h

    def draw_image(self, path, row, col, w, h):
        img = pygame.transform.scale(pygame.image.load(path), (w, h))
        main.WIN.blit(img, (row * PX_PER_TILE, col * PX_PER_TILE))

class Move:
    # INIT
    def __init__(self, name, type, category, pp, power, accuracy):
        self.name = name
        self.type = type
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
    # SET
    def set_name(self, name):
        self.name = name
    def set_type(self, type):
        self.type = type
    def set_category(self, category):
        self.category = category
    def set_pp(self, pp):
        self.pp = pp
    def set_power(self, power):
        self.power = power
    def set_accuracy(self, accuracy):
        self.accuracy = accuracy
    
    # GET
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type
    def get_category(self):
        return self.category
    def get_pp(self):
        return self.pp
    def get_power(self):
        return self.power
    def get_accuracy(self):
        return self.accuracy

class Pokemon:
    # INIT
    def __init__(self, ndex, name, types, abilities, stats):
        self.ndex = ndex
        self.name = name
        self.types = types
        self.abilities = abilities
        self.stats = stats
    #SET
    def set_ndex(self, ndex):
        self.ndex = ndex
    def set_name(self, name):
        self.name = name
    def set_types(self, types):
        self.types = types
    def set_abilities(self, abilities):
        self.abilities = abilities
    def set_stats(self, stats):
        self.stats = stats

    #GET
    def get_ndex(self):
        return self.ndex
    def get_name(self):
        return self.name
    def get_types(self):
        return self.types
    def get_abilities(self):
        return self.abilities
    def get_stats(self):
        return self.stats

class Trainer:
    # INIT
    def __init__(self, path, row, col, x, y, w, h):
        self.path = path
        self.row = row
        self.col = col
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    # SET
    def set_path(self, path):
        self.path = path
    def set_row(self, row):
        self.row = row
    def set_col(self, col):
        self.col = col
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def set_w(self, w):
        self.w = w
    def set_h(self, h):
        self.h = h
    
    # GET
    def get_path(self):
        return self.path
    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_w(self):
        return self.w
    def get_h(self):
        return self.h

class Item:
    def __init__(self, ):
        pass