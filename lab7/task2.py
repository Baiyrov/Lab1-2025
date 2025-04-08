import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

# Плейлист и соответствующие обложки
playlist = ["lab7/song1 (2).mp3", "lab7/song2.mp3", "lab7/song3.mp3"]
covers = ["lab7/красиввая.jpg", "lab7/moc.jpg", "lab7/medium_Eminem-Superman.jpg"]
current_track = 0

def play_music():
    print(f"Playing: {playlist[current_track]}")
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def stop_music():
    print("Music Stopped")
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    play_music()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    play_music()

def draw_cover():
    cover = pygame.image.load(covers[current_track])
    cover = pygame.transform.scale(cover, (400, 300))  # Подгоняем размер
    screen.blit(cover, (0, 0))

running = True
while running:
    screen.fill((0, 0, 0))  # Очистка экрана
    draw_cover()  # Отображение текущей обложки

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print("P Key Pressed - Play Music")
                play_music()
            elif event.key == pygame.K_s:
                print("S Key Pressed - Stop Music")
                stop_music()
            elif event.key == pygame.K_n:
                print("N Key Pressed - Next Track")
                next_track()
            elif event.key == pygame.K_b:
                print("B Key Pressed - Previous Track")
                prev_track()
    
    pygame.display.update()

pygame.quit()
