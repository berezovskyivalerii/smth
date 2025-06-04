import tkinter as tk
import random

ROWS, COL = 20, 10
CELL = 30
DELAY = 500

COLORS = ["cyan", 'blue', "red", "green", "pink", "yellow", "purple"]

SHAPES = {
    "I": [[(0, -1), (0, 0), (0, 1), (0, 2)]],
    "J": [[(0, -1), (0, 0), (0, 1), (-1, 1)]],
    "L": [[(0, -1), (0, 0), (0, 1), (1, 1)]],
    "O": [[(0, 0), (1, 0), (0, 1), (1, 1)]],
    "S": [[(0, 0), (1, 0), (0, 1), (-1, 1)]],
    "Z": [[(0, 0), (-1, 0), (0, 1), (1, 1)]],
    "T": [[(0, -1), (0, 0), (0, 1), (0, 2)]],
}

class Tetris:
    def __init__(self, root):
        self.root = root
        self.root.title("tetris")
        self.score = 0
        self.canvas = tk.Canvas(root, width=(COL+6) * CELL, height=ROWS*CELL, bg="black")
        self.canvas.pack()
        self.board = [[None for _ in range(COL)] for _ in range(ROWS)]
        self.game_over = False
        self.current_shape = self.new_shape()
        self.next_shape = self.new_shape()
        self.root.bind("<Key>", self.key_press)
        self.draw()
        
    def new_shape(self):
        pass
    
    def draw_block(self):
        pass
    
    def draw(self):
        pass
    
    def move(self):
        pass
    
    def rotate(self):
        pass
    
    def valud_position(self):
        pass
    
    def freeze(self):
        pass
    
    def key_press(self, event):
        pass
    
    def draw(self):
        pass
    
    def clean_line(self):
        pass
    

if __name__ == "__main__":
    root = tk.Tk()
    tetr = Tetris(root)
    root.mainloop()