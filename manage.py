# import model
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship, Session
from model import Base, add_user, create_user_task
import json
from flask.cli import FlaskGroup
from app import app

cli = FlaskGroup(app)

@cli.command('reset-db')
def reset_db():
    # os.remove('app.db')
    engine = create_engine('sqlite:///app.db', echo=True)
    Base.metadata.drop_all()
    Base.metadata.create_all()
    # session = Session(bind=engine)
    # session.query(User).delete()
    # session.commit()
    # Base.metadata.drop_all()
    # print(dir(Base.metadata))

@cli.command('fill-db')
def fill_db():
    with open('MOCK_DATA.json') as f:
        mock = json.load(f)
    for i in mock:
        add_user(**i)

@cli.command('fill-tasks')
def fill_tasks():
    with open('MOCK_DATAtasks.json') as f:
        mock = json.load(f)
    for i in mock:
        create_user_task(**i)

cli()
# fill_db()
# reset_db()