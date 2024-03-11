# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#Manu Berea
import numpy as numpy


class Game:
    player1 = {}
    player2 = {}
    moves = []
    moves2=[]
    n=0
    m=0
    def __init__(self, path):
        self.read_file(path)
        print(self.player1)
        print(self.player2)
        print(self.moves2)
        print(self.n)
        print(self.m)

    def read_file(self, path):
        file = open(path, 'r')

        line1 = file.readline().split()
        self.player1['Name'] = line1[0]
        moves_list = []
        for i in range(1, len(line1)):
            moves_list.append(line1[i])
        self.player1['Moves'] = moves_list

        self.n=len(moves_list)

        line2 = file.readline().split()
        self.player2['Name'] = line2[0]
        moves_list2 = []
        for i in range(1, len(line2)):
            moves_list2.append(line2[i])
        self.player2['Moves'] = moves_list2

        self.m=len(moves_list2)
        line = file.readline()

        while line != '':
            line_split = line.split()
            for i in range(len(line_split)):
                parsed = line_split[i].split('/')
                self.moves.append((int(parsed[0]), int(parsed[1])))
            line = file.readline()

        self.moves2 = self.moves
        # matrix=numpy.random.randint(1, size=(n, m))
        matrix=numpy.zeros((self.n,self.m),dtype='i,i')
        for i in range(self.n):
            for j in range(self.m):
                matrix[i][j]=self.moves.pop();
                print(matrix[i][j], end='   ')

            print()

        # strategis A
        tuplaA=[]
        tupl1=0
        tupl2=0
        for i in range(self.n):
            maxA=0
            for j in range(self.m):
                if maxA < matrix[i][j][0]:
                    tupl1=i
                    tupl2=j
        tuplaA.append(tuple[tupl1,tupl2])

        print(tuplaA)

        #strategis B
        tuplaB = []
        tupl1 = 0
        tupl2 = 0
        for i in range(self.m):
            maxB = 0
            for j in range(self.n):
                if maxB < matrix[j][i][0]:
                    tupl1 = j
                    tupl2 = i
        tuplaB.append(tuple[tupl1, tupl2])
        print(tuplaB)

        # strategie comuna dominanta
        i=0
        exist=0
        while len(tuplaA)>i and len(tuplaB)>i:
            if tuplaA[i]==tuplaB[i]:
                exist=1
                tuplaDomn=tuplaB
            i+=1

        print(tuplaDomn[0])
        if exist>0:
            print("Exista o stategie dominanta")
            if (tuplaDomn[0]==1):
                print("up")
            else:
                print("Down")
            if tuplaDomn[0]==1:
                print("left")
            else:
                print("right")




if __name__ == "__main__":
    game = Game("game.txt")