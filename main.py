from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    ssn = Column('ssn', Integer, primary_key=True)
    first_name = Column('first_name',String)
    last_name = Column('last_name',String)
    gender = Column('gender', CHAR)
    age = Column('age', Integer)

    def __init__(self, ssn, first_name, last_name, gender, age):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
    
    def __repr__(self):
        return f"({self.ssn} {self.first_name} {self.last_name}, {self.age}, {self.gender}"


class Things(Base):
    __tablename__ = 'things'

    tid = Column("tid", Integer, primary_key=True)
    description = Column("description", String)
    owner = Column(Integer, ForeignKey("people.ssn"))

    def __init__(self, tid, description, owner):
        self.tid = tid
        self.description = description
        self.owner = owner

    def __repr__(self):    
        return f"({self.tid}, {self.description}, Owned by {self.owner})"

engine = create_engine("sqlite:///myDb.db", echo=True)
Base.metadata.create_all(bind = engine)

Session = sessionmaker(bind=engine)
session = Session()

# person = Person(1234, "Anna", "Smith", "F", 34)
# person2 = Person(1212, "Jhon", "Colton", "M", 54)
# person3 = Person(1221, "Pete", "Singer", "M", 67)
# person4 = Person(1313, "Barbara", "Petersen", "f", 22)

# thin1 = Things(1, "Pencil", person.ssn)
# thin2 = Things(2, "Phone", person.ssn)
# thin3 = Things(3, "Suitcase", person2.ssn)


# session.add(person)
# session.add(person2)
# session.add(person3)
# session.add(person4)
# session.commit()

# session.add(thin1)
# session.add(thin2)
# session.add(thin3)
# session.commit()


# results = session.query(Person).all()
# results = session.query(Person).filter(Person.first_name == "Anna")
# results = session.query(Person).filter(Person.age > 40)
# results = session.query(Person).filter(Person.first_name.like("A%"))
# results = session.query(Person).filter(Person.first_name.in_(["Anna","Jhon"]))
results = session.query(Things, Person).filter(Things.owner == Person.ssn).filter(Person.first_name == "Anna")
for person in results:
    print(person)  

