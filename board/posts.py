from flask import Blueprint, render_template, redirect, request, url_for, flash
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

@bp.route("/edit/<int:post_id>", methods=["GET", "POST"])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        new_message = request.form.get("message")
        if new_message:
            post.message = new_message
            db.session.commit()
            return redirect(url_for("posts.posts"))
    return render_template("posts/edit.html", post=post)

@bp.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted!')
    return redirect(url_for("posts.posts"))