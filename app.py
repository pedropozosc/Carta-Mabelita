from flask import Flask, render_template

app = Flask(__name__)  # ← Esta línea debe ir antes de @app.route

@app.route('/')
def carta():
    return render_template('carta.html')

if __name__ == '__main__':
    app.run(debug=True)
