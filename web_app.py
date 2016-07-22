from flask import Flask, render_template, request
app = Flask(__name__)

from main_lib import *
from awesome_print import ap

@app.route('/')
def home():
	equivalent_lines = request.args.get("equivalent_lines")
	if equivalent_lines is not None:
		equivalent_lines = equivalent_lines.strip().split("\n")
		equivalent_lines = map( lambda line: line.strip(),  equivalent_lines)
		fsm_code = get_fsm_code( equivalent_lines)
		fsm_svg = get_svg(fsm_code)
	else:
		fsm_svg = ""
	return render_template('index.html', svg = fsm_svg, equivalent_lines = equivalent_lines)


if __name__ == '__main__':
	app.run(debug=False)