from flask import Flask, render_template, jsonify, Response
from flask_cors import CORS
import principal


app= Flask(__name__)
CORS(app)
PORT= 5000
DEBUG=True


@app.errorhandler(404)
def not_found (error):
    return "Not found"

@app.route('/', methods=['GET'])
def index ():
    return '''<ul>
        <li>Endpoint para anuncios de tabla oferta: /api/oferta </li>
        <li>Endpoint para especialidades de tabla keyword_search: /api/keyword </li>
        <li>Endpoint para portales escrapeados de tabla webscraping: /api/webscraping </li>
        <li>Endpoint para estadisticas de las especialidades : /api/piechart </li>
        <li>Endpoint para data csv de las especialidades : /data_csv/keyword_name </li>
        <li>Endpoint para iniciar el webscraping ¡¡No tocar :u!!: /start </li>
        </ul>'''

@app.route('/api/oferta', methods=['GET'])
def api_all():
    avisoresponse=[]
    listavisos= principal.listarAvisoDeOferta()
    for aviso in listavisos:
        anuncio = {
            'id': aviso[0],
            'id_webscraping': aviso[1],
            'titulo': aviso[2],
            'empresa': aviso[3],
            'lugar':aviso[4],
            'tiempo_publicado':aviso[5],
            'salario': aviso[6],
            'url_oferta': aviso[9],
            'url_pagina':aviso[10],
            'area' : aviso[11],
            'oferta_detalle': aviso[14],
            'time_publicacion': aviso[16],
            'id_anuncioempleo': aviso[17]
        }
        avisoresponse.append(anuncio)
    return jsonify(avisoresponse)

@app.route('/api/webscraping', methods=['GET'])
def listarPortalesWebscraping ():
    webscraping=[]
    listapaginasweb= principal.listarPaginasWeb()
    for lista in listapaginasweb: 
        response = {
            'id_webs' : lista[0],
            'busqueda' : lista[1],
            'pagina_web': lista[3],
            'url_pagina': lista[4],
            'url_busqueda': lista[5],
            'fecha_creacion': lista[6],
            'fecha_modificacion': lista[7],
        }
        webscraping.append(response)

    return jsonify(webscraping)

@app.route('/api/keyword', methods= ['GET'])
def listarKeyword():
    keyword=[]
    keywordsearch= principal.listarPalabras()
    for pal in keywordsearch:
        response = {
            'id': pal[0],
            'palabra' : pal[1]
        }
        keyword.append(response)
    return jsonify(keyword)

@app.route('/api/piechart', methods=['GET'])
def obtenerEstadisticasPiecharm():
    response=[]
    estadistic= principal.estaditicasEspecialidades()
    for res in estadistic:
        metrica = {
            'especialidad': res[0] ,
            'cantidad': res[1],
            'mes': res[3]
        }
        response.append(metrica)
    print(response)
    return jsonify(response)

@app.route('/data_csv/<string:especialidad>', methods=['GET'])
def get_data(especialidad=None):
    data=""
    datostotales= principal.get_data_fechas(especialidad)
    for d in datostotales:
        csv = str(d[0])+","+str(d[1])+'\n'
        data=data+csv
    return Response(data)

@app.route('/api/data_proyecciones', methods=['GET'])
def proyecciones():
    response=[]
    proyeccion= principal.get_proyecciones()
    for res in proyeccion:
        proy = {
            'especialidad': res[0] ,
            'cantidad': res[1],
            'fecha': res[2]
        }
        response.append(proy)
    print(response)
    return jsonify(response)

@app.route('/start' ,methods=['GET'])
def webscraping():
    principal.webscraping_sd()
    return "iniciando webscraping"

if __name__=="__main__":
    app.run(port=PORT, debug=DEBUG)