from flask import Flask, render_template
import os
import connection as c

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

@app.route('/')
def home():
    database = c.DataBase()
    database.cursor.execute("select * from temperaturas")
    result = database.cursor.fetchall()
    inserObject = []
    columnNames = [column[0] for column in database.cursor.description]

    for record in result:
        inserObject.append(dict(zip(columnNames, record)))
    database.cursor.close()
    return render_template('home.html', data=inserObject)

if __name__ == '__main__':
    app.run(debug=True, port=4000)