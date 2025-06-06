from flask import Blueprint, render_template

bp = Blueprint('errors', __name__)

@bp.app_errorhandler(404)
def handle_404(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def handle_500(error):
    return render_template('errors/500.html'), 500