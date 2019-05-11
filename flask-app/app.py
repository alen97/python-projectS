# -*- coding: <utf-8> -*-

from flask import Flask
from flask import Response
from flask import request
import mylib 

#from waitress import serve
#import threading

app = Flask(__name__)

########################################
### Páginas. Un método y ruta definida por página, agregar manualmente.

# Main (Home)
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def main():
    my_response = Response(response="Web Server Personal", status=200, mimetype="text/plain")
    my_response.headers["Content-Type"] = "text/plain; charset=utf-8"
    return my_response

# About
@app.route("/about", methods=['GET'])
def get_about():

    my_response = Response(response="ÉSTA ES MI PRIMER WEB APP CON FLASK", status=200, mimetype="text/plain")
    my_response.headers["Content-Type"] = "text/plain; charset=utf-8"

    return my_response

# Contact
@app.route("/contact", methods=['GET'])
def get_contact():

    my_response = Response(response="gabrielgna97@gmail.com", status=200, mimetype="text/plain")
    my_response.headers["Content-Type"] = "text/plain; charset=utf-8"

    return my_response


##########################################
### Manejo de errores

# URL incorrecta (Si el link fue tipeado con mayúsculas/minúsculas lo valida igual)
@app.errorhandler(404)
def url_incorrecta(error):

    # Agregar páginas manualmente. Setear ruta con la IP que se quiera usar.

    if(request.base_url.lower() == "http://localhost:8080/home"):
        return main()
    
    if(request.base_url.lower() == "http://localhost:8080/about"): 
        return get_about()

    if(request.base_url.lower() == "http://localhost:8080/contact"):
        return get_contact()

    return 'Página inexistente.', 404

###########################################

# Primera ejecución en la app
if __name__ == "__main__":

    #threading.Thread(target=app.run(debug=True, host="0.0.0.0", port=80)).start() # Nuevo thread    
    #serve(app, host='0.0.0.0', port=80, url_scheme='http') # Run con Waitress

    app.run(host="0.0.0.0", port=8080) # Run normal


# https://stackoverflow.com/questions/29251004/rewrite-a-url-with-flask
# https://stackoverflow.com/questions/14343812/redirecting-to-url-in-flask

