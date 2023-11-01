from flask import *
from interpretador import *
from UsarAnalisador import *
from interpretador import *



app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index2.html')

@app.route("/analisar", methods=['POST'])
def analisarLexer():
    codigo = str(request.form.get('code'))
    print(codigo)

    Analyzer = LexicalAnalyzer()
    token = []
    lexeme = []
    row = []
    column = []
    saida = []

    print(codigo.strip().split())
    for i in codigo.split(' '):
        t, lex, lin, col = Analyzer.tokenize(i)
        if(len(t) > 0):
            saida.append(f'Token = {t}, Lexeme = {lex}')
        token += t
        lexeme += lex
        row += lin
        column += col


    return render_template('exibir.html', tokens=saida)



if __name__ == '__main__':
    app.run(port=5050, debug=True)