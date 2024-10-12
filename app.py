# app.py

from flask import Flask, render_template
import logging
import threading
import wids  # Import the WIDS module to start sniffing

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='rogue_aps.log', level=logging.INFO)

@app.route('/')
def index():
    with open('rogue_aps.log', 'r') as f:
        logs = f.readlines()
    return render_template('index.html', rogue_aps=logs)

def run_flask():
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    # Start the Flask application
    run_flask()
    # Start sniffing in the same thread
    wids.start_sniffing()
