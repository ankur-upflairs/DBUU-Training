import tkinter as tk
from PIL import Image,ImageTk
from random import randint
MOVE_INCREMENT=20
class Canvas(tk.Canvas):
    
    def __init__(self):
        super().__init__(width=600,height=620 , background='black',highlightthickness=0)
        
        self.score=0
        self.snake_positions=[(100,100),(80,100),(60,100)]
        self.food_position=(200,100)
        self.direction = 'Right'
        self.bind_all('<Key>',self.on_key_press)
        self.load_assests()
        self.perform_actions()
    def load_assests(self):
        self.create_text(50,14,text=f'Score {self.score}',fill='white',font=('TkDefaultFont',16),tags='score')
        self.create_rectangle(7,23,593,613 , outline='lightyellow')
        self.load_snake_image=Image.open('snake.jpeg')
        self.snake_image= ImageTk.PhotoImage(self.load_snake_image)
        for x_position,y_position in self.snake_positions:
            self.create_image(x_position,y_position,image=self.snake_image,tags='snake')
        self.load_food_image=Image.open('food.jpeg')
        self.food_image =ImageTk.PhotoImage(self.load_food_image)
        self.create_image(*self.food_position,image=self.food_image,tags='food')
        
    def move_snake(self):
        head_x_position,head_y_position = self.snake_positions[0]
        if self.direction=='Right':
            new_head_position=[(head_x_position +MOVE_INCREMENT,head_y_position)]
        elif self.direction=='Left':
            new_head_position=[(head_x_position -MOVE_INCREMENT,head_y_position)]
        elif self.direction=='Up':
            new_head_position=[(head_x_position,head_y_position-MOVE_INCREMENT)]
        elif self.direction=='Down':
            new_head_position=[(head_x_position ,head_y_position+MOVE_INCREMENT)]
            
        self.snake_positions=new_head_position + self.snake_positions[:-1]
        for snakeId,position in zip(self.find_withtag('snake'),self.snake_positions):
            self.coords(snakeId,*position)
            
    def check_collision(self):
        x,y=self.snake_positions[0]
        return x in (0,600) or y in (20,620) or (x,y) in self.snake_positions[1:]
    
    def check_food_collision(self):
        if self.snake_positions[0] == self.food_position :
            self.score+=1
            self.food_position = self.change_food_position()
            self.coords('food',*self.food_position)
            self.snake_positions.append(self.snake_positions[-1])
            self.create_image(self.snake_positions[-1][0],self.snake_positions[-1][1],image=self.snake_image,tags='snake')
            score=self.find_withtag('score')
            self.itemconfig(score,text=f"Score {self.score}",tags='score')
            
    def change_food_position(self):
        while True:
            x=randint(1,29) * 20
            y=randint(3,29) * 20
            if (x,y) not in self.snake_positions:
                return (x,y)
        
        
    def perform_actions(self):
        if self.check_collision():
            self.end_game()
            return
        self.check_food_collision()
        self.move_snake()
        self.after(100,self.perform_actions)
        
    def on_key_press(self,e):
        all_directions = ('Right',"Left","Up","Down")
        oposite=({"Right","Left"},{"Up","Down"})
        key_pressed=e.keysym
        if key_pressed in all_directions and {key_pressed,self.direction} not in oposite:
            self.direction=key_pressed
        # print(key_pressed)
    def end_game(self):
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width()/2,
            self.winfo_height() /2,
            text=f"Game End: Your Score is {self.score}",
            font=('TkDefaultfont',24),
            fill='white'
        )
        
root=tk.Tk()
root.resizable(False,False)
board = Canvas()
board.pack()
root.mainloop()