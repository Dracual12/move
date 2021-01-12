import pygame, os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Car(pygame.sprite.Sprite):
    def __init__(self, screen2, image2, pos2):
        super().__init__()
        self.image = image2
        self.pos = pos2
        self.screen = screen2
        self.screen.blit(self.image, self.pos)

    def check(self, pos):
        if (pos[0] >= 450 and k == 1) or pos[0] <= 0 and (k <= -1):
            return True

    def transform(self, im):
        im2 = pygame.transform.flip(
                image, True, False)
        return im2


if __name__ == '__main__':
    image = load_image("car2.png")
    pygame.init()
    pygame.display.set_caption('Машинка')
    size = width, height = 600, 95
    screen = pygame.display.set_mode(size)
    running = True
    pos = [0, 0]
    v = 50
    k = 1
    clock = pygame.time.Clock()
    while running:
        screen.fill((255, 255, 255))
        car = Car(screen, image, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if car.check(pos):
            k *= -1
            image = car.transform(image)
        pos[0] += v * clock.tick() / 1000 * k
        pygame.display.flip()
    pygame.quit()
