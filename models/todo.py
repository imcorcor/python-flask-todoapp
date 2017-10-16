import sqlite3


class Todo:
    """ Class representing todo item."""

    def __init__(self, id, name, done=int(0)):
        self.name = name
        self.id = id
        self.done = done

    def toggle(self):
        """ Toggles item's state """
        self.done = not self.done
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        params = (int(self.done), self.id)
        query = ("UPDATE todos SET done=? WHERE ID=?")
        c.execute(query, params)
        conn.commit()
        conn.close()

    @classmethod
    def add(cls, name):
        """ Saves new added todo item in database """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        params = (name, int(0))
        query = ("INSERT INTO todos (name, done) values (?, ?)")
        c.execute(query, params)
        conn.commit()
        conn.close()

    def update(self, new_name):
        """ Updates todo item in database """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        params = (new_name, self.id)
        query = ("UPDATE todos SET name=? WHERE ID=?")
        c.execute(query, params)
        conn.commit()
        conn.close()

    def delete(self):
        """ Removes todo item from the database """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        params = (self.id, )
        query = ("DELETE FROM todos WHERE ID =?;")
        c.execute(query, params)
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        cls.Todo = []
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        query = ("SELECT ID, name, done FROM todos;")
        database = c.execute(query)
        for row in database:
            id = row[0]
            name = row[1]
            done = bool(row[2])
            todotask = Todo(id, name, done)
            cls.Todo.append(todotask)
        conn.close()
        return cls.Todo

    @classmethod
    def get_by_id(cls, todo_id):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
        Returns:
            Todo: Todo object with a given id
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        params = (todo_id, )
        query = ("SELECT * FROM todos WHERE ID=?;")
        selected_by_id = c.execute(query, params)
        for atr in selected_by_id:
            id = atr[0]
            name = atr[1]
            done = bool(atr[2])
            selected = Todo(id, name, done)
        return selected
