# -*- coding: utf-8 -*-

import pygame


class Fade(pygame.sprite.Sprite):

    def __init__(self, fadeType):
        super(Fade, self).__init__()
        self.rect = pygame.display.get_surface().get_rect()
        self.image = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
        if fadeType == 0:
            self.alpha = 0
            self.direction = 50
        elif fadeType == 1:
            self.alpha = 155
            self.direction = -30
        elif fadeType == 2:
            self.alpha = 255
            self.direction = -50
        elif fadeType == 3:
            self.alpha = 0
            self.direction = 5
        self.fadeType = fadeType

    def update(self):
        self.image.fill((0, 0, 0, self.alpha))
        if self.direction > 0:
            if self.alpha + self.direction <= 255 and not (self.fadeType == 3 and self.alpha + self.direction >= 230):
                self.alpha += self.direction
            else:
                self.alpha = 255
        elif self.direction < 0:
            if self.alpha + self.direction >= 0:
                self.alpha += self.direction
            else:
                self.alpha = 0
