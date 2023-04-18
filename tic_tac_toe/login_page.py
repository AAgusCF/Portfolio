from tkinter import *
from main_page import Game

class Login():

    def __init__(self):
        
        self.login = Tk()
        self.login.resizable(0, 0)
        self.login.geometry("520x520+800+300")
        self.login.config(background='white')
        self.login.title("Tic Tac Toe Game")
        frame=Frame(self.login, width=400, height=400, highlightbackground="black", highlightthickness=6, highlightcolor="black")
        frame.config(bd=20)
        frame.pack(expand=1)

        self.title = Label(frame, text="Tic Tac Toe Game", font=("Arial", 24, "bold"), fg='deep sky blue')
        self.title.place(x=35, y=20)
        self.player1 = Label(frame, text="Player 1", font=("Arial", 12, "bold"), fg='black')
        self.player1.place(x=100, y=140)

        self.p1 = Entry(frame, font=("Arial", 12, "bold"), bd=1, width=10)
        self.p1.place(x=170 , y=140)

        self.player2 = Label(frame, text="Player 2", font=("Arial", 12, "bold"), fg='black')
        self.player2.place(x=100, y=200)

        self.p2 = Entry(frame, font=("Arial", 12, "bold"), bd=1, width=10)
        self.p2.place(x=170 , y=200)


        self.start_button = Button(frame, text="Start game", font=("Arial", 14, "bold"), bg="red", fg="white", height=1, width=10, activebackground="red", activeforeground="white", border=0)
        self.start_button.place(x=125, y=280)
        self.start_button.bind('<Button>', self.start_game)

        self.login.mainloop()


    def start_game(self, event):
        player1 = str(self.p1.get())
        player2 = str(self.p2.get())
        self.login.destroy()
        #obj = Connect(self.player1, self.player2)
        Game(player1, player2)
        
        


    
if __name__ == "__main__":
    obj1 = Login()