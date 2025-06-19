from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

tarefas = []
contador_id = 1

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", tarefas=tarefas)

@app.route("/add", methods=["POST"])
def add():
    global contador_id
    desc = request.form.get("tarefa")
    if desc:
        tarefas.append({"id": contador_id, "descricao": desc})
        contador_id += 1
    return redirect("/")

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    global tarefas
    tarefas = [t for t in tarefas if t["id"] != id]
    return redirect("/")

@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    nova = request.form.get("nova_tarefa")
    for t in tarefas:
        if t["id"] == id:
            t["descricao"] = nova
            break
    return redirect("/")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)