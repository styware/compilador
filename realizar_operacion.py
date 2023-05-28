def realizar_operacion(tokens:list):
    
    for token in tokens:
        if len(token) == 7:
            # print(token)
            if token[1][0] == '+':
                print(float(token[0][0]) + float(token[2][0]))
            elif token[1][0] == '-':
                print(float(token[0][0]) - float(token[2][0]))
            