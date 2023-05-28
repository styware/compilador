import re
from analizador_sintactico import analizador_sintactico
from realizar_operacion import realizar_operacion

operadores = {
    '+': 'suma',
    '-': 'resta',
    '*': 'multiplicacion',
    '/': 'division',
    '=': 'asignacion',
    '>': 'mayor',
    '<': 'menor'
}
operadores_key = operadores.keys()

tipo_dato = {
    'int': 't_entero',
    'float': 't_flotante',
    'texto': 't_texto'
}
tipo_dato_key = tipo_dato.keys()

simbolos = {
    '!': 'fin'
}
simbolos_key = simbolos.keys()

archivo = open('comando.txt')

def analizador_lexico(codigo_fuente):
    codigo = codigo_fuente.split('\n')
    tokens = []

    l = 1
    for linea in codigo:
        tokens_linea = re.findall(r'([a-zA-Z]+|\d+\.\d+|\d+|\S)', linea)

        print('Listado de token ', tokens_linea)
        token_linea_actual = []

        for token in tokens_linea:

            if token in tipo_dato_key:
                token_linea_actual.append((token, tipo_dato[token]))

            elif token in operadores_key:
                token_linea_actual.append((token, operadores[token]))

            elif re.match(r'^[a-zA-Z]\w*$', token):
                token_linea_actual.append((token, 'identificador'))

            elif re.match(r'^\d+(\.\d+)?$', token):
                token_linea_actual.append((token, 'numero'))

            elif token in simbolos_key:
                token_linea_actual.append((token, simbolos[token]))

            else:
                print('Token no válido: ', token)
                return

        tokens.append(token_linea_actual)

        # if len(tokens_linea) == 0:
        #     tokens.pop(l - 1) 
        #     l -= 1

        # l += 1

    return tokens


codigo_fuente = archivo.read()

if __name__ == '__main__':

    tokens = analizador_lexico(codigo_fuente)
    sintaxis = analizador_sintactico(tokens)
    if(sintaxis):
        realizar_operacion(tokens)
