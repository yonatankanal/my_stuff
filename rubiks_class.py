class Rubiks_Cube:
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



    def create_cube(self):
        colors = ["w","g","r","b","o","y"]
        for i in range(6):
            self.cube.append([])
        for list in self.cube:
            for i in range(self.size * self.size):
                list.append(colors[self.cube.index(list)])


    def u_move(self):
        slicer = slice(3)
        holder = self.cube[1][slicer]
        self.cube[1][0:3] = self.cube[2][0:3]
        self.cube[2][0:3] = self.cube[3][0:3]
        self.cube[3][0:3] = self.cube[4][0:3]        
        self.cube[4][0:3] = holder

    def d_move(self):
        slicer = slice(6,9)
        holder = self.cube[1][slicer]
        self.cube[1][6:9] = self.cube[4][6:9]
        self.cube[4][6:9] = self.cube[3][6:9]
        self.cube[3][6:9] = self.cube[2][6:9]        
        self.cube[2][6:9] = holder

    def r_move(self):
        holder = self.cube[0]
        self.cube[0] = self.helper(self.cube[0],self.cube[1],2,5,8,2,5,8)
        self.cube[1] = self.helper(self.cube[1],self.cube[5],2,5,8,2,5,8)
        self.cube[5] = self.helper(self.cube[5],self.cube[3],2,5,8,2,5,8)        
        self.cube[3] = self.helper(self.cube[3],holder,0,3,6,8,5,2)

    def l_move(self):
        holder = self.cube[0]
        self.cube[0] = self.helper(self.cube[0],self.cube[3],0,3,6,2,5,8)        
        self.cube[3] = self.helper(self.cube[3],self.cube[5],2,5,8,0,3,6)
        self.cube[5] = self.helper(self.cube[5],self.cube[1],0,3,6,2,5,8)
        self.cube[1] = self.helper(self.cube[1],holder,0,3,6,0,3,6)

    def f_move(self):
        holder = self.cube[0]
        self.cube[0] = self.helper(self.cube[0],self.cube[4],6,7,8,8,5,2)        
        self.cube[3] = self.helper(self.cube[3],self.cube[5],2,5,8,0,3,6)
        self.cube[5] = self.helper(self.cube[5],self.cube[1],0,3,6,2,5,8)
        self.cube[1] = self.helper(self.cube[1],holder,0,3,6,0,3,6)

    def b_move(self):
        ...

    def helper(self,first,second,piece_aa,piece_ab,piece_ac,piece_ba,piece_bb,piece_bc):
            first[piece_aa] = second[piece_ba]
            first[piece_ab] = second[piece_bb]
            first[piece_ac] = second[piece_bc]
            return first



Dayan_Yuhong_Pro =  Rubiks_Cube(3, True, 2, "Maglev", "Hand")

print(Dayan_Yuhong_Pro.cube)