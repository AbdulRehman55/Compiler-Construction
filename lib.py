ignore = '$'
listOfPunctutors = ['(', ')', '{', '}', '[', ']', ';', ':', '.', ',', '..', "'", '"']
listOfOperators = ['+', '-', '/', '*', '%', '=', '!', '==', '&', '|', '!=', '&&', '||', '<', '>', '<=', '>=', '++',
                   '--', '*=', '/=','+=','-=']
keywords = {
    'int': 'Int_DT', 'float': 'Float_DT', 'boolean': 'Boolean_DT', 'word': 'String_DT', 'char': 'Char_DT',
    'for': 'f_loop', 'until': 'w_loop', 'do': 'd_w_loop',
    'if': 'if_branch_st', 'else': 'e_b_st', 'elif': 'elif_st', 'when': 'when_branch_st',
    'yield': 'return_st', 'interrupt': 'break_st', 'resume': 'cont_st',
    'class': 'class', 'abstract': 'abstract_class', 'extends': 'inheritance', 'public': 'acc_mod', 'private': 'acc_mod',
    'virtual': 'v_acc_mod', 'struct': 'oop_struct',
    'this': 'current_inst', 'static': 'static_oop', 'fun': 'function', 'step': 'loop_step', 'in': 'loop_in',
    'void': 'void', 'main': 'main', 'println': 'print_st', 'true': 'Boolean Constant'
    , 'false': 'Boolean Constant', 'super': 'parent_inst',
}
operators = {"PM": ["+", "-"], "MDR": ["*", "/", "%"], "AOP": ["=", "*=", "/="], "ROP": ["!=", "<=", ">="
    , "<", ">", "=="], "LOP": ["&&", "||", "&", "|"], "NOT": ["!"], "INC_DEC": ["++", "--","+=","-="]}

characters = {'\\n': 'New Line Character', '\\t': 'Tab Character'}