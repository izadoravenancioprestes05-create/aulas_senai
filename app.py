from flask import Flask, request

app = Flask(__name__)

# Serve o formulário HTML ao acessar a raiz
@app.route("/")
def index():
    return open("calculadora.html", encoding="utf-8").read()

# Recebe os dados do formulário e calcula
@app.route("/calcular", methods=["POST"])
def calcular():
    v1 = float(request.form["valor1"])
    v2 = float(request.form["valor2"])
    op = request.form["operacao"]

    operacoes = {
        "soma":           ("+", v1 + v2),
        "subtracao":      ("-", v1 - v2),
        "multiplicacao":  ("×", v1 * v2),
        "divisao":        ("÷", "Erro: divisão por zero" if v2 == 0 else v1 / v2),
    }

    simbolo, resultado = operacoes[op]

    return f"""
    <h1>Resultado</h1>
    <p>{v1} {simbolo} {v2} = <strong>{resultado}</strong></p>
    <a href="/">← Voltar</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
