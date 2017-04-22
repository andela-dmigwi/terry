""" Created by Migwi Ndung'u  @April 2017"""
from terry_bot import app
# from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

# migrate = Migrate(app, db)
manager = Manager(app)
# manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
