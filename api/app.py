from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS  # Importa Flask-CORS

app = Flask(__name__)

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'localhost'  # Cambia esto por la dirección de tu servidor MySQL
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'movies_ids'
mysql = MySQL(app)

# Configuración de CORS para permitir solicitudes desde cualquier origen
CORS(app)

@app.route('/')
def index():
    return '¡Hola, mundo!'

@app.route('/peliculas', methods=['GET'])
def getPeliculas():
    try:
        # Conexión a la base de datos y consulta SQL
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM peliculas')
        peliculas = cur.fetchall()
        cur.close()

        # Convertir los resultados en una lista de diccionarios
        resultados = [{'id': pelicula[0], 'nombre': pelicula[1], 'descripcion': pelicula[2],
                       'ranking': pelicula[3], 'url': pelicula[4]} for pelicula in peliculas]
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/solopelis', methods=['GET'])
def soloPeliculas():
    try:
      
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM peliculas where tipo = "pelicula"')
        peliculas = cur.fetchall()
        cur.close()

     
        resultados = [{'id': pelicula[0], 'nombre': pelicula[1], 'descripcion': pelicula[2],
                       'ranking': pelicula[3], 'url': pelicula[4]} for pelicula in peliculas]
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/soloseries', methods=['GET'])
def soloSeries():
    try:
      
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM peliculas where tipo = "serie"')
        peliculas = cur.fetchall()
        cur.close()
       
        resultados = [{'id': pelicula[0], 'nombre': pelicula[1], 'descripcion': pelicula[2],
                       'ranking': pelicula[3], 'url': pelicula[4]} for pelicula in peliculas]
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)})
    
    
    
@app.route('/popular', methods=['GET'])
def popular():
    try:
      
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM peliculas WHERE ranking > 4.3 ORDER BY ranking DESC;')
        peliculas = cur.fetchall()
        cur.close()
       
        resultados = [{'id': pelicula[0], 'nombre': pelicula[1], 'descripcion': pelicula[2],
                       'ranking': pelicula[3], 'url': pelicula[4]} for pelicula in peliculas]
        return jsonify(resultados)
    except Exception as e:
        return jsonify({'error': str(e)})    
    
  
        
if __name__ == '__main__':
    app.run(debug=True)
