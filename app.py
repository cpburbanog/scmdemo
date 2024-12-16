import os
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction_28 = None
    prediction_90 = None
    if request.method == 'POST':
        # Captura los datos de entrada desde el formulario
        psd_d50 = float(request.form['psd_d50'])
        n_psd = float(request.form['n_psd'])
        ssa_psd = float(request.form['ssa_psd'])
        density = float(request.form['density'])
        amorphous_phase = float(request.form['amorphous_phase'])
        sio2 = float(request.form['sio2'])
        al2o3 = float(request.form['al2o3'])
        fe2o3 = float(request.form['fe2o3'])
        cao = float(request.form['cao'])
        bound_water = float(request.form['bound_water'])

        # Simula predicciones
        prediction_28 = round(random.uniform(50, 100), 2)
        prediction_90 = round(random.uniform(70, 120), 2)

    return render_template('index.html', prediction_28=prediction_28, prediction_90=prediction_90)

if __name__ == '__main__':
    # Obtener el puerto asignado por Render
    port = int(os.environ.get("PORT", 5000))  # Usa 5000 si PORT no está definido
    app.run(host='0.0.0.0', port=port)

