from types import UnionType
from typing import Any


class Polynomial:
    '''
    ### Representing polynomials as objects
    f(x) = a_0 + a_1*x + a_2*x^2 + a_3*x^3 + . . . . . . + a_(n-1)*x^(n-1)\n
    The coefficients a_0, a_1, a_2, ... , a_(n-1) are represented as a tuple
    '''           
    
    def __init__(self, *__coeffs: float) -> tuple:
        self.__coeffs = __coeffs
    
    def __str__(self):
        return f'Coefficients : {self.__coeffs}'
       
    def get_indices(self) -> int:
        return range(len(self.__coeffs))
    
    def get_coeff(self, index:int) -> None:
        return self.__coeffs[index]
    
    def calc(self, var:list):
        def get_term(self,index:int):
            return self.get_coeff(index)*var**index
        return get_term
        
class Math_Var:
    # Methods reflect linear properties
    # ,
    def __init__(self,coefficient:float=1, index:float=1, symbol:str='X'):
        self.coefficient = coefficient
        self.index = index
        self.symbol = symbol  
    
    def map_domain():
        pass
    
    def __add__(self, other):
        if self.symbol == other.symbol:
            return self.coefficient + other.coefficient
        else:
            return f'{self.symbol} + {other.symbol}'
        
    def __repr__(self) -> str:
        if self.coefficient == 0:
            return ''
        elif self.index == 0:
            return f'{self.coefficient}'
        elif self.index == 1 and self.coefficient == 1:
            return f'{self.symbol}'
        elif self.index != 1 and self.coefficient == 1:
            return f'{self.symbol}^({self.index})'
        else:
            return f'{self.coefficient}.{self.symbol}^({self.index})' 


print(Math_Var(0,0))
print(Math_Var(0,1))
print(Math_Var(1,0))
print(Math_Var(1,1))
print(Math_Var(1,2))
print(Math_Var(2,1))
