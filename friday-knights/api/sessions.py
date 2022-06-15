from flask import Blueprint, jsonify
sessions_bp = Blueprint('sessions', __name__)


@sessions_bp.route('/sessions', methods=['GET'])
def get_sessions():
    return jsonify({
        'success': True,
        'sessions': 0
    }), 200
