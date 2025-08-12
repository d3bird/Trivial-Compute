

class Square:
    def __init__(self,X,Y, id=-1, category=-1, hq=False, is_start=False, neighbors = [], ):
        self.id = id
        self.category = category
        self.hq = hq
        self.x = X
        self.y = Y

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
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
class Board:
    def __init__(self):
        
        self.BoardSquares = {}
        
        index = 0
        self.BoardSquares[index] = Square(1,0,id=0,  category="none",neighbors=[1,9])
        index +=1
        self.BoardSquares[index] = Square(2,0,id=1,  category="yellow",neighbors=[0,2])
        index +=1
        self.BoardSquares[index] = Square(3,0,id=2,  category="blue",neighbors=[1,3])
        index +=1
        self.BoardSquares[index] = Square(4,0,id=3,  category="green",neighbors=[2,4])
        index +=1
        self.BoardSquares[index] = Square(5,0,id=4,  category="red",neighbors=[3,10,5], hq=True)
        index +=1
        self.BoardSquares[index] = Square(6,0,id=5,  category="yellow",neighbors=[4,6])
        index +=1
        self.BoardSquares[index] = Square(7,0,id=6,  category="blue",neighbors=[5,7])
        index +=1
        self.BoardSquares[index] = Square(8,0,id=7,  category="green",neighbors=[6,8])
        index +=1
        self.BoardSquares[index] = Square(9,0,id=8,  category="none",neighbors=[7,11])
        index +=1
        self.BoardSquares[index] = Square(1,1,id=9,  category="red",neighbors=[12,0])
        index +=1
        self.BoardSquares[index] = Square(5,1,id=10, category="yellow",neighbors=[13,4])
        index +=1
        self.BoardSquares[index] = Square(9,1,id=11, category="red",neighbors=[14,8])
        index +=1
        self.BoardSquares[index] = Square(1,2,id=12, category="green",neighbors=[15,9])
        index +=1
        self.BoardSquares[index] = Square(5,2,id=13, category="blue",neighbors=[16,10])
        index +=1
        self.BoardSquares[index] = Square(9,2,id=14, category="green",neighbors=[17,11])
        index +=1
        self.BoardSquares[index] = Square(1,3,id=15, category="blue",neighbors=[18,12])
        index +=1
        self.BoardSquares[index] = Square(5,3,id=16, category="green",neighbors=[22,13])
        index +=1
        self.BoardSquares[index] = Square(9,3,id=17, category="blue",neighbors=[16,14])
        index +=1
        self.BoardSquares[index] = Square(1,4,id=18, category="yellow",neighbors=[27,15,19], hq=True)
        index +=1
        self.BoardSquares[index] = Square(2,4,id=19, category="blue",neighbors=[18,20])
        index +=1
        self.BoardSquares[index] = Square(3,4,id=20, category="green",neighbors=[19,21])
        index +=1
        self.BoardSquares[index] = Square(4,4,id=21, category="red",neighbors=[20,22])
        index +=1
        self.BoardSquares[index] = Square(5,4,id=22, category="none",neighbors=[21,16,23,28], is_start=True)
        index +=1
        self.BoardSquares[index] = Square(6,4,id=23, category="blue",neighbors=[22,24])
        index +=1
        self.BoardSquares[index] = Square(7,4,id=24, category="yellow",neighbors=[23,25])
        index +=1
        self.BoardSquares[index] = Square(8,4,id=25, category="red",neighbors=[24,26])
        index +=1
        self.BoardSquares[index] = Square(9,4,id=26, category="green",neighbors=[25,17,29], hq=True)
        index +=1
        self.BoardSquares[index] = Square(1,5,id=27, category="red",neighbors=[18,30])
        index +=1
        self.BoardSquares[index] = Square(5,5,id=28, category="yellow",neighbors=[22,31])
        index +=1
        self.BoardSquares[index] = Square(9,5,id=29, category="red",neighbors=[26,32])
        index +=1
        self.BoardSquares[index] = Square(1,6,id=30, category="green",neighbors=[27,33])
        index +=1
        self.BoardSquares[index] = Square(5,6,id=31, category="red",neighbors=[28,34])
        index +=1
        self.BoardSquares[index] = Square(9,6,id=32, category="green",neighbors=[29,35])
        index +=1
        self.BoardSquares[index] = Square(1,7,id=33, category="blue",neighbors=[30,36])
        index +=1
        self.BoardSquares[index] = Square(5,7,id=34, category="green",neighbors=[31,40])
        index +=1
        self.BoardSquares[index] = Square(9,7,id=35, category="blue",neighbors=[32,44])
        index +=1
        self.BoardSquares[index] = Square(1,8,id=36, category="none",neighbors=[33,37])
        index +=1
        self.BoardSquares[index] = Square(2,8,id=37, category="yellow",neighbors=[36,38])
        index +=1
        self.BoardSquares[index] = Square(3,8,id=38, category="red",neighbors=[37,39])
        index +=1
        self.BoardSquares[index] = Square(4,8,id=39, category="green",neighbors=[38,40])
        index +=1
        self.BoardSquares[index] = Square(5,8,id=40, category="blue",neighbors=[39,34,41], hq=True)
        index +=1
        self.BoardSquares[index] = Square(6,8,id=41, category="yellow",neighbors=[40,42])
        index +=1
        self.BoardSquares[index] = Square(7,8,id=42, category="red",neighbors=[41,43])
        index +=1
        self.BoardSquares[index] = Square(8,8,id=43, category="green",neighbors=[42,44])
        index +=1
        self.BoardSquares[index] = Square(9,8,id=44, category="none",neighbors=[43,35])
        
        self.start_ID = 22

    def get_start_ID(self):
        return self.start_ID

    def get_square(self, ID):
        output = None
        if ID in self.BoardSquares.keys():
            output = self.BoardSquares[ID]
        else:
            print("could not find square with ID : " + str(ID))
        return output