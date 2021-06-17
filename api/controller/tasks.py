from flask import Blueprint
from db import get_db

TASKS_BLUEPRINT = Blueprint('tasks', __name__)

@TASKS_BLUEPRINT.route('/api/tasks')
def get_tasks():
    db = get_db()
    cursor = db.cursor()
    results = cursor.execute("select * from tasks").fetchall()
    db.commit()
    return { 'tasks': results[0]['name'] }
