from db import db


# Professor Course  1->*
# Course Student *->8
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(191), unique=True, nullable=False)
    courses = db.relationship('Course', backref='professor', lazy='dynamic')


CourseStudentAssociation = db.Table('course_student_association',
                                    db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True),
                                    db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True)
                                    )


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(191), unique=True, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(191))
    courses = db.relationship('Course', secondary=CourseStudentAssociation, lazy='subquery',
                              backref=db.backref('students', lazy='dynamic'))
