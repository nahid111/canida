from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import *
from models import *

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(engine)
session = Session()

# Seed data
p1 = Professor(id=1, name='Xavier')
p2 = Professor(id=2, name='Banner')

c1 = Course(id=1, name='Mathematics', professor_id=p1.id)
c2 = Course(id=2, name='Physics', professor_id=p1.id)
c3 = Course(id=3, name='Chemistry', professor_id=p2.id)
c4 = Course(id=4, name='Biology', professor_id=p2.id)

s1 = Student(id=1, name='Adam')
s2 = Student(id=2, name='Ben')
s3 = Student(id=3, name='Clark')
s4 = Student(id=4, name='Donald')
s5 = Student(id=5, name='Fred')
s6 = Student(id=6, name='George')

s1.courses.extend([c1, c3])
s2.courses.extend([c2, c4])
s3.courses.extend([c1, c2])
s4.courses.extend([c3, c4])
s5.courses.extend([c1, c4])
s6.courses.extend([c2, c3])

# Commit Data
objects = [p1, p2, c1, c2, c3, c4]
session.add_all(objects)
session.commit()
