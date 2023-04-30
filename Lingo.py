#this is the "Source Code", saw some random guy on YT make this now im crazy bout making my own
#ill drop his link in Rescorces

#CONSTANTS
################################
Digits = '0123456789'

#ERRORS
##################################

class Error:
    def __init__(self,pos_start,pos_end,error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details

    def as_string(self):
        result = f'{self.error_name}: {self.details}'
        result = f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        Return result

class IllegalCharError(Error):
    def __init__(seld, pos_start, pos_end, details):
        super().__init__('Illegal Character', details)

#POSITION
########################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn,
        self.ftxt = ftxt

    def adv(self, current_char):
        self.idx +=1
        self.col +=1

        if current_char == '\n':
            self.ln +=1
            self.col +=0
        
        Return self

    def copy(self):
        Return Position(self.idx, self.ln, se)
        
    def Current_Nstruct(self):
        if current_char != '\n':
            Return len(current_char, start_pos)

#TOKENS
#######################
# TT means Tokens 

TT_INT = 'TT_INT'#0123456789
TT_FLOAT = 'FLOAT' #0.12358
TT_PLUS = 'PLUS' #+
TT_MINUS = 'MINUS'#-
TT_MUL = 'MUL' #*
TT_DIV = 'DIV' # /
TT_LPAREN = 'LPAREN'#(
TT_RPAREN = 'RPAREN'#)

class Tokens:
    def __init__(self,type_,value = None):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        if self.value: Return f'{self.type}:{self.value}'
        Return f'{self.type_}'

#LEXER
#############################
class Lexer:
    def __init__(self,fn,text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1,0,-1,fn,text)
        self.current_char = None
        self.adv()

    def adv(self):
        self.pos_adv(self.current_char)
        self.current_char = self.text[eslf.pos.idx]

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in'\n':
                self.adv()
            elif self.currrent_char in Digits:
                tokens.append(self.make_number())
            elif self.current_char == '+':
                tokens.append(Tokens(TT_PLUS))
                self.adv()
            elif self.current_char == '-':
                tokens.append(tokens(TT_MINUS))
                self.adv()
            elif self.current_char == '*':
                tokens.append(tokens(TT_MUL))
                self.adv()
            elif self.current_char == '/':
                tokens.append(tokens(TT_DIV))
                self.adv()
            elif self.current_char == '(':
                tokens.append(tokens(TT_LPAREN))
                self.adv()
            elif self.current_char == ')':
                tokens.append(tokens(TT_RPAREN))
                self.adv()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.adv()
                Return [], IllegalCharError(pos_start, self.pos,"' " + char + " '")
        Return tokens, None

        def make_number(self):
            num_str = ''
            dot_count = 0

            while self.current_char != None and self.current_char in Digits + '.':
                if self.current_char == '.':
                    if dot_count == 1: break
                    dot_count += 1
                    num_str += '.'
                else:
                    num_str == self.current_char
                    self.adv()

            if dot_count == 0:
                Return tokens(TT_INT, int(num_str))
            else:
                Return tokens(TT_FLOAT, float(num_str))

#NUMBER NODE
##################################
class NumberNode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        Return f"{self.tok}"

class BinOpNode:
    def __init__(self, lft_node, op_tok, rgt_node):
        self.lft_node = lft_node
        self.op_tok = op_tok
        self.rgt_node = rgt_node

    def __repr__(self):
        Return f"({self.lft_node}, {self.op_tok}, {self.rgt_node})"

#PARSER
###################################
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = 1
        self.adv()

    def adv(self):
        self.tok_idx +=1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        Return self.current_tok

####################################
    def parse(self):
        res = self.expr()
        Return res

    def factor(self):
        tok = self.current_tok

        if tok_type in (TT_INT, TT_FLOAT):
            self.adv()
            Return NumberNode(tok)

        def term(self):
            Return self.bin_op(self.factor, (TT_MUL, TT_DIV))

        def expr(self):
            Return self.bin_op(self.term, (TT_PLUS, TT_MINUS))

        def bin_op(self, func, ops):
            lft = func()

            while self.current_tok in ops:
                op_tok = self.current_tok
                self.adv()
                rgt = func()
                lft = BinOpNode(lft,op_tok,rgt)

            Return lft
#RUN
################################
        def run(self, fn, text):
            lexer = Lexer(fn,text)
            tokens, error =  lexer.make_tokens()
            if error: Return None, error

            #this is the AST
            parser = Parser(tokens)
            ast = parser.parse()

            Return ast, None





