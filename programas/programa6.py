import re
import sys

def prog (texto):

    texto = re.sub(r'("patterns": \[[\s\S]*?".*")([\s\S]*?)(\s*\],\s*"responses": \[\s*".*")([\s\S]*?)(\s*\])', r'\1\3\5', texto)

    return texto


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
