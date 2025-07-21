

class Square:
    def __init__(self, id=-1, category=-1, hq=False, roll_again=False, center=False):
        self.id = id
        self.category = category
        self.hq = hq
        self.roll_again = False
        self.center = False
        self.neighbors = []

    def __repr__(self):
        return str(self.id)

    def moves(self, distance):
        visited = {self}
        q = [(self, 0)]
        ret = []
        while q:
            curr, x = q.pop(0)
            if x == distance:
                ret.append(curr)
            elif x < distance:
                for node in curr.neighbors:
                    if node not in visited:
                        visited.add(node)
                        q.append((node, x + 1))
        return ret
    
class Board:
    def __init__(self):
        squares = []
        # row 1
        squares.append(Square(id=0, roll_again=True))
        squares.append(Square(id=1, category=0))
        squares.append(Square(id=2, category=1))
        squares.append(Square(id=3, category=2))
        squares.append(Square(id=4, category=3, hq=True))
        squares.append(Square(id=5, category=0))
        squares.append(Square(id=6, category=1))
        squares.append(Square(id=7, category=2))
        squares.append(Square(id=8, roll_again=True))
        # row 2
        squares.append(Square(id=9, category=3))
        squares.append(Square(id=10, category=0))
        squares.append(Square(id=11, category=3))
        # row 3
        squares.append(Square(id=12, category=2))
        squares.append(Square(id=13, category=1))
        squares.append(Square(id=14, category=0))
        # row 4
        squares.append(Square(id=15, category=1))
        squares.append(Square(id=16, category=2))
        squares.append(Square(id=17, category=1))
        # row 5
        squares.append(Square(id=18, category=0, hq=True))
        squares.append(Square(id=19, category=1))
        squares.append(Square(id=20, category=2))
        squares.append(Square(id=21, category=3))
        squares.append(Square(id=22, center=True))
        squares.append(Square(id=23, category=1))
        squares.append(Square(id=24, category=0))
        squares.append(Square(id=25, category=3))
        squares.append(Square(id=26, category=2, hq=True))
        # row 6
        squares.append(Square(id=27, category=3))
        squares.append(Square(id=28, category=0))
        squares.append(Square(id=29, category=3))
        # row 7
        squares.append(Square(id=30, category=2))
        squares.append(Square(id=31, category=3))
        squares.append(Square(id=32, category=0))
        # row 8
        squares.append(Square(id=33, category=1))
        squares.append(Square(id=34, category=2))
        squares.append(Square(id=35, category=1))
        # row 9
        squares.append(Square(id=36, roll_again=True))
        squares.append(Square(id=37, category=0))
        squares.append(Square(id=38, category=3))
        squares.append(Square(id=39, category=2))
        squares.append(Square(id=40, category=1, hq=True))
        squares.append(Square(id=41, category=0))
        squares.append(Square(id=42, category=3))
        squares.append(Square(id=43, category=2))
        squares.append(Square(id=44, roll_again=True))

        # row 1
        squares[0].neighbors.extend([squares[1], squares[9]])
        squares[1].neighbors.extend([squares[0], squares[2]])
        squares[2].neighbors.extend([squares[1], squares[3]])
        squares[3].neighbors.extend([squares[2], squares[4]])
        squares[4].neighbors.extend([squares[3], squares[5], squares[10]])
        squares[5].neighbors.extend([squares[4], squares[6]])
        squares[6].neighbors.extend([squares[5], squares[7]])
        squares[7].neighbors.extend([squares[6], squares[8]])
        squares[8].neighbors.extend([squares[7], squares[11]])
        # row 2
        squares[9].neighbors.extend([squares[0], squares[12]])
        squares[10].neighbors.extend([squares[4], squares[13]])
        squares[11].neighbors.extend([squares[8], squares[14]])
        # row 3
        squares[12].neighbors.extend([squares[9], squares[15]])
        squares[13].neighbors.extend([squares[10], squares[16]])
        squares[14].neighbors.extend([squares[11], squares[17]])
        # row 4
        squares[15].neighbors.extend([squares[12], squares[18]])
        squares[16].neighbors.extend([squares[13], squares[22]])
        squares[17].neighbors.extend([squares[14], squares[26]])
        # row 5
        squares[18].neighbors.extend([squares[15], squares[19], squares[27]])
        squares[19].neighbors.extend([squares[18], squares[20]])
        squares[20].neighbors.extend([squares[19], squares[21]])
        squares[21].neighbors.extend([squares[20], squares[22]])
        squares[22].neighbors.extend([squares[16], squares[21], squares[23], squares[28]])
        squares[23].neighbors.extend([squares[22], squares[24]])
        squares[24].neighbors.extend([squares[23], squares[25]])
        squares[25].neighbors.extend([squares[24], squares[26]])
        squares[26].neighbors.extend([squares[17], squares[25], squares[29]])
        # row 6
        squares[27].neighbors.extend([squares[18], squares[30]])
        squares[28].neighbors.extend([squares[22], squares[31]])
        squares[29].neighbors.extend([squares[26], squares[32]])
        # row 7
        squares[30].neighbors.extend([squares[27], squares[33]])
        squares[31].neighbors.extend([squares[28], squares[34]])
        squares[32].neighbors.extend([squares[29], squares[35]])
        # row 8
        squares[33].neighbors.extend([squares[30], squares[36]])
        squares[34].neighbors.extend([squares[31], squares[40]])
        squares[35].neighbors.extend([squares[32], squares[44]])
        # row 9
        squares[36].neighbors.extend([squares[33], squares[37]])
        squares[37].neighbors.extend([squares[36], squares[38]])
        squares[38].neighbors.extend([squares[37], squares[39]])
        squares[39].neighbors.extend([squares[38], squares[40]])
        squares[40].neighbors.extend([squares[34], squares[39], squares[41]])
        squares[41].neighbors.extend([squares[40], squares[42]])
        squares[42].neighbors.extend([squares[41], squares[43]])
        squares[43].neighbors.extend([squares[42], squares[44]])
        squares[44].neighbors.extend([squares[35], squares[43]])

        self.squares = squares
        self.start = squares[22]