from typing import List
from catalogo.model.person import Person

class PersonRepository: 

    def __init__(self) -> None:
        self.storage: List[Person] = []
        self.last_used_id = int = 0  

    def insert(self, person: Person) -> None:
        assert person.id is None, "Person's id should be None"
        self.storage.append(person)
        self.last_used_id += 1
        person.id = self.last_used_id 
        print(person.id)

    def count(self):
        return len(self.storage)

    def delete(self, person: Person):
        assert person.id is not None, 'Person has alredy been delete'
        for i in range(len(self.storage)):
            if self.storage[i] == person:
                self.storage[i].name = None
                self.storage[i].birthdate = None
                self.storage[i].id = None