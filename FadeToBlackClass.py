# -*- coding: utf-8 -*-

import pygame


class Fade(pygame.sprite.Sprite):

    def __init__(self, direction):
        super(Fade, self).__init__()
        self.rect = pygame.display.get_surface().get_rect()
        self.image = pygame.Surface(self.rect.size, flags=pygame.SRCALPHA)
        if direction == 0:
            self.alpha = 0
            self.direction = 50
        elif direction == 1:
            self.alpha = 155
            self.direction = -30
        elif direction == 2:
            self.alpha = 255
            self.direction = -50

    def update(self):
        self.image.fill((0, 0, 0, self.alpha))
        if self.direction > 0:
            if self.alpha + self.direction <= 255:
                self.alpha += self.direction
            else:
                self.alpha = 255
        elif self.direction < 0:
            if self.alpha + self.direction >= 0:
                self.alpha += self.direction
            else:
                self.alpha = 0
