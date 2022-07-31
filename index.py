from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort


def get_db_connection():
    conn = sqlite3.connect('src/database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    post_view = conn.execute('SELECT * FROM posts WHERE id = ?', (post_id,)).fetchone()
    conn.close()
    if post_view is None:
        abort(404)
    return post_view


app = Flask(__name__)  # guardo en una variable la inicialización de Flask


@app.route('/')  # defino una ruta dentro de mi sitio (aquí el root)
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('blog.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post_selected = get_post(post_id)
    return render_template('post.html', post=post_selected)


if __name__ == '__main__':  # verifico que estoy en el main y no en un módulo
    app.run(debug=True)  # método de escucha para el browser
