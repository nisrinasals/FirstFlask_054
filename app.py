from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form['nama']
    umur = request.form['umur']
    return render_template('submit.html', nama=nama, umur=umur)  # Render ke submit.html dengan data nama & umur

if __name__ == '__main__':
    app.run(debug=True)
