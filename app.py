from flask import Flask, request, render_template

from lotto import generate_draw

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/generate', methods=['POST', 'GET'])
def generate():
    if request.method == 'POST':
        number_of_draws = request.form['number_of_draws']
        use_system = request.form['use_system']
        max_for_system = request.form['max_for_system']
        result_list = generate_draw(int(number_of_draws), eval(use_system), int(max_for_system))
        return render_template("index.html", results=result_list)


if __name__ == '__main__':
    app.run(debug=True)
    