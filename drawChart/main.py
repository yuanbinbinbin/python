
from flask import Flask, render_template, current_app
from view import pc


if __name__ == '__main__':
	web_index = Flask(__name__)
	web_index.register_blueprint(pc, url_prefix='/pc')
	web_index.run(host='192.168.3.196',port=8080)