from flask import Flask, render_template, request, redirect, url_for, session
from database import get_connection, crear_tabla, crear_tabla_usuarios
from functools import wraps

app = Flask(__name__)
app.secret_key = "clave_secreta"

# Aseguramos que las tablas existan al arrancar
crear_tabla()
crear_tabla_usuarios()

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect(url_for("index"))
        else:
            # En lugar de un return directo, pasamos el error al template
            error = "Credenciales incorrectas. Intente de nuevo."

    return render_template("login.html", error=error)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/")
@login_required
def index():
    conn = get_connection()
    cursor = conn.cursor()
    total = cursor.execute("SELECT COUNT(*) FROM reclamos").fetchone()[0]
    pendientes = cursor.execute("SELECT COUNT(*) FROM reclamos WHERE estado='Pendiente'").fetchone()[0]
    resueltos = cursor.execute("SELECT COUNT(*) FROM reclamos WHERE estado='Resuelto'").fetchone()[0]
    conn.close()
    return render_template("index.html", total=total, pendientes=pendientes, resueltos=resueltos)

@app.route("/reclamos")
@login_required
def reclamos():
    busqueda = request.args.get("busqueda", "")
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM reclamos WHERE 1=1"
    params = []
    if busqueda:
        query += " AND (dni LIKE ? OR nombre LIKE ? OR direccion LIKE ?)"
        like_val = f"%{busqueda}%"
        params.extend([like_val, like_val, like_val])
    cursor.execute(query, params)
    reclamos_data = cursor.fetchall()
    total = cursor.execute("SELECT COUNT(*) FROM reclamos").fetchone()[0]
    pendientes = cursor.execute("SELECT COUNT(*) FROM reclamos WHERE estado='Pendiente'").fetchone()[0]
    resueltos = cursor.execute("SELECT COUNT(*) FROM reclamos WHERE estado='Resuelto'").fetchone()[0]
    conn.close()
    return render_template("ver_reclamos.html", reclamos=reclamos_data, total=total, pendientes=pendientes, resueltos=resueltos, busqueda=busqueda)

@app.route("/nuevo", methods=["GET", "POST"])
@login_required
def nuevo_reclamo():
    if request.method == "POST":
        dni = request.form["dni"]
        nombre = request.form["nombre"]
        direccion = request.form["direccion"]
        tipo = request.form["tipo"]
        descripcion = request.form["descripcion"]
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reclamos (dni, nombre, direccion, tipo, descripcion, estado) VALUES (?, ?, ?, ?, ?, 'Pendiente')", (dni, nombre, direccion, tipo, descripcion))
        conn.commit()
        conn.close()
        return redirect(url_for("reclamos"))
    return render_template("nuevo_reclamo.html")

@app.route("/resolver/<int:id>")
@login_required
def resolver(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE reclamos SET estado='Resuelto' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for("reclamos"))

if __name__ == "__main__":
    app.run(debug=True)