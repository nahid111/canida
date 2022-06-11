from flask import Blueprint, request, jsonify

from db import db
from models import Professor
from schemas import ProfessorSchema

bp_professor = Blueprint('professor', __name__)


@bp_professor.route('/', methods=['GET'])
def get_professors():
    """All
    This Returns a list of Professor objects
    ---
    tags:
      - name: Professors
    definitions:
      Professor:
        type: object
        properties:
          id:
            type: integer
          name:
            type: string
          courses:
            type: array
            items:
              type: string
    responses:
      200:
        description: A list of Professor objects
    """
    sc = ProfessorSchema(many=True)
    professors = Professor.query.all()
    return jsonify(sc.dump(professors)), 200


@bp_professor.route('/<int:id>', methods=['GET'])
def get_professors_by_id(id: int):
    """By id
    This Returns a single Professor by id
    ---
    tags:
      - name: Professors
    parameters:
      - in: path
        name: id
        required: true
    responses:
      200:
        description: A single Professor object
        schema:
            $ref: '#/definitions/Professor'
    """
    sc = ProfessorSchema()
    professors = Professor.query.get(id)
    return sc.dump(professors), 200


@bp_professor.route('/', methods=['POST'])
def create_professors():
    """Create
    This creates a Professor object
    ---
    tags:
      - name: Professors
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
        - in: body
          name: professor
          required: true
          description: The Professor to create.
          properties:
            name:
              type: string
    responses:
      202:
        description: A single Professor object
        schema:
            $ref: '#/definitions/Professor'
    """
    payload = request.json
    professors = Professor(name=payload.get('name'))
    db.session.add(professors)
    db.session.commit()
    sc = ProfessorSchema()
    return sc.dump(professors), 202


@bp_professor.route('/<int:id>', methods=['DELETE'])
def delete_professors(id: int):
    """Delete
    This deletes a Professor object
    ---
    tags:
      - name: Professors
    parameters:
      - in: path
        name: id
        required: true
    responses:
      200:
        description: Object deleted
    """
    professors = Professor.query.get(id)
    db.session.delete(professors)
    db.session.commit()
    return {}, 200
