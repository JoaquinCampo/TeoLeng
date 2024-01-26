# -*- coding: utf-8 -*-

import sys
import io
import nltk


# grammar definition
grammar = """

FUNCION -> 'def' F '(' V ')' ':' '{' CODIGO '}' | 'def' F '(' V ')' ':' '{' '}'

CODIGO -> INST CODIGO | INST

INST ->  ASIG ';' | LLAMAR_FUNC ';' | IF | WHILE | FOR | 'return' SENT ';'

LOOP -> IF | FOR | WHILE

IF -> 'if' BOOL ':' '{' CODIGO '}' 'else' ':' '{' CODIGO '}' | 'if' BOOL ':' '{' CODIGO '}' | 'if' BOOL ':' 'return' SENT ';' 'else' ':' 'return' SENT ';' | 'if' BOOL ':' CODIGO

WHILE -> 'while' BOOL ':' '{' CODIGO '}'

FOR -> 'for' V 'in' 'range' '(' SENT ')' ':' '{' CODIGO '}' | 'for' V 'in' 'range' '(' SENT ')' ':' LOOP | 'for' V 'in' 'range' '(' SENT ',' SENT ')' ':' '{' CODIGO '}' | 'for' V 'in' 'range' '(' SENT ',' SENT ')' ':' LOOP

ASIG -> V '=' SENT

LLAMAR_FUNC -> F '(' SENT ')'

BOOL -> '('BOOL')' | 'not' BOOL | BOOL 'and' BOOL | BOOL 'or' BOOL | SENT '==' SENT | SENT '<''=' SENT | SENT '>''=' SENT | SENT '!''=' SENT | SENT '<' SENT | SENT '>' SENT | 'True' | 'False' | K | V 

SENT -> SENT '+' SENT | SENT '-' SENT | SENT '*' SENT | SENT '/' SENT | SENT'//'SENT |'(' SENT ')'| SENT '*''*' SENT | SENT '%' SENT | K | N | V | LLAMAR_FUNC

V -> VAR | VAR '[' SENT']' | ':'VAR | VAR':'
VAR -> 'x0' | 'x1' | 'x2' | 'x3' | 'x4' | 'x5' | 'x6' | 'x7' | 'x8' | 'x9' | 'x10' | 'x' |  'i' | 'j' | 'k' | 'arr' | 'n' | 'left' | 'right' | 'mid'

F -> 'f1' | 'f2' | 'f3' | 'f4' | 'f5' | 'f6' | 'f7' | 'f8' | 'f9' | 'f10' | 'len' | 'range'
K -> 'k1' | 'k2' | 'k3' | 'k4' | 'k5' | 'k6' | 'k7' | 'k8' | 'k9' | 'k10'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100'
"""


def parse(s, grammar):
        
    # parser
    grammar = nltk.CFG.fromstring(grammar)
    parser = nltk.LeftCornerChartParser(grammar)
    
    # tokenize
    s_tokenized = nltk.word_tokenize(s)

    # parse
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s, grammar)
      if tree:
          salida = "PERTENECE"
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO PERTENECE - FUERA DE VOCABULARIO"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()


