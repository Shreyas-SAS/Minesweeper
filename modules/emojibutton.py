
import pygame


class EmojiButton(pygame.sprite.Sprite):
    def __init__(self, images, position, status_code=0, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images['face_normal']
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.status_code = status_code
    def draw(self, screen):
        if self.status_code == 0:
            self.image = self.images['face_normal']
        elif self.status_code == 1:
            self.image = self.images['face_fail']
        elif self.status_code == 2:
            self.image = self.images['face_success']
        screen.blit(self.image, self.rect)
    def setstatus(self, status_code):
        self.status_code = status_code