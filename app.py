from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'rahasia123'  # Untuk session

@app.route("/", methods=["GET", "POST"])
def tebak_angka():
    if 'angka_rahasia' not in session:
        session['angka_rahasia'] = random.randint(1, 10)

    message = None

    if request.method == "POST":
        try:
            tebakan = int(request.form['tebakan'])
            angka_rahasia = session['angka_rahasia']

            if tebakan < angka_rahasia:
                message = "Terlalu kecil!"
            elif tebakan > angka_rahasia:
                message = "Terlalu besar!"
            else:
                message = "Selamat! Kamu benar! Game direset."
                session.pop('angka_rahasia')

        except ValueError:
            message = "Masukkan angka yang valid!"

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
