from flask import Flask, render_template, jsonify

app = Flask(__name__)

import sqlite3
STATSDB = 'stats.db'

@app.route('/')
def fetchStats():
    con = sqlite3.connect(STATSDB)
    stats = []
    cur = con.execute('SELECT * FROM stats ORDER BY points DESC')

    for row in cur:
        stats.append(list(row))
    con.close()
    return jsonify('stats')
