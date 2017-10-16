from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from models.todo import Todo


app = Flask(__name__)


@app.route("/")
def list():
    """
    Shows list of todo items stored in the database.
    """
    todo_list = Todo.get_all()
    return render_template("index.html", todo_list=todo_list)


@app.route('/add', methods=["POST"])
def add():
    """
    Adds new item to the list.
    """
    name = request.form['name']
    Todo.add(name)
    return redirect(url_for('list'))


@app.route("/remove/<todo_id>")
def remove(todo_id):
    """
    Removes todo item with selected id from the database.
    """
    selected = Todo.get_by_id(todo_id)
    selected.delete()
    return redirect(url_for('list'))


@app.route("/edit/<todo_id>", methods=['POST'])
def edit(todo_id):
    """
    Edits todo item with selected id in the database.
    """
    selected = Todo.get_by_id(todo_id)
    new_name = request.form['new_name']
    selected.update(new_name)
    return redirect(url_for('list'))


@app.route("/toggle/<todo_id>")
def toggle(todo_id):
    """
    Toggles the state of todo item
    """
    selected = Todo.get_by_id(todo_id)
    selected.toggle()
    return redirect(url_for('list'))


if __name__ == "__main__":
    app.run()
