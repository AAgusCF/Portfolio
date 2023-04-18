import mysql.connector as con
from tabulate import tabulate
import constants

class Connect:

    def __init__(self, p1, p2):

        self.db = con.connect(
                                user=constants.USER,
                                password=constants.PASSWORD,
                                host=constants.HOST,
                                database=constants.DB,
                                port=constants.PORT
                            )

        self.mycursor = self.db.cursor()

        self.mycursor.execute("INSERT INTO score () Values ()")

        self.foreign_key = self.mycursor.lastrowid

        self.player1, self.player2 = p1, p2

        self.add_players()

        self.db.commit()

    def add_players(self):

        self.mycursor.execute("INSERT INTO player (player_name, match_id) VALUES (%s,%s)", (self.player1, self.foreign_key))
        self.mycursor.execute("INSERT INTO player (player_name, match_id) VALUES (%s,%s)", (self.player2, self.foreign_key))


    def update_score(self, winner):

        if winner == 1:
            self.mycursor.execute(f"UPDATE score SET won_p1 = won_p1 + {1} WHERE match_id = {self.foreign_key}")
            self.mycursor.execute(f"UPDATE score SET lost_p2 = lost_p2 + {1} WHERE match_id = {self.foreign_key}")
        elif winner == 2:
            self.mycursor.execute(f"UPDATE score SET won_p2 = won_p2 + {1} WHERE match_id = {self.foreign_key}")
            self.mycursor.execute(f"UPDATE score SET lost_p1 = lost_p1 + {1} WHERE match_id = {self.foreign_key}")

        self.print_score()
        self.db.commit()

    def print_score(self):
        self.mycursor.execute(f"SELECT won_p1, lost_p1, won_p2, lost_p2 FROM score WHERE match_id = {self.foreign_key}")

        print(tabulate(self.mycursor, headers=[self.player1+' won',self.player1+' lost',self.player2+' won',self.player2+' lost'], tablefmt='fancy_grid'))
        #for bd in self.mycursor:
        #    print(bd)