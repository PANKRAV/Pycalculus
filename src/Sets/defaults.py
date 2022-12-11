import random
from typing import Callable, List, Tuple




DEFAULTS = ("Reals", "Integers", "Naturals", "Empty")
class Set(object) :
    def __new__(cls, *args, **kwargs) :
        default_type = None
        if args[0] in DEFAULTS :
            args = list(args)
            default_type = args.pop(0)
            args = tuple(args)                
        if default_type == "Reals" :
            return Reals.__new__(Reals, *args, **kwargs)
        elif default_type == "Integers" :
            return Integers.__new__(Integers, *args, **kwargs)
        elif default_type == "Naturals" :
            return Naturals.__new__(Naturals, *args, **kwargs)
        
        
        return object.__new__(cls, *args, **kwargs)


    def __init__(self, filters : List[Callable] | Tuple[Callable, ...], signs = None) -> None:
        self.signs = signs
        self.filters = filters
    

    def __check__(self, /, x) :
        tests = []
        for check in self.filters :
            tests.append(check(x))
        
        if all(tests) :
            return True
        else :
            return False
    

    def __iter__(self) :
        ...
    

    def __next__(self) :
        ...
    

    def __aiter__(self) :
        ...
    

    def __anext__(self) :
        ...



    @classmethod
    def from_set_format(cls, ctx : str) :
        ...





class Reals(Set) :
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None :
            return object.__new__(cls)
        
        else :
            return cls.instance
    
    def __init__(self) -> None:
        filters = []
        filters.append(lambda x : isinstance(x, int))
        super().__init__(filters)



class Integers(Set) :
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None :
            return object.__new__(cls)
        
        else :
            return cls.instance
    
    def __init__(self) -> None:
        filters = []
        filters.append(lambda x : isinstance(x, (float, int)))
        super().__init__(filters)


class Naturals(Set) :
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None :
            return object.__new__(cls)
        
        else :
            return cls.instance
        
    def __init__(self) -> None:
        filters = []
        filters.append(lambda x : isinstance(x, int))
        filters.append(lambda x : x >= 0)
        super().__init__(filters)

class Empty(Set) :
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None :
            return object.__new__(cls)
        
        else :
            return cls.instance
        
    def __init__(self) -> None:
        filters = []
        filters.append(lambda x : False)
        super().__init__(filters)




