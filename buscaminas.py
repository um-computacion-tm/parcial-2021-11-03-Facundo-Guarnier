import random

class Buscaminas:
    def __init__(self, rows="", cols="", bombs=""):
        self.rows=rows
        self.cols=cols
        self.bombs=bombs
        # self.show=[["-"]*cols]*rows        #Sin nada
        # self.board=[["-"]*cols]*rows        #Con bombas
        self.show=self.crear()
        self.board=self.crear(True)


    def crear(self, bomba=False):
        
        tablero=[]
        for c in range(self.cols):
            fila=["-"]
            for f in range(self.rows):
                fila.append("-")
            tablero.append(fila)

        if bomba:
            for i in range(self.bombs+1):
                tablero[random.randrange(0, self.rows, 1)][random.randrange(0, self.cols, 1)]="B"


        
        return tablero

    def lose(self):
        for i in self.show: 
            if "B" in i:
                return True
        return False


    def win(self):
        cantidad=0
        for i in self.show: 
            for j in i:
                if "F" == j:
                    cantidad+=1
        if cantidad==self.bombs:
            return True
        return False
        

    def show_board(self):   #imprime la tabla con los datos y la tabla a completar
        # self.show=self.crear()
        a=""
        for i in range(self.rows):
            a = a + str(self.board[i]) + "  " + str(self.show[i]) + "\n"
        print(a)


    def question(self, a):
        mov = input("Ingrese movimiento: ")
        if not mov in a: 
            raise Exception
        row = int(input("Ingrese fila: "))
        col = int(input("Ingrese columna: "))
        if col > self.cols or row > self.rows:
            raise Exception
        return mov, row, col


    def play(self, movimineto, fila, columna):

        if movimineto == "uncover":
            self.show[fila][columna]=self.board[fila][columna]


        elif movimineto == "flag":   #solo marcar si hay bomba
            self.show[fila][columna]="F"

