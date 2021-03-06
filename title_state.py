import game_framework
import lobby
from pico2d import *



name = "TitleState"
image = None
time = False

def enter():
    global image
    image = load_image('Image\\title.png')

def exit():
    global image
    del(image)


def handle_events():
    global time
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                #time = True
                game_framework.change_state(lobby)


def draw():
    clear_canvas()
    image.draw(400, 400)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass






