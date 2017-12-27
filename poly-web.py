from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route("/")
def status_screen():
    time_string = datetime.datetime.now().isoformat()
    templateData = {
        'name' : 'PolyBot',
        'time' : time_string
        }
    return render_template('status.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

