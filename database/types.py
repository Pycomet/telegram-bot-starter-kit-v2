from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    "User Class Repr"
    _id: str = 0
    name: str
    wallet: str
    chat: str
    verified: bool = False
    disabled: bool = False
    created_at: str = date.now()
