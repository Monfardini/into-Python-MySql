from dataclasses import dataclass
import datetime
from typing import Optional
@dataclass
class Person:
    name: str
    birthdate: Optional[datetime.datetime] = None
    id: Optional[int] = None
    
    
   