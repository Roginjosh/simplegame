def bigprint(prn):
    for i in len(prn):
        print(prn[i])




# class Cell:
#     def __init__(self, center = "", sides=wall):
#         self.sides = sides
#         self.center = center
#         if self.center == "":
#             all_wall = True
#             for key in self.sides:
#                 if self.sides[key] == False:
#                     all_wall = False
#             if all_wall:
#                 center == "█"
    
class Cell:
    def __init__(self, sides = ""):
        self.n = "  " if "n" in sides else "██"
        self.s = "  " if "s" in sides else "██"
        self.e = "  " if "e" in sides else "██"
        self.w = "  " if "w" in sides else "██"
    
    def draw(self):
        return [
        f'██{self.n}██',
        f'{self.w}  {self.e}',
        f'██{self.s}██'
        ]
        



def print_map(map):
    printable = []
    for i in range(len(map)):
        firstCell = map[i][0].draw()
        row0 = firstCell[0]
        row1 = firstCell[1]
        row2 = firstCell[2]
        if len(map[0]) > 1:
            for ii in range(len(map[0])-1):
                this_cell = map[i][ii+1].draw()
                row0 += this_cell[0]
                row1 += this_cell[1]
                row2 += this_cell[2]
        
        printable.append(row0)
        printable.append(row1)
        printable.append(row2)
    
    for i in range(len(printable)):
        print(printable[i])




if __name__ == "__main__":
    map = [
        [Cell("nswe"), Cell("ew"), Cell("ws")],
        [Cell("ns"), Cell("nsew"), Cell("ns")],
        [Cell("ne"), Cell("ew"), Cell("wn")],
    ]

    # map = [
    #     [Cell(nw), Cell(ne)],
    #     [Cell(sw), Cell(es)],
    #        ]
    print_map(map)