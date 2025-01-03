from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('officials.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        state = request.form['state']
        district = request.form['district']
        block = request.form['block']
        
        conn = get_db_connection()
        officials = conn.execute('SELECT * FROM officials WHERE state = ? AND district = ? AND block = ?',
                                 (state, district, block)).fetchall()
        conn.close()
        return render_template('search.html', officials=officials)
    
    return render_template('search.html', officials=[])

@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    if request.method == 'POST':
        state = request.form['state']
        district = request.form['district']
        block = request.form['block']
        name = request.form['name']
        position = request.form['position']
        contact = request.form['contact']
        notes = request.form['notes']
        
        conn = get_db_connection()
        conn.execute('INSERT INTO officials (state, district, block, name, position, contact, notes) VALUES (?, ?, ?, ?, ?, ?, ?)',
                     (state, district, block, name, position, contact, notes))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    
    return render_template('contribute.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)