origional = """

    self.cube[1][6:9] = self.cube[2][0:3]
    self.cube[2][0:3] = self.cube[3][0:3]
    self.cube[3][0:3] = self.cube[4][0:3]        
    self.cube[4][0:3]
    
"""

change_from = input("Change from --> ")
change_to = input("Change to --> ")

print(origional.replace(change_from,change_to))