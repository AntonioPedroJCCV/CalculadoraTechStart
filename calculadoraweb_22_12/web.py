from flask import Flask
from main import soma, subtracao, multiplicacao, divisao

app = Flask(__name__)

@app.route('/')
def index():
    h1 = '<h1> Calculadora Olist </h1>'
    ol = '''
            <ol> 
                <li><a href='/soma'>Somar</a></li>
                <li><a href='/subtracao'>Subtrair</a></li>
                <li><a href='/multiplicacao'>Multiplicar</a></li>
                <li><a href='/divisao'>Dividir</a></li> 
            </ol>
        '''
    return f'{h1} {ol}'

@app.route('/soma')
def somar():
    n1 = 5.0
    n2 = 5.0
    resultado = soma(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> O resultado de 5 + 5 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/subtracao')
def subtrair():
    n1 = 10.0
    n2 = 5.0
    resultado = subtracao(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> O resultado de 10 - 5 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/multiplicacao')
def multiplicar():
    n1 = 4.0
    n2 = 4.0
    resultado = multiplicacao(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> O resultado de 4 x 4 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

@app.route('/divisao')
def dividir():
    n1 = 6.0
    n2 = 2.0
    resultado = divisao(n1, n2)
    h1 = '<h1> Calculadora </h1>'
    h3 = f'<h3> O resultado de 6 / 2 é : {resultado}</h3>'
    voltar = "<a href='/'>Voltar</a>"

    return f'{h1} {h3} <br /> {voltar}'

app.run()