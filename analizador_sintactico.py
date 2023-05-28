def analizador_sintactico(tokens: list):
    # print('tupla de tokens: ',tokens)
    # print(lineas_codigo)

    if not tokens:
        print('La lista de tokens esta vacia.')
        return False

    l = 1
    variables = []

    for token in tokens:
        # print(token)
        if len(token) == 0:
            pass

        elif len(token) == 3:
            if not token[0][1] == 't_entero' and not token[0][1] == 't_flotante' and not token[0][1] == 't_texto':
                print(l, ' - ', 'Primero se debe definir un tipo de dato.')
                return False

            if not token[1][1] == 'identificador':
                print(l, ' - ', 'No se creo una variable correctamente.')
                return False

            if not token[2][1] == 'fin':
                print(l, ' - ', 'Falta el simbolo ! al final de la linea')
                return False

            variable = token[1][0]

            if variable in variables:
                print(l, ' - ', f'la variable {variable} ya fue definida.')
                return False
            else:
                variables.append(variable)

        elif len(token) == 7:

            if not token[0][1] == 'numero':
                print(l, ' - ', 'Verifique el numero de la operacion.')
                return False

            if not token[1][1] == 'suma' and not token[1][1] == 'resta' and not token[1][1] == 'multiplicacion' and not token[1][1] == 'division':
                print(l, ' - ', 'Verifique el simbolo de la operacion.')
                return False

            if not token[2][1] == 'numero':
                print(l, ' - ', 'Verifique el numero de la operacion.')
                return False

            if not token[3][1] == 'asignacion':
                print(l, ' - ', 'Verifique la asignacion.')
                return False

            if not token[4][1] == 'mayor':
                print(l, ' - ', 'Primero se debe definir un tipo de dato.')
                return False

            if not token[5][1] == 'identificador':
                print(l, ' - ', 'No se creo una variable correctamente.')
                return False
            else:
                if token[5][0] not in variables:
                    print(l, ' - ', 'Esta variable no esta definida.')
                    return False

            if not token[6][1] == 'fin':
                print(l, ' - ', 'Falta el simbolo ! al final de la linea')
                return False

        else:
            print("La linea ", l, ' no satisface los requerimientos')
            return False
        l = l + 1
    # print(variables)
    return True
