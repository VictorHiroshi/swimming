from Environment import Environment
setup_params={
    "screen_width": 512,
    "screen_height": 512,
    "rendering": True        
}
environment = Environment(background_color={"r":32, "g":64, "b":128}, setup=setup_params)

def setup():
    size(setup_params["screen_width"], setup_params["screen_height"], P2D)

def draw():
    environment.update()
    
