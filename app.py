from flask import Flask, render_template

app = Flask(__name__)  # ← Esta línea debe ir antes de @app.route

@app.route('/')
def carta():
    return render_template('carta.html')
import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

