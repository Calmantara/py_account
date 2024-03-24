# main app for flask
import os
from flask_migrate import Migrate
from app.main import create_app, db
from app import blueprint

app, config = create_app(env=os.getenv("ENVIRONMENT"))
app.register_blueprint(blueprint=blueprint)
app.app_context().push()

Migrate(app, db)

if __name__ == "__main__":
    # run flask app
    app.run("0.0.0.0", config.APP_PORT, config.DEBUG)
