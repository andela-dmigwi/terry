""" Created by Migwi Ndung'u  @April 2017"""
from app import create_app
from app.models import db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
