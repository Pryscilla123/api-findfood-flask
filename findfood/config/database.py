from decouple import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, inspect

db = SQLAlchemy()


def configure_database(app):
    db_url = f'postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}' \
             f'@{config("DB_HOST")}:{config("DB_PORT")}/{config("DB_NAME")}'

    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # engine inspector

    with app.app_context():
        engine = create_engine(db_url)
        inspector = inspect(engine)

        if not inspector.get_table_names():
            db.create_all()
