from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Rota principal que carrega o Front-End (HTML)
@app.route('/')
def home():
    return render_template('index.html')

# Rota da API que recebe o clique do botão "SIM"
@app.route('/aceitou')
def aceitou():
    # Aqui o Python processa a resposta. Você poderia salvar em um banco de dados,
    # enviar um e-mail para você mesmo avisando, etc.
    print("O pedido de namoro foi ACEITO! 🎉") 
    return jsonify({"mensagem": "Não tinha escolha, obrigado por aceitar!"})

if __name__ == '__main__':
    app.run(debug=True)
