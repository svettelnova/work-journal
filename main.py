from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import render_template
import sqlalchemy
import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def createData():
    session = db_session.create_session()
    if session.query(Jobs).count() > 0:
        return
    user = User()
    leader1 = user
    user.surname = "Scott"
    user.name = "Ridley"
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    session.add(user)
    user = User()
    leader2 = user
    user.surname = "Weir"
    user.name = "Andy"
    user.position = "helper of captain"
    user.speciality = "engineer"
    user.address = "module_2"
    user.email = "weir_helper@mars.org"
    session.add(user)
    user = User()
    user.surname = "Wotny"
    user.name = "Mark"
    user.position = "member"
    user.speciality = "board engineer"
    user.address = "module_3"
    user.email = "wotny@mars.org"
    session.add(user)
    user = User()
    leader3 = user
    user.surname = "Sanders"
    user.name = "Teddy"
    user.position = "member"
    user.speciality = "explorer"
    user.address = "module_3"
    user.email = "sanders@mars.org"
    session.add(user)
    # session.commit()

    job = Jobs()
    job.team_leader = leader1
    job.description = 'deployment of residential modules 1 and 2'
    job.start_date = datetime.datetime(2012, 3, 3, 10, 10, 10)
    job.work_size = 15
    job.collaborators = "2, 3"
    job.is_finished = False
    session.add(job)
    job = Jobs()
    job.team_leader = leader2
    job.description = 'Exploration of mineral resources'
    job.start_date = datetime.datetime(2012, 3, 3, 10, 10, 10)
    job.work_size = 15
    job.collaborators = "4, 3"
    job.is_finished = False
    session.add(job)
    job = Jobs()
    job.team_leader = leader3
    job.description = 'Development of a management system'
    job.start_date = datetime.datetime(2012, 3, 3, 10, 10, 10)
    job.work_size = 25
    job.collaborators = "5"
    job.is_finished = False
    session.add(job)
    session.commit()


def main():
    db_session.global_init("mars_explorer.db")
    createData()
    app.run(port=8080, host='127.0.0.1')


@app.route("/")
def index():
    session = db_session.create_session()
    jobs = []
    for job in session.query(Jobs).all():
        jobs.append(job)
    return render_template("work journal.html", jobs=jobs)


if __name__ == '__main__':
    main()
