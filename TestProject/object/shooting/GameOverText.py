from pygameEasy.GameObject import TextObject

class GameOverText(TextObject):
    def set_data(self, data) -> None:
        super().set_data(data)
        
        self.visible = False
        
    def update(self):
        return super().update()