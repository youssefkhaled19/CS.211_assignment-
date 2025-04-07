LETTER = 0
DIGIT = 1
UNKNOWN = 99
EOF = -1

INT_LIT = 10
IDENT = 11
ASSIGN_OP = 20
ADD_OP = 21
SUB_OP = 22
MULT_OP = 23
DIV_OP = 24
LEFT_PAREN = 25
RIGHT_PAREN = 26
SEMICOLON = 27
KEYWORD_INT = 28
KEYWORD_DOUBLE = 29
KEYWORD_WHILE = 30

charClass = None
lexeme = ""
nextChar = ""
lexLen = 0
nextToken = None
input_data = "int youssef = 61; double int ahmed = 21; while(1);"
index = 0

def addChar():
    global lexeme, lexLen
    if lexLen <= 98:
        lexeme += nextChar
    else:
        print("Error - lexeme is too long")

def getChar():
    global nextChar, charClass, index
    if index < len(input_data):
        nextChar = input_data[index]
        index += 1
        if nextChar.isalpha():
            charClass = LETTER
        elif nextChar.isdigit():
            charClass = DIGIT
        else:
            charClass = UNKNOWN
    else:
        charClass = EOF

def getNonBlank():
    global nextChar
    while nextChar.isspace():
        getChar()

def lookup(ch):
    global nextToken
    operators = {'+': ADD_OP, '-': SUB_OP, '*': MULT_OP, '/': DIV_OP,
                 '(': LEFT_PAREN, ')': RIGHT_PAREN, ';': SEMICOLON, '=': ASSIGN_OP}
    addChar()
    nextToken = operators.get(ch, EOF)
    return nextToken

def checkKeyword():
    global nextToken
    keywords = {'int': KEYWORD_INT, 'double': KEYWORD_DOUBLE, 'while': KEYWORD_WHILE}
    nextToken = keywords.get(lexeme, IDENT)

def lex():
    global lexeme, nextToken, lexLen
    lexeme = ""
    lexLen = 0
    getNonBlank()

    if charClass == LETTER:
        addChar()
        getChar()
        while charClass in [LETTER, DIGIT]:
            addChar()
            getChar()
        checkKeyword()

    elif charClass == DIGIT:
        addChar()
        getChar()
        while charClass == DIGIT:
            addChar()
            getChar()
        nextToken = INT_LIT

    elif charClass == UNKNOWN:
        lookup(nextChar)
        getChar()

    elif charClass == EOF:
        nextToken = EOF
        lexeme = "EOF"

    print(f"Next token is: {nextToken}, Next lexeme is '{lexeme}'")
    return nextToken

def main():
    global input_data, index
    index = 0
    getChar()

    while nextToken != EOF:
        lex()

if __name__ == "__main__":
    main()
