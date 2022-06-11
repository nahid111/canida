from flask import Blueprint, jsonify, request

from models import Course
from schemas import CourseSchema

bp_course = Blueprint('course', __name__)


@bp_course.route('/', methods=['GET'])
def get_courses():
    """All or One
    Returns a list of Course objects
    OR
    Filters Courses by given Name
    ---
    tags:
      - name: Courses
    definitions:
      Course:
        type: object
        properties:
          id:
            type: int
          name:
            type: string
          professor:
            type: string
          students:
            type: array
            items:
              type: string
    parameters:
      - in: query
        name: name
        schema:
          type: string
    responses:
      200:
        description: A list of Course objects
    """
    sc = CourseSchema(many=True)
    name = request.args.get('name', None)
    if name:
        course = Course.query.filter(Course.name == name).all()
        return jsonify(sc.dump(course)), 200
    courses = Course.query.all()
    return jsonify(sc.dump(courses)), 200


@bp_course.route('/<int:id>', methods=['GET'])
def get_courses_by_id(id: int):
    """By id
    This Returns a single Course by id
    ---
    tags:
      - name: Courses
    parameters:
      - in: path
        name: id
        required: true
    responses:
      200:
        description: A single Course object
        schema:
            $ref: '#/definitions/Course'
    """
    sc = CourseSchema()
    course = Course.query.get(id)
    return sc.dump(course), 200
