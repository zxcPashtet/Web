from flask import Flask, render_template, redirect
from Data import db_session
from Data.users import User
from Data.jobs import Jobs
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'zxcmodePashtet'


def add_users():
    user = User()
    user.surname = 'Scott'
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.speciality = 'research engineer'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user2 = User()
    user2.surname = 'Pivikov'
    user2.name = 'Pasha'
    user2.age = 16
    user2.position = 'creator'
    user2.speciality = 'programmist'
    user2.address = 'himik'
    user2.email = 'pavel.pivikov2008@yandex.ru'
    db_sess.add(user2)
    db_sess.commit()

    user3 = User()
    user3.surname = 'Korunov'
    user3.name = 'Petya'
    user3.age = 16
    user3.position = 'subordinate'
    user3.speciality = 'cleaner'
    user3.address = 'Tverskaya1'
    user3.email = 'petya@ya.ru'
    db_sess.add(user3)
    db_sess.commit()

    user4 = User()
    user4.surname = 'Adrenov'
    user4.name = 'Kostya'
    user4.age = 21
    user4.position = 'subordinate'
    user4.speciality = 'cleaner'
    user4.address = 'Polevaya'
    user4.email = 'kostya@ya.ru'
    db_sess.add(user4)
    db_sess.commit()


def add_jobs():
    job = Jobs()
    job.team_leader = 3
    job.job = 'filling the foundation'
    job.work_size = 42
    job.collaborators = '3, 4'
    job.start_date = datetime.date.today()
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()


@app.route('/')
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return render_template('table_jobs.html', jobs=jobs)


def main():
    db_session.global_init('db/baza.db')
    app.run()
    #add_users()
    #add_jobs()


if __name__ == '__main__':
    main()