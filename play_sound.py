import time
import pygame

def play_sound():
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound("result.wav")
    # Query length of the response so that the computer can play it
    rest_time = "length", sounda.get_length()
    rt = round(rest_time[1])
    sounda.play()
    time.sleep(rt)

    return

