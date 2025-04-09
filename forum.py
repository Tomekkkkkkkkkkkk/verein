from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime

forum_bp = Blueprint('forum', __name__, template_folder='templates')
forum_posts = []

@forum_bp.route('/forum')
@login_required
def forum():
    return render_template('forum.html', posts=reversed(forum_posts))

@forum_bp.route('/forum/post', methods=['POST'])
@login_required
def post():
    content = request.form['content']
    if content:
        forum_posts.append({
            'author': current_user.username,
            'timestamp': datetime.now().strftime('%d.%m.%Y %H:%M:%S'),
            'content': content
        })
    return redirect(url_for('forum.forum'))
