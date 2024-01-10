def TowersOfHanoi(n, A, B, C):
    nmoves = 0
    if n> 0:
        nmoves += TowersOfHanoi(n-1, A, C, B)
        print("Move from", A, "To", C)
        nmoves += TowersOfHanoi(n-1, B, A, C)
        nmoves +=1
    return nmoves
n = int(input("Numbers of Disks:"))
print("Numbers of moves:",TowersOfHanoi(n, "A", "B", "C"))
        
