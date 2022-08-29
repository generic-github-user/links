from lark import Lark
from lark.indenter import Indenter

class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 2

#parser = Lark(import_paths=['grammar.lark'], parser='lalr', postlex=TreeIndenter())
with open('grammar.lark', 'r') as grammar:
    parser = Lark(grammar.read(), parser='lalr', lexer='contextual', postlex=TreeIndenter(), debug=True)
    #parser = Lark(grammar.read(), parser='earley', lexer='basic', postlex=TreeIndenter())

def parse():
    with open('links.txt', 'r') as f:
        parsed = parser.parse(f.read())
    print(parsed.pretty()[:2000])
    #breakpoint()

    result = ''
    #for tree in parsed.iter_subtrees():
        #print(tree.pretty()[:100])
    #breakpoint()
    print(result)

parse()
