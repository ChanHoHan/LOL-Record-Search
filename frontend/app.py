from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def main():
    if request.method == 'GET':
        return render_template('home.html')

@app.route("/api", methods = ['POST'])
def api():
    if request.method == 'POST':
        result = request.form
        print(dict(result))
        return render_template("record.html", result = dict(result)['Name'])

if __name__ == "__main__":
    app.run()
