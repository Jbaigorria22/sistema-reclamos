from flask import Flask, render_template, request, redirect, url_for, session
from database import get_connection, crear_tabla, crear_tabla_usuarios
from functools import wraps

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Crear tablas al iniciar
crear_tabla()
crear_tabla_usuarios()


# ==========================
# LOGIN REQUIRED DECORATOR
# ==========================
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function


# ==========================
# LOGIN
# ==========================
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM usuarios WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("inicio"))

    return render_template("login.html")


# ==========================
# LOGOUT
# ==========================
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# ==========================
# INICIO
# ==========================
@app.route("/")
@login_required
def inicio():
    return render_template("inicio.html")


# ==========================
# NUEVO RECLAMO
# ==========================
@app.route("/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_reclamo():

    if request.method == "POST":

        nombre = request.form["nombre"]
        direccion = request.form["direccion"]
        tipo = request.form["tipo"]
        descripcion = request.form["descripcion"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO reclamos (nombre, direccion, tipo, descripcion, estado)
            VALUES (?, ?, ?, ?, 'Pendiente')
        """, (nombre, direccion, tipo, descripcion))

        conn.commit()
        conn.close()

        return redirect(url_for("ver_reclamos"))

    return render_template("nuevo_reclamo.html")


# ==========================
# VER RECLAMOS
# ==========================
@app.route("/reclamos")
@login_required
def ver_reclamos():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reclamos")
    reclamos = cursor.fetchall()

    conn.close()

    return render_template("ver_reclamos.html", reclamos=reclamos)


# ==========================
# RUN
# ==========================
if __name__ == "__main__":
    app.run(debug=True)
