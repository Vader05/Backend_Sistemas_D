from flask import Flask, render_template
import principal

app= Flask(__name__)
PORT= 5000
DEBUG=True

@app.errorhandler(404)
def not_found (error):
    return "Not found"

@app.route('/', methods=['GET'])
def index ():
    return "puro mongolito"

@app.route('/sd' ,methods=['GET'])
def webscraping():
    principal.webscraping_sd()
    return "iniciando webscraping"

if __name__=="__main__":
    app.run(port=PORT, debug=DEBUG)