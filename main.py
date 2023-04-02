
import pygame
import matplotlib.pyplot as plt
import numpy as np


# #KRZYWE BEZIERA
#
# def draw_bezier_curve(x, y):
#     t = np.arange(0, 1, 0.0005)
#     curve_x = np.zeros_like(t)
#     curve_y = np.zeros_like(t)
#
#     n = len(x)
#
#     for i in range(n):
#         curve_x += x[i] * (1 - t) ** (n - i - 1) * t ** i * nchoosek(n - 1, i)
#         curve_y += y[i] * (1 - t) ** (n - i - 1) * t ** i * nchoosek(n - 1, i)
#
#     plt.plot(curve_x, curve_y, 'r')
#     plt.plot(x, y, 'yo')
#
#
# def nchoosek(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     else:
#         return nchoosek(n - 1, k - 1) * n // k
#
#
#
# ####P
# x = [10, 20, 20, 10]
# y = [40, 50, 60, 70]
# draw_bezier_curve(x, y)
#
# x = [10, 10]
# y = [10, 70]
# draw_bezier_curve(x, y)
#
# ####A
# x = [20, 30, 40, 50]
# y = [10, 90, 90, 10]
# draw_bezier_curve(x, y)
#
# x = [20, 50]
# y = [40, 40]
# draw_bezier_curve(x, y)
#
# plt.show()

####Caveman game

# pygame.init()
# screen = pygame.display.set_mode((800, 500))
# pygame.display.set_caption("Caveman Game")
# game_icon = pygame.image.load('images/cave.png').convert()
# pygame.display.set_icon(game_icon)
#
# sign = pygame.image.load('images/sign.png').convert_alpha()
#
# bg = pygame.image.load('images/bg.jpg').convert()
# bg = pygame.transform.scale(bg, (800, 500))
# bg_sound = pygame.mixer.Sound('sounds/cavesound.mp3')
# bg_sound.play()
#
# bg_sound.set_volume(0.1)
#
# walk_left = [pygame.image.load('images/caveman_left.png').convert_alpha()]
# walk_right = [pygame.image.load('images/caveman_right.png').convert_alpha()]
#
# player_anim_count = 0
#
# player_speed = 3
# player_x = 20
# player_y = 390
#
# monster = pygame.image.load('images/monster.png').convert_alpha()
# monster_list = []
#
# is_jump = False
# jump_hight = 2.7
#
# monster_timer = pygame.USEREVENT + 1
# pygame.time.set_timer(monster_timer, 1000)
#
# label = pygame.font.Font('font/font.otf', 60)
# lose = label.render('You lose', False, (193, 196, 199))
# restart = label.render('Try again', False, (115, 132, 148))
# restart_rect = restart.get_rect(topleft=(250, 220))
# lose_sound = pygame.mixer.Sound('sounds/lose.mp3')
# lose_sound_played = True
#
# label2 = pygame.font.Font('font/font2.ttf', 60)
# victory = label2.render('You win', False, (193, 196, 199))
# restart2 = label2.render('Play again', False, (115, 132, 148))
# restart2_rect = restart2.get_rect(topleft=(250, 220))
# victory_sound = pygame.mixer.Sound('sounds/win.mp3')
# win_sound_played = True
#
# spear = pygame.image.load('images/spear.png').convert_alpha()
# spears = []
# spear_left = 4
#
# clock = pygame.time.Clock()
#
# gameplay = True
#
# game = True
#
# while game:
#
#     screen.blit(bg, (0, 0))
#     screen.blit(sign, (700, 395))
#
#     if gameplay:
#
#         player_rect = walk_left[0].get_rect(topleft=(player_x, player_y))
#
#         if monster_list:
#             for (i, el) in enumerate(monster_list):
#                 screen.blit(monster, el)
#                 el.x -= 3
#
#                 if el.x < -10:
#                     monster_list.pop(i)
#
#                 if player_rect.colliderect(el):
#                     gameplay = False
#
#         keys = pygame.key.get_pressed()
#
#         if keys[pygame.K_LEFT]:
#             screen.blit(walk_left[player_anim_count], (player_x, player_y))
#         else:
#             screen.blit(walk_right[player_anim_count], (player_x, player_y))
#
#         if keys[pygame.K_LEFT] and player_x > 10:
#             player_x -= player_speed
#         elif keys[pygame.K_RIGHT] and player_x < 750:
#             player_x += player_speed
#
#         if not is_jump:
#             if keys[pygame.K_SPACE]:
#                 is_jump = True
#         if is_jump:
#             if jump_hight >= -2.7:
#                 if jump_hight > 0:
#                     player_y -= (jump_hight ** 2) / 2
#                 else:
#                     player_y += (jump_hight ** 2) / 2
#                 jump_hight -= 0.04
#             else:
#                 is_jump = False
#                 jump_hight = 2.7
#
#         if spears:
#             for (i, el) in enumerate(spears):
#                 screen.blit(spear, (el.x, el.y))
#                 el.x += 7
#
#                 if el.x > 799:
#                     spears.pop(i)
#
#                 if monster_list:
#                     for (index, monster_el) in enumerate(monster_list):
#                         if el.colliderect(monster_el):
#                             monster_list.pop(i)
#                             spears.pop(i)
#
#         if player_x >= 700:
#             gameplay = False
#
#     elif player_x >= 700:
#         screen.fill((87, 88, 89))
#         screen.blit(victory, (250, 150))
#         screen.blit(restart2, restart2_rect)
#         if win_sound_played:
#             victory_sound.play()
#             victory_sound.set_volume(0.4)
#             win_sound_played = False
#
#         mouse = pygame.mouse.get_pos()
#
#         if restart2_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
#             gameplay = True
#             is_jump = False
#             player_x = 20
#             player_y = 390
#             monster_list.clear()
#             spears.clear()
#             spear_left = 4
#             win_sound_played = True
#         pygame.display.update()
#
#
#
#     else:
#         screen.fill((87, 88, 89))
#         screen.blit(lose, (250, 150))
#         screen.blit(restart, restart_rect)
#         if lose_sound_played:
#             lose_sound.play()
#             lose_sound.set_volume(0.4)
#             lose_sound_played = False
#
#         mouse = pygame.mouse.get_pos()
#
#         if restart_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
#             gameplay = True
#             is_jump = False
#             player_x = 20
#             player_y = 390
#             monster_list.clear()
#             spears.clear()
#             spear_left = 4
#             lose_sound_played = True
#
#     pygame.display.update()
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game = False
#             pygame.quit()
#         if event.type == monster_timer:
#             monster_list.append(monster.get_rect(topleft=(790, 390)))
#         if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_j and spear_left > 0:
#             spears.append(spear.get_rect(topleft=(player_x + 5, player_y + 3)))
#             spear_left -= 1
#
#     clock.tick(100)
