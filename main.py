from focus import read_flowers_data, plot_watering_intervals, add_flowers_from_txt_to_database
from flowers.flowers import add_flower, remove_all, remove_one, show_one
from flask import Flask, render_template, send_from_directory, request, redirect, url_for, send_from_directory
from db import get_connection
import os

app = Flask(__name__)

@app.route('/')
def index():
    flowers_data = read_flowers_data("flowers_data.txt")
    plot_watering_intervals(flowers_data)
    return render_template('index.html', flowers=flowers_data)

@app.route('/plot')
def plot_image():
    return send_from_directory('.', 'watering_intervals.png')

@app.route('/search')
def search():
    return render_template('search.html')

@app.route('/search_one')
def search_one():
    query = request.args.get("flower_name")

    flower_data = None
    if query:
        flower_data = show_one(query)

    return render_template("search.html", query=query, flower_data=flower_data)

@app.route('/dbflowers')
def db_flowers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT flowerid, namn, bildlank, beskrivning FROM flowers")
    rows = cursor.fetchall()

    flowers = []
    for row in rows:
        flowers.append({
            "flowerid": row[0],
            "namn": row[1],
            "beskrivning": row[3]
        })

    conn.close()

    return render_template("db_flowers.html", flowers=flowers)

@app.route('/add_txt', methods=['POST'])
def add_txt():
    add_flowers_from_txt_to_database()
    return redirect(url_for('db_flowers'))

@app.route('/remove_all', methods=['POST'])
def remove_all_flowers():
    remove_all()

    return redirect(url_for('db_flowers'))

@app.route('/remove_one', methods=['POST'])
def remove_one_flower():
    flower_id_to_remove = request.form.get('flowerid')

    if flower_id_to_remove:
        remove_one(flower_id_to_remove)

    return redirect(url_for('db_flowers'))

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        flowerid = request.form['flowerid']
        namn = request.form['namn']
        bildlank = request.form['bildlank']
        beskrivning = request.form['beskrivning']

        add_flower(flowerid, namn, bildlank, beskrivning)
        return redirect(url_for('db_flowers'))

    return render_template('add_flower.html')

if __name__ == "__main__":
    app.run(debug=True)
