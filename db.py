import sqlite3

def add(id):
    connection_obj = sqlite3.connect('DB.db', check_same_thread=False)
    cursor_obj = connection_obj.cursor()
    try:
        cursor_obj.execute("INSERT INTO users (id) VALUES(?)",
                           (id,))
        connection_obj.commit()
        connection_obj.close()
        return True
    except:
        connection_obj.commit()
        connection_obj.close()
        return False

def change(text):
    connection_obj = sqlite3.connect('DB.db', check_same_thread=False)
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute(f'UPDATE mailing SET text = ?', (text,))
    connection_obj.commit()
    connection_obj.close()

def mailing():
    connection_obj = sqlite3.connect('DB.db', check_same_thread=False)
    cursor_obj = connection_obj.cursor()
    text = cursor_obj.execute("SELECT text FROM mailing").fetchall()[0][0]
    connection_obj.commit()
    connection_obj.close()
    return text

def users():
    connection_obj = sqlite3.connect('DB.db', check_same_thread=False)
    cursor_obj = connection_obj.cursor()
    text = cursor_obj.execute("SELECT id FROM users").fetchall()
    connection_obj.commit()
    connection_obj.close()
    return text

def channel_change(text):
    connection_obj = sqlite3.connect('DB.db', check_same_thread=False)
    cursor_obj = connection_obj.cursor()
    cursor_obj.execute(f'UPDATE channel SET accept = ?', (text,))
    connection_obj.commit()
    connection_obj.close()

def channel():
    connection_obj = sqlite3.connect('DB.db', check_same_thread=False)
    cursor_obj = connection_obj.cursor()
    text = cursor_obj.execute(f'SELECT accept FROM channel').fetchall()[0][0]
    connection_obj.commit()
    connection_obj.close()
    return text

