class Rectangle:
    nbr = 0
    def __init__(self,longeur , largeur):
        self.longeur = longeur
        self.largeur = largeur
        
    def prémiter(self):  
        return 2*(self.longeur+self.largeur)
    def Aire(self):
        # Calculate and return the area of the rectangle
        return  self.largeur * self.longeur
    def is_carre(self):
        if  self.largeur == self.longeur :
            print("this rectangle is carre")
        else :
            print("this rectangle is not carre")
    def affichage (self):
        print(self.largeur)
        print(self.largeur)
        print(Rectangle.prémiter(self))
        print(Rectangle.Aire(self))
        print(Rectangle.is_carre(self))