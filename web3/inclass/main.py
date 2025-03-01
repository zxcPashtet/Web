from flask import Flask, render_template, redirect
from Data import db_session
from Data.users import User
from Data.news import News
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zxcmodePashtet'


def add_users():
    user = User()
    user.name = 'Пользователь1'
    user.about = 'О пользователе 1'
    user.email = 'user1@email.ru'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    user2 = User(
        name='Пользователь2',
        about='О пользователе 2',
        email='user2@email.ru'
    )
    db_sess.add(user2)
    db_sess.commit()


def view_users():
    db_sess = db_session.create_session()
    user = db_sess.query(User).first()
    print(user.name)
    for user in db_sess.query(User).all():
        print(user)
    for user in db_sess.query(User).filter((User.id > 1), (User.about.notlike('%1%'))).all():
        print(user.name)
    for user in db_sess.query(User).filter((User.id > 1) | (User.about.notlike('%1%'))).all():
        print(user.name)


def delete_user():
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == 2).first()
    db_sess.delete(user)
    db_sess.commit()


def delete_users():
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id > 1).delete()
    db_sess.commit()


def add_news():
    db_sess = db_session.create_session()
    new1 = News(
        title='Завтра турнир',
        content='В кабинете 4 состоится',
        user_id=1, is_private=False
    )
    new2 = News(
        title='',
        content='',
        user_id=2
    )
    db_sess.add(new1)
    db_sess.add(new2)
    db_sess.commit()


@app.route('/')
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return render_template('index.html', news=news)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form, message='Пароли не совпадают')
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form, message='Такой пользователь уже есть')
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    db_session.global_init('db/news.db')
    app.run()
    #add_news()
    #view_users()
    #add_users()


if __name__ == '__main__':
    main()