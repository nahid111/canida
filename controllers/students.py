from flask import Blueprint, jsonify

from models import Student
from schemas import StudentSchema

bp_student = Blueprint('student', __name__)


@bp_student.route('/', methods=['GET'])
def get_students():
    """All
    Returns a list of Student objects
    ---
    tags:
      - name: Students
    definitions:
      Student:
        type: object
        properties:
          id:
            type: int
          name:
            type: string
          courses:
            type: array
            items:
              type: string
    responses:
      200:
        description: A list of Student objects
    """
    sc = StudentSchema(many=True)
    students = Student.query.all()
    return jsonify(sc.dump(students)), 200


@bp_student.route('/<int:id>', methods=['GET'])
def get_students_by_id(id: int):
    """By id
    This Returns a single Student by id
    ---
    tags:
      - name: Students
    parameters:
      - in: path
        name: id
        required: true
    responses:
      200:
        description: A single Student object
        schema:
            $ref: '#/definitions/Student'
    """
    sc = StudentSchema()
    student = Student.query.get(id)
    return sc.dump(student), 200
