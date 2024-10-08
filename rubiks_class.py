import sys
import random
import datetime
import time
import select
from datetime import datetime
from datetime import date


class RubiksCube():
    def __init__(
        self,
        size=3,
        core_magnets=False,
        magnet_strengh=1,
        interior="Spring",
        adjusting_mechanism="screw"):

        self.size = size
        self.core_magnets = core_magnets
        self.magnet_strengh = magnet_strengh
        self.interior = interior
        self.adjusting_mechanism = adjusting_mechanism
        self.cube = []
        self.create_cube()
        self.choose_function()


    def create_cube(self):
        colors = [r"⬜","🟩","🟥","🟦","🟧","🟨"]
        for i in range(6):
            self.cube.append([])
        for list in self.cube:
            for i in range(self.size * self.size):
                list.append(colors[self.cube.index(list)])

    def choose_function(self):
        moves = sys.argv
        try:
            moves.pop(0)
        except IndexError:
            ...
        if moves == ["scramble"]:
            scrambled = self.scramble()
            new_moves = self.replace_moves(scrambled)
            self.do_moves(new_moves)
            print(f"\nSCRAMBLE --> {" ".join(scrambled).replace("p","\'")}")
            if __name__ == "__main__":
                self.print_cube()
            self.inspection()
            self.timer(scrambled)
        elif "".join(moves).isalnum():
            new_moves = self.replace_moves(moves)
            self.do_moves(new_moves)
            if __name__ == "__main__":
                self.print_cube()

    def scramble(self):
        move_list = [["R","Rp","R2"],["L","Lp","L2"],["U","Up","U2"],["D","Dp","D2"],["F","Fp","F2"],["B","Bp","B2"]]
        moves = []
        i = random.randint(0,5)
        old_num = i
        for _ in range(20):
            new_num = random.randint(0,5)
            while new_num == i or new_num == old_num:
                new_num = random.randint(0,5)
            old_num = i
            i = new_num
            moves.append(random.choice(move_list[i]))
        return moves

    def replace_moves(self,moves):
        new_moves = []
        for move in moves:
            if len(move) == 1:
                new_moves.append(move)
            elif move.find("2") == -1:
                new_moves.append(move[0])
                new_moves.append(move[0])
                new_moves.append(move[0])
            elif move.find("2") != -1:
                new_moves.append(move[0])
                new_moves.append(move[0])
        return new_moves

    def u_move(self):
        slicer = slice(3)
        holder = self.cube[1][slicer].copy()
        self.cube[1][0:3] = self.cube[2][0:3]
        self.cube[2][0:3] = self.cube[3][0:3]
        self.cube[3][0:3] = self.cube[4][0:3]        
        self.cube[4][0:3] = holder
        self.cube[0] = self.side_rotater(self.cube[0])

    def d_move(self):
        slicer = slice(6,9)
        holder = self.cube[1][slicer].copy()
        self.cube[1][6:9] = self.cube[4][6:9]
        self.cube[4][6:9] = self.cube[3][6:9]
        self.cube[3][6:9] = self.cube[2][6:9]        
        self.cube[2][6:9] = holder
        self.cube[5] = self.side_rotater(self.cube[5])

    def r_move(self):
        holder = self.cube[0].copy()
        self.cube[0] = self.helper(self.cube[0],self.cube[1],2,5,8,2,5,8)
        self.cube[1] = self.helper(self.cube[1],self.cube[5],2,5,8,2,5,8)
        self.cube[5] = self.helper(self.cube[5],self.cube[3],2,5,8,6,3,0)  
        self.cube[3] = self.helper(self.cube[3],holder,0,3,6,8,5,2)
        self.cube[2] = self.side_rotater(self.cube[2])

    def l_move(self):
        holder = self.cube[0].copy()
        self.cube[0] = self.helper(self.cube[0],self.cube[3],0,3,6,8,5,2)        
        self.cube[3] = self.helper(self.cube[3],self.cube[5],2,5,8,6,3,0)
        self.cube[5] = self.helper(self.cube[5],self.cube[1],0,3,6,0,3,6)
        self.cube[1] = self.helper(self.cube[1],holder,0,3,6,0,3,6)
        self.cube[4] = self.side_rotater(self.cube[4])

    def f_move(self):
        holder = self.cube[0].copy()
        self.cube[0] = self.helper(self.cube[0],self.cube[4],6,7,8,8,5,2)        
        self.cube[4] = self.helper(self.cube[4],self.cube[5],2,5,8,0,1,2)
        self.cube[5] = self.helper(self.cube[5],self.cube[2],0,1,2,6,3,0)
        self.cube[2] = self.helper(self.cube[2],holder,0,3,6,6,7,8)
        self.cube[1] = self.side_rotater(self.cube[1])

    def b_move(self):
        holder = self.cube[0].copy()
        self.cube[0] = self.helper(self.cube[0],self.cube[2],0,1,2,2,5,8)
        self.cube[2] = self.helper(self.cube[2],self.cube[5],2,5,8,8,7,6)
        self.cube[5] = self.helper(self.cube[5],self.cube[4],6,7,8,0,3,6)
        self.cube[4] = self.helper(self.cube[4],holder,0,3,6,2,1,0)
        self.cube[3] = self.side_rotater(self.cube[3])

    def helper(self,first,second,piece_aa,piece_ab,piece_ac,piece_ba,piece_bb,piece_bc):
        first[piece_aa] = second[piece_ba]
        first[piece_ab] = second[piece_bb]
        first[piece_ac] = second[piece_bc]
        return first

    def side_rotater(self,premove):
        postmove = [premove[6],premove[3],premove[0],premove[7],premove[4],premove[1],premove[8],premove[5],premove[2]]
        return postmove

    def do_moves(self,moves):
        for move in moves:
            move = move.lower()
            if move == "r":
                self.r_move()
            elif move == "l":
                self.l_move()
            elif move == "u":
                self.u_move()
            elif move == "d":
                self.d_move()
            elif move == "f":
                self.f_move()
            elif move == "b":
                self.b_move()

    def print_cube(self):
        top = slice(3)
        middle = slice(3,6)
        bottom = slice(6,9)
        
        layout = f"""
                    {"".join(self.cube[0][top])}
                    {"".join(self.cube[0][middle])}
                    {"".join(self.cube[0][bottom])}

            {"".join(self.cube[4][top])}  {"".join(self.cube[1][top])}  {"".join(self.cube[2][top])}  {"".join(self.cube[3][top])}
            {"".join(self.cube[4][middle])}  {"".join(self.cube[1][middle])}  {"".join(self.cube[2][middle])}  {"".join(self.cube[3][middle])}
            {"".join(self.cube[4][bottom])}  {"".join(self.cube[1][bottom])}  {"".join(self.cube[2][bottom])}  {"".join(self.cube[3][bottom])}

                    {"".join(self.cube[5][top])}
                    {"".join(self.cube[5][middle])}
                    {"".join(self.cube[5][bottom])}
        
        """

        print(layout)

    def inspection(self):
        start = input("\nPress enter to start inspection timer.")
        print("")
        number = 0
        while True:
            if number <= 15:
                print(f"\r{number}", end="")
            elif number <= 17:
                print(f"\r+{number-15}", end="")
            else:
                print(f"\r+{number-15} (DNF)", end="")
            time.sleep(1)
            number += 1
            if self.check_for_input():
                input()
                break

    def check_for_input(self):
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])
    
    def timer(self,scrambled):
        tic = datetime.now()
        print(f"\nPress enter to finish:\n")

        seconds = 0
        while True:
            print(f"\r{round(seconds,3)}", end="")
            time.sleep(0.1)
            seconds += 0.1
            if self.check_for_input():
                toc = datetime.now()
                break

        duration = toc - tic

        minutes = int(duration.total_seconds() // 60)
        seconds = str(duration.seconds).zfill(2)
        microseconds = round(duration.microseconds / 1000)

        what_to_print = f"{int(minutes)}:{seconds}.{microseconds}"

        print(f"\r{what_to_print}")

        with open("Rubiks_times.csv", "a") as file:
            file.write(f"{what_to_print}   ---   {date.today()} ---   {' '.join(scrambled).replace("p","\'")}\n")

        


if __name__ == '__main__':
    DayanYuhongPro = RubiksCube()