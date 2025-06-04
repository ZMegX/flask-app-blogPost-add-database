from flask import Blueprint, render_template, redirect, request, url_for
from board.models import Post, db, User  # import your model and db session

bp = Blueprint("posts", __name__)

@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        username = request.form.get("author") or "Anonymous"
        message = request.form.get("message")

        if message:
            user = User.query.filter_by(username=username).first()

            if not user:
                user = User(username=username)
                db.session.add(user)
                db.session.commit()

            new_post = Post(author=user, message=message)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for("posts.posts"))

    return render_template("posts/create.html")

@bp.route("/posts")
def posts():
    posts = Post.query.order_by(Post.created.desc()).all()
    return render_template("posts/posts.html", posts=posts)
