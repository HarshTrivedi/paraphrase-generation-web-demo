from flask import Flask, render_template, request
app = Flask(__name__)

from main_lib import *
from awesome_print import ap

if app.debug is not True:   
    import logging
    app.logger.setLevel(logging.ERROR)

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


@app.errorhandler(500)
def internal_error(exception):
	app.logger.error(exception)
	error_html = "<html><head><title>Internal Server Error</title></head><body><h1><p>Internal Server Error</p></h1></body></html>"
	return error_html, 500

if __name__ == '__main__':
	app.run(debug=False)