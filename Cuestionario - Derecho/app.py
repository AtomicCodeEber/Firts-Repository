from flask import Flask, render_template, request

app = Flask("Derecho-Constitucional")

@app.route('/')
def inicio():
    return render_template('cuestionario.html')

@app.route('/submit', methods=['POST'])
def enviar_respuestas():
    respuestas_usuario = request.form
    puntaje = 0

    respuestas_correctas = ['a', 'b', 'b', 'c', 'c', 'a', 'd', 'b', 'b']

    for i in range(len(respuestas_correctas)):
        respuesta_correcta = respuestas_correctas[i]
        respuesta_usuario = respuestas_usuario.get(str(i))

        if respuesta_usuario == respuesta_correcta:
            puntaje += 1

    return render_template('resultado.html', puntaje=puntaje)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
