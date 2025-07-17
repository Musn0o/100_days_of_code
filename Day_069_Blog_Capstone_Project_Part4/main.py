from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from functools import wraps
from forms import CreatePostForm, RegisterForm, LoginForm, CommentForm
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import hashlib

# Initialize Flask application
app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.config["SECRET_KEY"] = secret_key
ckeditor = CKEditor(app)
bootstrap = Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


# Configure SQLAlchemy database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# User loader callback
@login_manager.user_loader
def load_user(user_id):
    """User loader callback for Flask-Login."""
    return User.query.get(int(user_id))


# --- Database Models ---


# Create User class
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    email: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    posts: Mapped[list["BlogPost"]] = relationship(back_populates="author")
    comments: Mapped[list["Comment"]] = relationship(back_populates="comment_author")


# Create BlogPost class
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship(back_populates="parent_post")


# Create Comment class
class Comment(db.Model):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(Integer, db.ForeignKey("users.id"))
    comment_author: Mapped["User"] = relationship(back_populates="comments")
    post_id: Mapped[str] = mapped_column(Integer, db.ForeignKey("blog_posts.id"))
    parent_post: Mapped["BlogPost"] = relationship(back_populates="comments")
    text: Mapped[str] = mapped_column(Text, nullable=False)


# --- Decorators and Utility Functions ---


# Decorator to restrict access to admin users only
def admin_only(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        # Checks if the current user is authenticated and has an ID of 1 (assuming admin ID is 1)
        if not current_user.is_authenticated or current_user.id != 1:
            abort(403)
        return func(*args, **kwargs)

    return wrapper_function


# Function to generate Gravatar URL based on email
def get_gravatar_url(email, size=100, default="retro", rating="g"):
    url = "https://www.gravatar.com/avatar/"
    hash_value = hashlib.md5(email.lower().encode("utf-8")).hexdigest()
    url += hash_value + f"?s={size}&d={default}&r={rating}"
    return url


# Helper function to flash messages with optional links
def flash_message(category, message, link_text=None, link_url=None):
    """Utility function to flash messages with optional links."""
    if link_text and link_url:
        message += f' <a href="{link_url}" class="alert-link" style="color: #007bff; text-decoration: underline;">{link_text}</a>'
    flash(message, category)


# --- Routes ---


@app.route("/")
def get_all_posts():
    # Retrieve all blog posts from the database
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST" and form.validate():
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Hash the password
        hashed_password = generate_password_hash(
            password, method="pbkdf2:sha256", salt_length=8
        )

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash_message(
                "danger",
                "Email already registered. Please use another email or",
                "Log In Here",
                url_for("login"),
            )

            return redirect(url_for("register"))

        # Create new user and add to database
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash_message("success", f"Account created for {name}!")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        email = request.form.get("email")
        password = request.form.get("password")
        remember = "remember" in request.form

        # Check if user exists
        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=remember)
                flash_message("success", "Logged In successfully!")
                return redirect(url_for("get_all_posts"))
            else:
                flash_message("danger", "Incorrect password. Please try again.")
        else:
            flash_message(
                "danger",
                "Email not found. Please use the correct email or",
                "Sign Up Here",
                url_for("register"),
            )

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    # Log out the current user
    logout_user()
    flash_message("success", "Logged out successfully!")
    return redirect(url_for("get_all_posts"))


@app.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    comment_form = CommentForm()

    if request.method == "POST":
        if current_user.is_authenticated:
            if comment_form.validate_on_submit():
                new_comment = Comment(
                    text=comment_form.comment_text.data,
                    comment_author=current_user,
                    parent_post=requested_post,
                )
                db.session.add(new_comment)
                db.session.commit()
                return redirect(url_for("show_post", post_id=post_id))
        else:
            flash_message(
                "warning",
                "You must be logged in to leave a comment.",
                "Log In Here",
                url_for("login"),
            )
            return redirect(url_for("login"))

    return render_template(
        "post.html",
        post=requested_post,
        form=comment_form,
        current_user=current_user,
        get_gravatar_url=get_gravatar_url,
    )


@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y"),
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
@admin_only
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body,
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.author = current_user
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("make-post.html", form=edit_form, is_edit=True)


@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
