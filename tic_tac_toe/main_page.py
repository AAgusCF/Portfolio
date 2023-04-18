from tkinter import *
from tkinter import messagebox
from connection import Connect

class Game():

    def __init__(self, p1, p2):

        self.connection = Connect(p1+"(P1)", p2+"(P2)")

        self.page = Tk()
        self.page.resizable(0, 0)
        self.page.geometry("520x520+800+300")
        self.page.config(background='white')
        self.page.title("Tic Tac Toe Game")
        self.frame=Frame(self.page, width=400, height=400)
        self.frame.config(bg="black", bd=5, cursor="hand2")
        self.frame.pack(expand=1)

        self.break_flag, self.answer = False, False
        self.row, self.col, self.i, self.p = 3, 3, 0, 0
        self.x, self.o = [0]*8, [0]*8
        self.winner, self.player1, self.player2 = "", p1, p2

        self.button1 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button1,0,0))
        self.button2 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button2,0,1))
        self.button3 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button3,0,2))
        self.button4 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button4,1,0))
        self.button5 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button5,1,1))
        self.button6 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button6,1,2))
        self.button7 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button7,2,0))
        self.button8 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button8,2,1))
        self.button9 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button9,2,2))

        self.restart_button = Button(self.page, text="Restart game", font=("Arial", 8, "bold"), bg="deep sky blue", height=1, width=10, command= lambda: self.restart_game())

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)

        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)

        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)

        self.restart_button.place(x=220, y=485)

        self.page.mainloop()



    def button_click(self, b: Button, r: int, c: int) -> None:

        
        if b['text'] == " " and self.i % 2 == 0:
            b.config(fg="red", disabledforeground="red")
            b['text'] = "X"
            self.row, self.col = r, c

        elif b['text'] == " " and self.i % 2 != 0:
            b.config(fg="blue", disabledforeground="blue")
            b['text'] = "O"
            self.row, self.col = r, c
            
        else:
            messagebox.showerror("Tic Tac Toe", "This is not an empty space\nPick another space.")
            self.row, self.col = 3, 3
            self.i -= 1

        self.answer = self.player_vs_player([self.row, self.col], self.x, self.o, self.i)
        self.i += 1
        self.winner, self.break_flag, self.p = self.select_winner(self.x, self.o)

        if self.winner != "":
            self.disable_buttons()
            messagebox.showinfo("Tic Tac Toe", "Player "+self.winner+" won")
            self.connection.update_score(self.p)

        if self.i == 9 and not self.break_flag:
            self.winner = "Draw"
            self.disable_buttons()
            messagebox.showinfo("Tic Tac Toe", "Draw")

            


    def restart_game(self) -> None:

        self.break_flag, self.answer = False, False
        self.row, self.col, self.i = 3, 3, 0
        self.x, self.o = [0]*8, [0]*8
        self.winner = ""

        self.button1 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button1,0,0))
        self.button2 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button2,0,1))
        self.button3 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button3,0,2))
        self.button4 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button4,1,0))
        self.button5 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button5,1,1))
        self.button6 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button6,1,2))
        self.button7 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button7,2,0))
        self.button8 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button8,2,1))
        self.button9 = Button(self.frame, text=" ", font=("Arial", 24, "bold"), bg="grey85", height=3, width=6, command= lambda: self.button_click(self.button9,2,2))

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)

        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)

        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)




    def disable_buttons(self) -> None:
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)
        self.button3.config(state=DISABLED)
        self.button4.config(state=DISABLED)
        self.button5.config(state=DISABLED)
        self.button6.config(state=DISABLED)
        self.button7.config(state=DISABLED)
        self.button8.config(state=DISABLED)
        self.button9.config(state=DISABLED)




    def player_vs_player(self, pos: list[int], x: list[int], o: list[int], i: int) -> bool:

        try:
                
            if 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2:
                if i % 2 == 0:
                    current = x
                else:
                    current = o
            else:
                raise IndexError()

            
        except (AttributeError, IndexError):

            return False

        else:
            current[pos[0]] += 1
            current[pos[1]+3] += 1

            if pos[0] == pos[1]:
                current[-2] += 1
            if pos[0] == 2 - pos[1]:
                current[-1] += 1

            return True



    def select_winner(self, x: list[int], o: list[int]) -> list[str, bool, int]:

        for n in range(len(x)):
            if x[n] == 3:
                winner = self.player1
                break_flag = True
                return [winner, break_flag, 1]
            elif o[n] == 3:
                winner = self.player2
                break_flag = True
                return [winner, break_flag, 2]
            
        return ["", False, 0]