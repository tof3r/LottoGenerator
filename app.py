from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap5

from lotto import generate_draw, paginated_list

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/generate', methods=['POST'])
def generate():
    number_of_draws = request.form.get('number_of_draws') or 1
    use_system = request.form.get('use_system') or False
    max_for_system = request.form.get('max_for_system') or 7
    result_list = generate_draw(int(number_of_draws), bool(use_system), int(max_for_system))
    paginated = paginated_list(result_list, 10)
    return render_template("index.html", result_len=len(result_list), paginated=paginated, pages=len(paginated))


if __name__ == '__main__':
    app.run(debug=True)
    