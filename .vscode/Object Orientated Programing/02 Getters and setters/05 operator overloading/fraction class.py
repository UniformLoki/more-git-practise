


class Fraction:
    
    def __init__(self, num:int=0, den:int=1) -> None:
        self.num = num
        if den == 0:
            den = 1
        self.den = den
        self.reduce()
     
    @property
    def num(self) -> int:
        return self._num  
    
    @num.setter
    def num(self, value:int) -> None:
        self._num = value
        
    @property
    def den(self) -> int:
        return self._den  
    
    @den.setter
    def den(self, value:int) -> None:
        if value != 0:
            self._den = value

    def reduce(self) -> None:
        gcd = 1
        minimum = min(abs(self.num), abs(self.den))
        
        for i in range(2, int(minimum + 1)):
            if self.num % i == 0 and self.den % i == 0:
                gcd = i
                
        self.num = int(self.num / gcd)
        self.den = int(self.den / gcd)
        
        
        if self.num == 0:
            self.den = 1
            
    def __add__(self, other:'Fraction') -> 'Fraction':
            new_num = self.num * other.den + self.den * other.num
            new_den = self.den * other.den
            result = Fraction(new_num/new_den)
            return result
        
    def __sub__(self, other:'Fraction') -> 'Fraction':
            new_num = self.num * other.den + self.den * other.num
            new_den = self.den * other.den
            result = Fraction(new_num,new_den)
            return result
            
    def __mul__(self, other:'Fraction') -> 'Fraction':
            new_num = self.num * other.den 
            new_den = self.den * other.den
            result = Fraction(new_num,new_den)
            return result        
        
    def __truediv__(self, other:'Fraction') -> 'Fraction':
            new_num = self.num * other.den
            new_den = self.den * other.num
            result = Fraction(new_num,new_den)
            return result
          
            
            
    def __str__(self):
            return f"{self.num} / {self.den}"
        
        
        
f1 = Fraction()
f2 = Fraction(2, 4)

print(f1)
print(f2)

f3 = f1 + f2
print(f3)