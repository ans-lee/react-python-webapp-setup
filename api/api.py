from flask import Flask, g
from routes.tasks import TASKS_BLUEPRINT

app = Flask(__name__)
app.register_blueprint(TASKS_BLUEPRINT)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
