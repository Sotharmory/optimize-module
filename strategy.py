from utils import Shortener, Preserver, DetailAdder
from models import OptimizedPropmpt

class PromptStrategy:
    def __init__(self, model, contents):
        self.model = model
        self.contents = contents

    def optimize(self):
        shortened = Shortener(self.contents, 50)
        Preserver()
        DetailAdder()
        return OptimizedPropmpt(
            self.contents, 
            shortened, 
            len(self.contents.split()) - len(shortened.split()),
            ["important", "key", "critical"],
            ["efficient", "effective"]
        )
