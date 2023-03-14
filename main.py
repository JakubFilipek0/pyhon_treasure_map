import random

row1 = ["💩", "💩", "💩"]
row2 = ["💩", "💩", "💩"]
row3 = ["💩", "💩", "💩"]
treasure_map = [row1, row2, row3]
#print(f"{row1}\n{row2}\n{row3}")
[print(a) for a in treasure_map]
position = input("Where do you want to put the treasure (eg. 12, 1 for column and 2 for line): ")
#💰
treasure_map[int(position[1]) - 1][int(position[0]) - 1] = "💰"
[print(a) for a in treasure_map]

