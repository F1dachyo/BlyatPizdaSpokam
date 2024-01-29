from params import letters, size, width, height
from def_and_class import Keyboard, Enemy, str_key, change_score, change_money, load_image, generate

from pynput.keyboard import Listener
import pygame
import os
import sys
import random
import sqlite3

con = sqlite3.connect('data/game.sqlite3')
cur = con.cursor()

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
pygame.init()
screen.fill(pygame.Color("white"))
font = pygame.font.Font(None, 20)

tup = 2
all_sprites.add(generate(50, tup))
keyboard = Keyboard()
data = []
activ = True
act_word = ""


def x(q):
    global activ, act_word
    activ = True
    act_word = q
    print(q)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            con.commit()
            con.close()
    if pygame.mouse.get_focused():
        all_sprites.update(pygame.mouse.get_pos(), act_word)
        screen.fill(pygame.Color("white"))
    """if act_word == 'q':
        for i in all_sprites.sprites():
            i.kill()"""
    if activ:
        activ = False
        all_sprites.update(pygame.mouse.get_pos(), act_word)
        act_word = ""
        data = []
        for i in all_sprites.sprites():
            data.append((i.name, i.distance, x))
        keyboard.set_active_words(data)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
