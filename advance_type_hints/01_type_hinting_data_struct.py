"""
Docstring for advance_type_hints.01_type_hinting_data_struct
"""
# For python version <= 3.9
from typing import List, Dict, Tuple

price: List[int] = [213, 234, 984]
immutable_price: Tuple[int, int, int] = (231, 983, 704)
price_dict: Dict[str, int] = {
    "item1": 340,
    "item2": 500
}
