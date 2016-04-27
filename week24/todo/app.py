from flask import (
    Flask, render_template, request, redirect, url_for
)

from todo import *


app = Flask(__name__)

tasks = []


@app.route('/')
def todos():
    result_tasks = tasks
    completed = 'completed' in request.args
    uncompleted = 'uncompleted' in request.args
    if completed:
        result_tasks = get_completed(result_tasks)
    elif uncompleted:
        result_tasks = get_uncompleted(result_tasks)
    tag = request.args.get('tag')
    if tag:
        result_tasks = filter_by_tag(result_tasks, tag)
    order = request.args.get('order')
    if order == 'priority':
        result_tasks = order_by_priority(result_tasks)
    elif order == 'deadline':
        result_tasks = order_by_deadline(result_tasks)
    return render_template(
        'index.html',
        tasks=result_tasks,
        tags=TAGS,
        priorities=PRIORITIES.keys()
    )


@app.route('/tasks/create', methods=['POST'])
def create():
    add_task(
        tasks,
        request.form['title'],
        request.form['deadline'],
        request.form['priority'],
        request.form.getlist('tags')
    )
    return redirect(url_for('todos'))


@app.route('/tasks/clear', methods=['POST'])
def clear():
    clear_completed(tasks)
    return redirect(url_for('todos'))


@app.route('/tasks/<int:index>/remove', methods=['POST'])
def remove(index):
    remove_task(tasks, index)
    return redirect(url_for('todos'))


@app.route('/tasks/<int:index>/complete', methods=['POST'])
def complete(index):
    complete_task(tasks, index)
    return 'ok'


@app.route('/tasks/<int:index>/uncomplete', methods=['POST'])
def uncomplete(index):
    uncomplete_task(tasks, index)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
