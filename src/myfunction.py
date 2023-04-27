"""
These are my functions
"""

def add(x:int, y:int, _round:bool=True) -> int:
    if _round:
        return round(x+y)
    else: 
        return x+y

