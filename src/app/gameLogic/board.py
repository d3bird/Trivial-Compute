

class Square:
    def __init__(self, id=-1, category=-1, hq=False, is_start=False, neighbors = []):
        self.id = id
        self.category = category
        self.hq = hq

        #only the none color can be a roll again 
        if category == "none":
            self.roll_again = True
        else:
            self.roll_again = False

        self.is_start = is_start
        self.neighbors = neighbors

    def get_ID(self):
        return self.id
    
    def get_category(self):
        return self.category
    
    def get_neighbors(self):
        return self.neighbors

    def is_roll_again(self):
        return self.roll_again
    
    def is_hq(self):
        return self.hq
    
    def is_start(self):
        return self.is_start

class Board:
    def __init__(self):
        
        BoardSquares = {}
        
        index = 0
        BoardSquares[index] = Square(id=0,  category="none",neighbors=[1,9])
        BoardSquares[index] = Square(id=1,  category="yellow",neighbors=[0,2])
        BoardSquares[index] = Square(id=2,  category="blue",neighbors=[1,3])
        BoardSquares[index] = Square(id=3,  category="green",neighbors=[0,2])
        BoardSquares[index] = Square(id=4,  category="",neighbors=[0,2], hq=True)
        BoardSquares[index] = Square(id=5,  category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=6,  category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=7,  category="green",neighbors=[0,2])
        BoardSquares[index] = Square(id=8,  category="none",neighbors=[0,2])
        BoardSquares[index] = Square(id=9,  category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=10, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=11, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=12, category="green",neighbors=[0,2])
        BoardSquares[index] = Square(id=13, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=14, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=15, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=16, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=17, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=18, category="",neighbors=[0,2], hq=True)
        BoardSquares[index] = Square(id=19, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=20, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=21, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=22, category="none",neighbors=[0,2], is_start=True)
        BoardSquares[index] = Square(id=23, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=24, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=25, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=26, category="",neighbors=[0,2], hq=True)
        BoardSquares[index] = Square(id=27, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=28, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=29, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=30, category="none",neighbors=[0,2])
        BoardSquares[index] = Square(id=31, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=32, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=33, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=34, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=35, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=36, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=37, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=38, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=39, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=40, category="",neighbors=[0,2], hq=True)
        BoardSquares[index] = Square(id=41, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=42, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=43, category="",neighbors=[0,2])
        BoardSquares[index] = Square(id=44, category="none",neighbors=[43,2])
        
        self.start_ID = 22

    def get_start_ID(self):
        return self.start_ID

    def get_square(self, ID):
        output = None
        if ID in self.BoardSquares.keys():
            output = self.BoardSquares[ID]
        return output