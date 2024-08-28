origional = """



"""

change_from = input("Change from --> ")
change_to = input("Change to --> ")

i = 0
while i < len(change_from):
    print(origional.replace(change_from[i],change_to[i]))
    i += 1