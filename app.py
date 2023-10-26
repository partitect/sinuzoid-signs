from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/frekans')
def frekans():
    return render_template('frekans.html')


@app.route('/arrange')
def arrange():
    return render_template('arrange.html')


@app.route('/resultfreqency', methods=['GET', 'POST'])
def resultfreqency():
    if request.method == 'POST':
        frekans = request.form.get("frekans")
        genlik = request.form.get("genlik")
        ornek_sayisi = request.form.get("ornek_sayisi")

        if frekans is not None and genlik is not None and ornek_sayisi is not None:
            frekans = float(frekans)
            genlik = float(genlik)
            ornek_sayisi = int(ornek_sayisi)

            zaman = np.linspace(0, 1, ornek_sayisi)
            sinuzoid = genlik * np.sin(2 * np.pi * frekans * zaman)

            plt.figure(figsize=(8, 4), dpi=100)
            plt.plot(zaman, sinuzoid, lw=2)
            plt.title(
                f"Sinüzoidal İşaret - Frekans: {frekans} Hz, Genlik: {genlik}")
            plt.xlabel("Zaman (saniye)")
            plt.ylabel("Genlik")
            plt.grid(True)
            plt.savefig("static/sinuzoid-frequency.png")
            plt.close()

            return render_template("resultfreqency.html", image="static/sinuzoid-frequency.png")


@app.route('/resultarrange', methods=['GET', 'POST'])
def resultarrange():
    if request.method == 'POST':
        x1 = request.form.get("x1")
        x2 = request.form.get("x2")
        if x1 is not None and x2 is not None:
            x1 = float(x1)
            x2 = float(x2)
            # x1'den x2'ye kadar olan aralığı oluşturun
            x = np.arange(x1, x2+1)
            # x'e karşılık gelen işareti tanımlayın. Örnek olarak, bu işaret x'in karesidir.
            y = x**2
            plt.figure(figsize=(8, 4))
            plt.plot(x, y, lw=2)
            plt.title(
                f"Sinüzoidal İşaret - x1: {x1} Hz, x2: {x2}")
            plt.xlabel("x")
            plt.ylabel("İşaret Değeri")
            plt.grid(True)
            plt.savefig("static/sinuzoid-arrange.png")
            plt.close()

            return render_template("resultarrange.html", image="static/sinuzoid-arrange.png")
