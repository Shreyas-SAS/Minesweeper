
import pygame


class Mine(pygame.sprite.Sprite):
    def __init__(self, images, position, status_code=0, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.images = images
        self.image = self.images['blank']
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.status_code = status_code
        self.is_mine_flag = False
        self.num_mines_around = -1
    def setstatus(self, status_code):
        self.status_code = status_code
    def burymine(self):
        self.is_mine_flag = True
    def setnumminesaround(self, num_mines_around):
        self.num_mines_around = num_mines_around
    def draw(self, screen):
        if self.status_code == 0:
            self.image = self.images['blank']
        elif self.status_code == 1:
            self.image = self.images['mine'] if self.is_mine_flag else self.images[str(self.num_mines_around)]
        elif self.status_code == 2:
            self.image = self.images['flag']
        elif self.status_code == 3:
            self.image = self.images['ask']
        elif self.status_code == 4:
            assert not self.is_mine_flag
            self.image = self.images[str(self.num_mines_around)]
        elif self.status_code == 5:
            self.image = self.images['0']
        elif self.status_code == 6:
            assert self.is_mine_flag
            self.image = self.images['blood']
        elif self.status_code == 7:
            assert not self.is_mine_flag
            self.image = self.images['error']
        screen.blit(self.image, self.rect)
    @property
    def opened(self):
        return self.status_code == 1