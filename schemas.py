from flask_marshmallow import Marshmallow
from models import Professor, Course, Student

ma = Marshmallow()


class CourseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Course

    id = ma.auto_field()
    name = ma.auto_field()
    professor = ma.Pluck('self', 'name')
    students = ma.Pluck('self', 'name', many=True)


class ProfessorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Professor

    id = ma.auto_field()
    name = ma.auto_field()
    # courses = ma.Nested(CourseSchema(only=('id', 'name',)), many=True)
    courses = ma.Pluck('self', 'name', many=True)


class StudentSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Student

    id = ma.auto_field()
    name = ma.auto_field()
    courses = ma.Pluck('self', 'name', many=True)
