from catalogo.model import Person
from catalogo.repository import PersonRepository
import datetime
from unittest import TestCase


class PersonReposioryTestCase(TestCase):

    def setUp(self):
        self.repository: PersonRepository = PersonRepository()

    def teste_insert_operation(self):
        person: Person = Person(
            name="Nelson Pereira de Paula Netto", 
            birthdate = datetime.datetime(year = 2004, month = 12, day = 1)
        )
        
        old_person_count: int = self.repository.count()

        self.assertIsNone(person.id)

        self.repository.insert(person)

        self.assertIsInstance(person.id, int)

        new_person_count: int = self.repository.count()
        self.assertEqual(new_person_count, old_person_count + 1)
    
    def test_delete_operation(self):
        person: Person = Person(
            name="Nelson Pereira de Paula Netto", 
            birthdate = datetime.datetime(year = 2004, month = 12, day = 1),
            id = 1
        )
        
        self.repository.delete(person)
    
    def test_insert_people_operation(self):
        people = [
            Person(name="Nelson Pereira de Paula Netto", birthdate=datetime.datetime(2004, 12, 1)),
            Person(name="Maria Clara Silva", birthdate=datetime.datetime(1998, 3, 15)),
            Person(name="João Pedro Santos", birthdate=datetime.datetime(2001, 7, 22)),
            Person(name="Ana Beatriz Oliveira", birthdate=datetime.datetime(1995, 11, 30)),
            Person(name="Lucas Gabriel Costa", birthdate=datetime.datetime(2000, 5, 10)),
            Person(name="Gabriel Almeida", birthdate=datetime.datetime(1999, 8, 25)),
            Person(name="Larissa Fernandes", birthdate=datetime.datetime(2002, 2, 14)),
            Person(name="Rafael Souza", birthdate=datetime.datetime(1997, 6, 3)),
            Person(name="Juliana Rocha", birthdate=datetime.datetime(1996, 9, 12)),
            Person(name="Leonardo Silva", birthdate=datetime.datetime(2000, 10, 21)),
            Person(name="Alice Santos", birthdate=datetime.datetime(1995, 1, 5)),
            Person(name="Bruno Oliveira", birthdate=datetime.datetime(1998, 2, 10)),
            Person(name="Carla Mendes", birthdate=datetime.datetime(2000, 3, 15)),
            Person(name="Diego Costa", birthdate=datetime.datetime(1997, 4, 20)),
            Person(name="Elisa Ferreira", birthdate=datetime.datetime(1999, 5, 25)),
            Person(name="Felipe Lima", birthdate=datetime.datetime(2001, 6, 30)),
            Person(name="Gabriela Souza", birthdate=datetime.datetime(2003, 7, 5)),
            Person(name="Henrique Alves", birthdate=datetime.datetime(1996, 8, 10)),
            Person(name="Isabela Rocha", birthdate=datetime.datetime(1998, 9, 15)),
            Person(name="João Vitor", birthdate=datetime.datetime(2000, 10, 20)),
            Person(name="Karina Silva", birthdate=datetime.datetime(2002, 11, 25)),
            Person(name="Lucas Martins", birthdate=datetime.datetime(2004, 12, 30)),
            Person(name="Mariana Costa", birthdate=datetime.datetime(1995, 1, 10)),
            Person(name="Nicolas Pereira", birthdate=datetime.datetime(1997, 2, 15)),
            Person(name="Olivia Fernandes", birthdate=datetime.datetime(1999, 3, 20)),
            Person(name="Pedro Henrique", birthdate=datetime.datetime(2001, 4, 25)),
            Person(name="Quintino Almeida", birthdate=datetime.datetime(2003, 5, 30)),
            Person(name="Rafaela Lima", birthdate=datetime.datetime(1996, 6, 5)),
            Person(name="Samuel Santos", birthdate=datetime.datetime(1998, 7, 10)),
            Person(name="Tatiana Oliveira", birthdate=datetime.datetime(2000, 8, 15)),
            Person(name="Ursula Mendes", birthdate=datetime.datetime(2002, 9, 20)),
            Person(name="Victor Costa", birthdate=datetime.datetime(2004, 10, 25)),
            Person(name="Wesley Ferreira", birthdate=datetime.datetime(1995, 11, 30)),
            Person(name="Xavier Lima", birthdate=datetime.datetime(1997, 12, 5)),
            Person(name="Yasmin Souza", birthdate=datetime.datetime(1999, 1, 10)),
            Person(name="Zoe Alves", birthdate=datetime.datetime(2001, 2, 15)),
            Person(name="Arthur Rocha", birthdate=datetime.datetime(2003, 3, 20)),
            Person(name="Beatriz Martins", birthdate=datetime.datetime(1996, 4, 25)),
            Person(name="Caio Pereira", birthdate=datetime.datetime(1998, 5, 30)),
            Person(name="Daniela Fernandes", birthdate=datetime.datetime(2000, 6, 5)),
            Person(name="Eduardo Henrique", birthdate=datetime.datetime(2002, 7, 10)),
            Person(name="Fernanda Almeida", birthdate=datetime.datetime(2004, 8, 15)),
            Person(name="Gustavo Lima", birthdate=datetime.datetime(1995, 9, 20)),
            Person(name="Helena Santos", birthdate=datetime.datetime(1997, 10, 25)),
            Person(name="Igor Oliveira", birthdate=datetime.datetime(1999, 11, 30)),
            Person(name="Julia Costa", birthdate=datetime.datetime(2001, 12, 5)),
            Person(name="Kevin Ferreira", birthdate=datetime.datetime(2003, 1, 10)),
            Person(name="Larissa Mendes", birthdate=datetime.datetime(1996, 2, 15)),
            Person(name="Marcelo Lima", birthdate=datetime.datetime(1998, 3, 20)),
            Person(name="Natália Souza", birthdate=datetime.datetime(2000, 4, 25)),
            Person(name="Otávio Alves", birthdate=datetime.datetime(2002, 5, 30)),
            Person(name="Patrícia Rocha", birthdate=datetime.datetime(2004, 6, 5)),
            Person(name="Renato Martins", birthdate=datetime.datetime(1995, 7, 10)),
            Person(name="Sofia Pereira", birthdate=datetime.datetime(1997, 8, 15)),
            Person(name="Thiago Fernandes", birthdate=datetime.datetime(1999, 9, 20)),
            Person(name="Ubirajara Henrique", birthdate=datetime.datetime(2001, 10, 25)),
            Person(name="Valentina Almeida", birthdate=datetime.datetime(2003, 11, 30)),
            Person(name="William Lima", birthdate=datetime.datetime(1996, 12, 5)),
            Person(name="Ximena Santos", birthdate=datetime.datetime(1998, 1, 10)),
            Person(name="Yuri Oliveira", birthdate=datetime.datetime(2000, 2, 15)),
            Person(name="Alice Santos", birthdate=datetime.datetime(1995, 1, 5)),
            Person(name="Bruno Oliveira", birthdate=datetime.datetime(1998, 2, 10)),
            Person(name="Carla Mendes", birthdate=datetime.datetime(2000, 3, 15)),
            Person(name="Diego Costa", birthdate=datetime.datetime(1997, 4, 20)),
            Person(name="Elisa Ferreira", birthdate=datetime.datetime(1999, 5, 25)),
            Person(name="Felipe Lima", birthdate=datetime.datetime(2001, 6, 30)),
            Person(name="Gabriela Souza", birthdate=datetime.datetime(2003, 7, 5)),
            Person(name="Henrique Alves", birthdate=datetime.datetime(1996, 8, 10)),
            Person(name="Isabela Rocha", birthdate=datetime.datetime(1998, 9, 15)),
            Person(name="João Vitor", birthdate=datetime.datetime(2000, 10, 20)),
            Person(name="Karina Silva", birthdate=datetime.datetime(2002, 11, 25)),
            Person(name="Lucas Martins", birthdate=datetime.datetime(2004, 12, 30)),
            Person(name="Mariana Costa", birthdate=datetime.datetime(1995, 1, 10)),
            Person(name="Nicolas Pereira", birthdate=datetime.datetime(1997, 2, 15)),
            Person(name="Olivia Fernandes", birthdate=datetime.datetime(1999, 3, 20)),
            Person(name="Pedro Henrique", birthdate=datetime.datetime(2001, 4, 25)),
            Person(name="Quintino Almeida", birthdate=datetime.datetime(2003, 5, 30)),
            Person(name="Rafaela Lima", birthdate=datetime.datetime(1996, 6, 5)),
            Person(name="Samuel Santos", birthdate=datetime.datetime(1998, 7, 10)),
            Person(name="Tatiana Oliveira", birthdate=datetime.datetime(2000, 8, 15)),
            Person(name="Ursula Mendes", birthdate=datetime.datetime(2002, 9, 20)),
            Person(name="Victor Costa", birthdate=datetime.datetime(2004, 10, 25)),
            Person(name="Wesley Ferreira", birthdate=datetime.datetime(1995, 11, 30)),
            Person(name="Xavier Lima", birthdate=datetime.datetime(1997, 12, 5)),
            Person(name="Yasmin Souza", birthdate=datetime.datetime(1999, 1, 10)),
            Person(name="Zoe Alves", birthdate=datetime.datetime(2001, 2, 15)),
            Person(name="Arthur Rocha", birthdate=datetime.datetime(2003, 3, 20)),
            Person(name="Beatriz Martins", birthdate=datetime.datetime(1996, 4, 25)),
            Person(name="Caio Pereira", birthdate=datetime.datetime(1998, 5, 30)),
            Person(name="Daniela Fernandes", birthdate=datetime.datetime(2000, 6, 5)),
            Person(name="Eduardo Henrique", birthdate=datetime.datetime(2002, 7, 10)),
            Person(name="Fernanda Almeida", birthdate=datetime.datetime(2004, 8, 15)),
            Person(name="Gustavo Lima", birthdate=datetime.datetime(1995, 9, 20)),
            Person(name="Helena Santos", birthdate=datetime.datetime(1997, 10, 25)),
            Person(name="Igor Oliveira", birthdate=datetime.datetime(1999, 11, 30)),
            Person(name="Julia Costa", birthdate=datetime.datetime(2001, 12, 5)),
            Person(name="Kevin Ferreira", birthdate=datetime.datetime(2003, 1, 10)),
            Person(name="Larissa Mendes", birthdate=datetime.datetime(1996, 2, 15)),
            Person(name="Marcelo Lima", birthdate=datetime.datetime(1998, 3, 20)),
            Person(name="Natália Souza", birthdate=datetime.datetime(2000, 4, 25))
        ]
        for i in range(len(people)):
            self.repository.insert(people[i])
        
        self.repository.delete(people[5])
        self.repository.delete(people[67])
        self.repository.delete(people[50])
        self.repository.delete(people[33])
        self.repository.delete(people[27])
        self.repository.delete(people[8])
        self.repository.delete(people[19])
        self.repository.delete(people[91])
        self.repository.delete(people[81])
        self.repository.delete(people[44])
  
        people = [
            Person(name="Bruna Ferreira", birthdate=datetime.datetime(2000, 2, 5)),
            Person(name="Carlos Henrique Silva", birthdate=datetime.datetime(1998, 7, 19)),
            Person(name="Daniela Costa", birthdate=datetime.datetime(2003, 3, 22)),
            Person(name="Eduarda Santos", birthdate=datetime.datetime(2001, 12, 10)),
            Person(name="Felipe Almeida", birthdate=datetime.datetime(1999, 5, 14)),
            Person(name="Giovana Oliveira", birthdate=datetime.datetime(2002, 8, 30)),
            Person(name="Henrique Souza", birthdate=datetime.datetime(1997, 11, 3)),
            Person(name="Isabel Ribeiro", birthdate=datetime.datetime(1996, 4, 27)),
            Person(name="Joana Martins", birthdate=datetime.datetime(2004, 6, 9)),
            Person(name="Leonardo Rocha", birthdate=datetime.datetime(2000, 10, 21))
        ]
        for i in range(len(people)):
            self.repository.insert(people[i])
            
        
        if self.repository.storage[109].id is None:
            pass
        
        
        