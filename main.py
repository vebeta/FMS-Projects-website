from flask import Flask, render_template
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/science_projects.db")
    app.run()


@app.route('/')
def main_page():
    return render_template('home.html', title='Главная')


if __name__ == '__main__':
    main()