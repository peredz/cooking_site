from flask import Flask
from data import db_session
from data.users import Jobs, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def finished(bol):
    if bol == 0:
        return 'Is not finished'
    return 'Is finished'


def main():
    db_session.global_init('db/crew.db')
    # db_session.global_init(input())
    db = db_session.create_session()
    jobs = [job for job in db.query(Jobs)]
    filtered_jobs = list()
    for i in jobs:
        if not i.is_finished and i.work_size < 20:
            filtered_jobs.append(f'<Job> {i.job}')
    print(*filtered_jobs, sep='\n')


if __name__ == '__main__':
    main()