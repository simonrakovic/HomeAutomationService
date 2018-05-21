from flask import Flask, render_template

app = Flask(__name__)


@app.route('/api/status')
def api_status():
    return "disabled"

@app.route('/api/zalivaj/<int:id>/<int:cas>')
def api_zalivaj(id, cas):

    return "done"

@app.route('/api/stop')
def api_ustavi_zalivanje():

    return "done"

@app.route('/')
def index():
    teamplateData = {
        "title": "hello"
    }
    return render_template('index.html', **teamplateData)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
