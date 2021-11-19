
def Hanoi(nbDisque, plotStart, plotEnd, plotMid, action):
    action[0] += 1
    if nbDisque != 0:
        Hanoi(nbDisque-1, plotStart, plotMid, plotEnd, action)
        print("action",action[0],":","Déplacer le disque de" , plotStart , "vers" , plotEnd)
        Hanoi(nbDisque-1, plotMid, plotEnd, plotStart, action)

nbAction = [0]
Hanoi(3, 1, 3, 2, nbAction)