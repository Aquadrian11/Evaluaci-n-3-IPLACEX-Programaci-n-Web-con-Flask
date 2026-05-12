from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta principal: Menú
@app.route('/')
def index():
    return render_template('index.html')


# Ruta Ejercicio 1: Cálculo de Notas

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Capturamos las notas en formato decimal (escala 1.0 - 7.0)
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        # Cálculo del promedio chileno
        promedio = (nota1 + nota2 + nota3) / 3

        # Aplicamos la exigencia chilena: Nota >= 4.0 y Asistencia >= 75%
        if promedio >= 4.0 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template('ejercicio1.html', promedio=round(promedio, 1), estado=estado)

    return render_template('ejercicio1.html')


# Ruta Ejercicio 2: Nombres
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        # Encontramos el nombre más largo usando la función max con la clave 'len'
        nombre_mas_largo = max(nombres, key=len)
        longitud = len(nombre_mas_largo)

        return render_template('ejercicio2.html', nombre_largo=nombre_mas_largo, longitud=longitud)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)