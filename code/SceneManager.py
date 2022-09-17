from Scene import Scene
from gameOver import gameOver
from gameWin import gameWin
    
    
PLAY_SCENE = 0
GAME_OVER_SCENE = 1
GAME_WIN_SCENE = 2
class SceneManager:
    def __init__(self, camera) -> None:
        self.currentState = Scene(camera)
        self.camera = camera
        self.state = PLAY_SCENE
        
        
    def update(self, delta):
        change = self.currentState.update(delta, self.camera)
        
        if change and self.state == PLAY_SCENE:
            self.currentState = gameOver(self.camera)
            self.state = GAME_OVER_SCENE
        
    def render(self, display):
        self.currentState.render(display, self.camera)
        
    def input(self, event):
        change = self.currentState.input(event, self.camera)
        if change and self.state == PLAY_SCENE:
            self.currentState = gameWin(self.camera)
            self.state = GAME_WIN_SCENE
        
    