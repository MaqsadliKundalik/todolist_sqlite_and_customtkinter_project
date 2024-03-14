from sqlite3 import Connection

conn = Connection("data.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS list (id INTEGER PRIMARY KEY, title, description)")
conn.commit()

def add_item(title, description):
    c.execute("INSERT INTO list (title, description) VALUES (?, ?)", (title, description))
    conn.commit()

def del_item(id):
    c.execute("DELETE FROM list WHERE id=?", (id, ))
    conn.commit()

def get_items():
    return c.execute("SELECT id, title, description FROM list").fetchall()

print(get_items())


def close_db():
    conn.close()
