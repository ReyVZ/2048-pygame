import pygame
from pygame.locals import *
import random
import sys

WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((512, 512))
pygame.display.set_caption('2048')

ie = pygame.image.load('empty.png')
i2 = pygame.image.load('2.png')
i4 = pygame.image.load('4.png')
i8 = pygame.image.load('8.png')
i16 = pygame.image.load('16.png')
i32 = pygame.image.load('32.png')
i64 = pygame.image.load('64.png')
i128 = pygame.image.load('128.png')
i256 = pygame.image.load('256.png')
i512 = pygame.image.load('512.png')
i1024 = pygame.image.load('1024.png')
i2048 = pygame.image.load('2048.png')

link = {
    0: ie,
    2: i2,
    4: i4,
    8: i8,
    16: i16,
    32: i32,
    64: i64,
    128: i128,
    256: i256,
    512: i512,
    1024: i1024,
    2048: i2048
}

arr = []
for i in range(4):
    arr.append([0, 0, 0, 0])

def fill():
    if 0 not in (arr[0] + arr[1] + arr[2] + arr[3]):
        return
    while True:
        x = random.randrange(0, 4)
        y = random.randrange(0, 4)
        n = random.choice([2, 4])
        if arr[x][y] == 0:
            break
    arr[x][y] = n

def shake(a):
    zeroes = a.count(0)
    for i in range(zeroes):
        a.remove(0)
        a.append(0)
    if a[0] == a[1]:
        a[0] += a[1]
        a[1] = a[2]
        a[2] = a[3]
        a[3] = 0
    if a[1] == a[2]:
        a[1] += a[2]
        a[2] = a[3]
        a[3] = 0
    if a[2] == a[3]:
        a[2] += a[3]
        a[3] = 0
    return a

def cross():
    global arr
    t = arr
    temp = list(zip(t[0], t[1], t[2], t[3]))
    for i in range(4):
        temp[i] = list(temp[i])
    arr = temp

fill()
fill()

def left():
    for a in arr:
        a = shake(a)
    fill()
 
def right():
    for a in arr:
        a.reverse()
        a = shake(a)
        a.reverse()
    fill()

def up():
    cross()
    for a in arr:
        a = shake(a)
    cross()
    fill()

def down():
    cross()
    for a in arr:
        a.reverse()
        a = shake(a)
        a.reverse()
    cross()
    fill()


def main():
    while True:
        screen.fill(WHITE)
        for i in range(4):
            for j in range(4):
                num = arr[i][j]
                screen.blit(link[num], (j * 128, i * 128))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    up()
                if event.key == K_DOWN:
                    down()
                if event.key == K_LEFT:
                    left()
                if event.key == K_RIGHT:
                    right()

        pygame.display.update()

if __name__ == '__main__':
    main()
