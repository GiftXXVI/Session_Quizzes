from flask import Blueprint, jsonify
from flask_cors import CORS
sessions_bp = Blueprint('sessions', __name__)

CORS(
    sessions_bp,
    resources=r'/sessions',
    origins=r'*',
    methods=[
        'PATCH',
        'PUT',
        'DELETE'])


@sessions_bp.route('/sessions', methods=['GET'])
def get_sessions():
    return jsonify({
        'success': True,
        'sessions': 0
    }), 200
