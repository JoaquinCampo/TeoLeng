import re
import sys

def prog (texto):

    ret = []

    match = re.findall(r'"tag": "(.*)",\s*"patterns": \[[\s\S]([\s\S]*?)\s*\],\s*"responses": \[\s*([\s\S]*?)\s*\]', texto)

    for i in match:
        ret.append(i[0] + ' ' + str(len(re.findall(r'"([^\n]*)',i[1]))) + ' ' + str(len(re.findall(r'"([^\n]*)',i[2]))))

    ret = '\n'.join(ret)

    return f"{ret}"

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
