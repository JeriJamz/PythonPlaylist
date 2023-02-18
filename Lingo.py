import time,sys
def delay_print(z):
    for t in z:
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(.05)
#this is the source code
########################
#CONSTANTS
########################
Digits = '0123456789'

#######################
#ERRORS
#######################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result = f'{self.error_name}: {self.details}'#should return the error name: details
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__('Illegal Character', details)

########################
# POSITION
########################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx  = idx
        self.ln = ln 
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def adv(self, current_char):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1 
            self.col = 0

        return self
    
    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#########################
# TOKENS
##########################
#* Constants for TOKENS
# TT stands for token type


TT_INT = 'TT_INT'#0123456789
TT_FLOAT = 'FLOAT'#.00001
TT_PLUS = 'PLUS'# + 
TT_MINUS = 'MINUS'# - 
TT_MUL = 'MUL'# * 
TT_DIV = 'DIV'# / 
TT_LPAREN = 'LPAREN'# ( 
TT_RPAREN = 'RPAREN'# )


class Tokens:
    def __init__(self,type_,value = None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'#if token has a value it will print the 'type:value'
        return f'{self.type}'#if it doesnt have a value it will print jus the type

############################
#LEXER
############################

class Lexer:#this is what read the text
    def __init__(self,fn, text):
        self.fn = fn
        self.text = text #this makes text and obj of lexer
        self.pos = Position(-1, 0, -1, fn, text)#make sure it doesnt start at a blank space and the code starts to freak out
        self.current_char = None#agains sets everything basically to 0 or -1
        self.adv()

    def adv(self):
        self.pos.adv(self.current_char)
        #below is where the lexer will advance but what stops it from being an infinite loop is the else None
        # current char is linked with adv. and is equal to the pos of the text. 
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None 

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in '\n':#this will check for blank spaces and move on
                self.adv()
            elif self.current_char in Digits:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Tokens(TT_PLUS))#i might have to call it tokens(remember to add the S)
                self.adv()
            elif self.current_char == '-':
                tokens.append(Tokens(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(Tokens(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(Tokens(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(Tokens(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(Tokens(TT_RPAREN))
                self.adv()
            else:# the error
                pos_start = self.pos.copy()
                char = self.current_char
                self.adv()
                return [], IllegalCharError(pos_start, self.pos,"' " + char +" '")

        return tokens, None


    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in Digits + '.':
            if self.current_char == '.':
                if dot_count == 1: break 
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
                self.adv()
            
        if dot_count == 0:
            return Tokens(TT_INT, int(num_str))
        else:
            return Tokens(TT_FLOAT, float(num_str))

###########################
#NUMBER NODE
############################

class NumberNode:
    def __init__(self, tok):
        self.tok = tok
    def __repr__(self):
        return f"{self.tok}"

class BinOpNode:
    def __init__(self, lft_node,op_tok, rgt_node):
        self.lft_node = lft_node
        self.op_tok = op_tok
        self.rgt_node = rgt_node
    
    def __repr__(self):
        return f'({self.lft_node}, {op_tok}, {rgt_node})'

##########################
#PARSER
########################

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens 
        self.tok_idx = 1
        self.adv()

    def adv(self):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

#######################

    def parse(self):
        res = self.expr()
        return res


    def factor(self):
        tok = self.current_tok

        if tok_type in  (TT_INT, TT_FLOAT):
            self.adv()
            return NumberNode(tok)
    
    def term(self):
        return self.bin_op(self.factor, (TT_MUl, TT_DIV))
    
    def expr(self):
        return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

    def bin_op(self, func, ops):
        lft = func()

        while self.current_tok in ops:
            op_tok = self.current_tok
            self.adv()
            rgt = func()
            lft = BinOpNode(lft,op_tok, rgt)

        return lft

############################
#Run
############################

def run(fn, text):
    #this makes tokens
    lexer = Lexer(fn, text)
    tokens, error =  lexer.make_tokens()   
    if error: return None, error

    #this makes the AST
    parser = Parser(tokens)
    ast = parser.parse()

    return ast, None

delay_print('This a go again\n'
'All you can put in is number and (+,*,/,-)'
'dont mind two,\n' 'its a prototype\n')
