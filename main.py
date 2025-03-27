from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
import secrets

app = Flask(__name__)
secret_key = secrets.token_hex(16)
app.config['SECRET_KEY'] = secret_key


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"


# User loader function
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        try:
            # Pre-render check
            try:
                render_template('secrets.html', username=name)
            except Exception as e:
                print(e)
                return render_template('register.html',
                                       error="An unexpected error occurred during registration. Please try again later.")
            # Hash the password
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

            new_user = User(name=name, email=email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            return redirect(url_for('secrets', username=name))

        except IntegrityError:
            db.session.rollback()
            return render_template('register.html', error="Email already exists.")

        except SQLAlchemyError as e:
            db.session.rollback()
            return render_template('register.html', error=f"Database error: {e}")

        except Exception as e:
            db.session.rollback()
            print(e)
            return render_template('register.html',
                                   error=f"An unexpected error occurred during registration. Please try again later.")

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))  # Redirect to secrets

        else:
            flash("Invalid email or password", "error")

    return render_template('login.html')


@app.route('/secrets')
@login_required
def secrets():
    return render_template('secrets.html', username=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/download')
@login_required
def download():
    directory = os.path.join(app.root_path, 'static', 'files')
    filename = 'cheat_sheet.pdf'
    return send_from_directory(
        directory=directory,
        path=filename,
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)
