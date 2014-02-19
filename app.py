from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == 'GET':
        return render_template('hello.html')
    elif request.method == 'POST':
        return render_template('greeting.html',
                               fullname=request.form['fullname'])

if __name__ == "__main__":
    app.run(debug=True)
