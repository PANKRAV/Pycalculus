#BUILTINS
from functools import singledispatchmethod
from typing import Callable

#THIRDPARTIES


#MYMODULES


class OutsideDomain(Exception) :
    ...



#vars
placeholder = ""



class Fonction(object) :
    
    def __new__(cls, *args, **kwargs) :
        functype = None
        if isinstance(args[0], str) :
            ...
        elif isinstance(args[0], Callable) :
            ...
        else :
            raise NotImplementedError("Function type not implemented yet or wrong initialization format")


            
        if functype == "Power" :
            return Power.__new__(Power, *args, **kwargs)
        
        elif functype == "Root" :
            return Root.__new__(Root, *args, **kwargs)

        
        elif functype == "Log" :
            return Log.__new__(Log, *args, **kwargs)

        
        elif functype == "Exp" :
            return Exp.__new__(Exp, *args, **kwargs)


        else :
            raise NotImplemented("Function type not implemented yet or wrong initialization format")
        
        


    #Not to be called seperately
    def __init__(self, domain, process : Callable) -> None:
        self.domain = domain
        self.process = process
    

    def __call__(self, /, x : float|int) :
        if float(x) in self.domain :

            return self.process(x)
        
        else :
            raise OutsideDomain
    

    def __add__(self, ctx) :
        ...
    

    def __sub__(self, ctx) :
        ...


    def __pow__(self, ctx) :
        ...

    
    def __truediv__(self, ctx) :
        ...
    

    def __mul__(self, ctx) :
        ...
    

    def __abs__(self) :
        ...



    def __iadd__(self, ctx) :
        ...
    

    def __isub__(self, ctx) :
        ...


    def __ipow__(self, ctx) :
        ...

    
    def __itruediv__(self, ctx) :
        ...
    

    def __imul__(self, ctx) :
        ...
    


    


class Power(Fonction) :
    def __new__(cls, *args, **kwargs):
        functype = None
        if functype == "Pow" :
            return object.__new__(Power)
        
        elif functype == "Polynomial" :
            return object.__new__(Root)

        
        elif functype == "Parabole" :
            return object.__new__(Parabole)

        
        elif functype == "Hyperbole" :
            return object.__new__(Hyperbole)


        else :
            raise NotImplemented("Function type not implemented yet or wrong initialization format")
    

    def __init__(self, exponent : int, domain = "R") -> None:
        self.exponent = exponent
        self.process = lambda x : x ** self.exponent
        super().__init__(self, domain, self.process)



class SimplePow(Power):
    def __new__(cls, *args, **kwargs):
        return object.__new__(SimplePow)


class Polynomial(Power) :
    def __new__(cls, *args, **kwargs):
        return object.__new__(Polynomial)


class Parabole(Power) :
    def __new__(cls, *args, **kwargs):
        return object.__new__(Parabole)


class Hyperbole(Power) :
    def __new__(cls, *args, **kwargs):
        return object.__new__(Hyperbole)

class Root(Fonction) :
    def __new__(cls, *args, **kwargs):
        functype = None
        if functype == "Root" :
            return object.__new__(Root)
        
        elif functype == "Sqrt" :
            return Root.__new__(Root, *args, **kwargs)

    
class Sqrt(Root) :
    def __new__(cls, *args, **kwargs):
        return object.__new__(Sqrt)


class Log(Fonction) :
    def __new__(cls, *args, **kwargs):
        functype = None
        if functype == "Root" :
            return object.__new__(Log)
        
        elif functype == "Sqrt" :
            return Ln.__new__(Ln, *args, **kwargs)


class Ln(Log) :
    def __new__(cls, *args, **kwargs):
        return object.__new__(Ln)


class Exp(Fonction) :
    def __new__(cls, *args, **kwargs):
        functype = None
        if functype == "Root" :
            return object.__new__(Exp)
        
        elif functype == "Sqrt" :
            return ExpE.__new__(ExpE, *args, **kwargs)


class ExpE(Exp) :
    def __new__(cls, *args, **kwargs):
        return object.__new__(ExpE)


