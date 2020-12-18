import pygame, os, sys


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


if __name__ == '__main__':
    image = load_image("creature.png")
    pygame.init()
    pygame.display.set_caption('Свой курсор')
    size = width, height = 300, 300
    screen = pygame.display.set_mode(size)
    running = True
    pos = (0, 0)
    while running:
        screen.fill((255, 255, 255))
        screen.blit(image, pos)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                pos = list(pos)
                if event.key == pygame.K_LEFT:
                    pos[0] -= 10
                elif event.key == pygame.K_RIGHT:
                    pos[0] += 10
                elif event.key == pygame.K_UP:
                    pos[1] -= 10
                elif event.key == pygame.K_DOWN:
                    pos[1] += 10
                pos = tuple(pos)

        pygame.display.flip()
    pygame.quit()
