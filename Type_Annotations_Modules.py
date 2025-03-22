# Type Annotations help with code clarity and static type checking.
from typing import List,Tuple

def get_coordinates()-> Tuple[float,float]:
    return (40.7128, -74.0060)

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

