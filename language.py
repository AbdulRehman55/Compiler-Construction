import argparse
import re
from token import Token


def main():
    #### parsing the command line arguement for file to compile #####
    # file=parseArguements()
    # tokenzing the selected file #########

    file = parseArguements()
    tokenize(file)


# parsing the cmd arguement passed ###########
def parseArguements():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, default="",
                        help="file to compile")
    args = vars(parser.parse_args())
    file=open(args['f'],'rb')
    return file


def tokenize(fileToParse):
    listofTokens = []
    lineNumber = 1
    temp = ""
    index = 1
    string = False;
    character = fileToParse.read(1)
    while character:
        if '#' in temp and character.decode("utf-8") != '\r' and temp[0] != '"':
            pass
        elif character.decode("utf-8") == '\r':
            if len(str(temp)) > 0 and '#' not in temp and '"' in temp:
                token = Token(temp, temp, lineNumber)
                listofTokens.append(token)
            temp = ""
            lineNumber += 1
        elif character.decode("utf-8").isdigit():
            temp += character.decode("utf-8")

        elif character.decode("utf-8") == '\n':
            if len(str(temp)) > 0:
                token = Token(temp, temp, lineNumber)
                temp = ""
                listofTokens.append(token)


        elif character.decode("utf-8") == '\t':
            if len(str(temp)) > 0:
                token = Token(temp, temp, lineNumber)
                temp = ""
                listofTokens.append(token)

        elif character.decode("utf-8").isspace():
            if '#' not in temp:
                if '"' in temp or "'" in temp:
                    temp += character.decode("utf-8")
                elif len(str(temp)) > 0:
                    token = Token(temp, temp, lineNumber)
                    temp = ""
                    listofTokens.append(token)


        elif character.decode("utf-8") in listOfOperators:
            if '#' not in temp:
                pass
                if '"' in temp or "'" in temp:
                    temp += character.decode("utf-8")

                ############# for  + and ++ operator #############
                elif character.decode("utf-8") == '+':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '+' or nextt == '=':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)

                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)


                ############# for  - and -- operator #############
                elif character.decode("utf-8") == '-':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)

                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '-' or nextt == '=':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)

                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)
                        nextt = ""


                ############# for  * and *= operator #############
                elif character.decode("utf-8") == '*':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '=':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)

                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)
                        nextt = ""

                ############# for  / and /= operator #############
                elif character.decode("utf-8") == '/':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)

                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '=':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)

                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)
                        nextt = ""

                ############# for  & and && operator #############
                elif character.decode("utf-8") == '&':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)

                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '&':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)

                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        # temp = nextt
                        listofTokens.append(token1)
                        nextt = ""

                ############# for  | and || operator #############
                elif character.decode("utf-8") == '|':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '|':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)
                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)
                        nextt = ""

                ############# for  = and == operator #############
                elif character.decode("utf-8") == '!' or character.decode("utf-8") == '=':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '=':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)
                        temp = ""
                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)
                        nextt = ""

                ############# for  > , >= and <, <= operator #############
                elif character.decode("utf-8") == '>' or character.decode("utf-8") == '<':
                    if len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '=':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)
                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)
                        nextt = ""

                ############# for  / and // operator #############
                elif character.decode("utf-8") == '/':
                    if len(str(temp)) > 0:
                        if '"' in temp or "'" in temp:
                            temp += character.decode("utf-8")
                        else:
                            token = Token(temp, temp, lineNumber)
                            listofTokens.append(token)
                            temp = ""

                    temp = character.decode("utf-8")
                    nextt = fileToParse.read(1).decode("utf-8")

                    if nextt == '/':
                        temp += nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)
                        temp = ""

                    else:
                        token1 = Token(temp, temp, lineNumber)
                        temp = nextt
                        listofTokens.append(token1)
                        nextt = ""

                else:
                    if '"' in temp or "'" in temp:
                        temp += character.decode("utf-8")
                    else:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""
                        token1 = Token(character.decode("utf-8"), "", lineNumber)
                        listofTokens.append(token1)


        elif character.decode("utf-8") in listOfPunctutors:
            if '#' not in temp:
                # if temp.count('"') < 2 :
                # 	temp+='"'
                # 	token=Token(temp,temp,lineNumber)
                # 	token.show()
                # 	temp = character.decode("utf-8")
                #
                # elif temp.count('"') == 2 or temp.count("'") == 2:
                # 	token1=Token(temp,temp,lineNumber)
                # 	token1.show()
                # 	temp=""

                ############# for  . and .. operator #############
                if len(temp) == 0 and character.decode("utf-8") == ".":
                    temp = character.decode("utf-8")

                elif character.decode("utf-8") == '.' and "." not in temp:
                    nextt = fileToParse.read(1).decode("utf-8")
                    if nextt == '.':
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = character.decode("utf-8") + nextt
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)
                        temp = ""

                    elif len(temp) > 0 and temp[-1].isdigit() and nextt.isdigit():
                        temp += character.decode("utf-8") + nextt

                    elif nextt != '.':
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = character.decode("utf-8")
                        token1 = Token(temp, temp, lineNumber)
                        listofTokens.append(token1)
                        temp = nextt



                    elif len(str(temp)) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = character.decode("utf-8") + nextt



                elif character.decode("utf-8") == '.' and '.' in temp:
                    token = Token(temp, temp, lineNumber)
                    listofTokens.append(token)
                    temp = character.decode("utf-8")


                elif character.decode("utf-8") == "'":
                    if "'" not in temp:
                        if temp.count('"') > 0:
                            temp += '"'
                            string = True
                            token = Token(temp, temp, lineNumber)
                            listofTokens.append(token)
                        temp = character.decode("utf-8")

                    else:
                        temp += character.decode("utf-8")
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""
                        if len(temp) > 0:
                            temp = '"'
                elif character.decode("utf-8") == '"':
                    if '"' not in temp:
                        temp += character.decode("utf-8")

                    elif len(temp) > 0 and temp.count('"') == 1:
                        temp += character.decode("utf-8")
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""

                elif len(str(temp)) > 0 and character.decode("utf-8") != '.' and character.decode(
                        "utf-8") != "'" and '"' not in temp:
                    token = Token(temp, temp, lineNumber)
                    listofTokens.append(token)
                    token1 = Token(character.decode("utf-8"), character, lineNumber)
                    listofTokens.append(token1)
                    temp = ""

                elif character.decode("utf-8") == ";":
                    if len(temp) > 0:
                        token = Token(temp, temp, lineNumber)
                        listofTokens.append(token)
                        temp = ""
                    token1 = Token(character.decode("utf-8"), character, lineNumber)
                    listofTokens.append(token1)

                elif character.decode("utf-8") != '.' and '"' not in temp:
                    token1 = Token(character.decode("utf-8"), character, lineNumber)
                    listofTokens.append(token1)

                elif "." not in temp:
                    temp += character.decode("utf-8") + nextt
                else:
                    token1 = Token(character.decode("utf-8"), character, lineNumber)
                    listofTokens.append(token1)


        elif character.decode("utf-8") == ignore:
            temp += fileToParse.read(1).decode("utf-8")


        ## checking for comments
        elif character.decode("utf-8") == '#':
            if '"' in temp:
                temp += "#"
            elif temp.count('"') == 2 or '"' not in temp:
                temp = character.decode("utf-8")
        else:
            if '#' not in temp or '"' in temp:
                temp += character.decode("utf-8")

        character = fileToParse.read(1)
        index += 1

    if len(temp) > 0 and '#' not in temp:
        token = Token(temp, temp, lineNumber)
        listofTokens.append(token)
        temp = ""
    fileToParse.close()

    # for i in listofTokens:
    # 	i.show()
    valid_tokens(listOfTokens=listofTokens)


def valid_tokens(listOfTokens):
    Tokens = []
    # Validate through the RE of Identifier
    re_of_id = r"^[_A-Za-z_][A-Za-z0-9]*"
    re_of_float = r'^[+-]?([0-9]+([.][0-9]*)?|[.][0-9]+)$'
    re_of_numbers = r'^([+-]?[1-9]\d*|0)$'
    patt_for_id = re.compile(re_of_id)
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for token in listOfTokens:
        if token.word in listOfPunctutors:
            Tokens.append(Token(token.word, '_', token.lineNumber))
        elif token.word in listOfOperators:
            for key in operators.items():
                for type in key[1]:
                    if type == token.word:
                        Tokens.append(Token(token.word, key[0], token.lineNumber))
        elif re.match(re_of_numbers, token.word):
            Tokens.append(Token(token.word, 'Integer Constant', token.lineNumber))
        elif re.match(re_of_float, token.word):
            Tokens.append(Token(token.word, 'Float Constant', token.lineNumber))
        elif token.word[0] == '"' and token.word[-1] == '"':
            Tokens.append(Token(token.word, 'String Constant', token.lineNumber))

        elif token.word[0] == "'" and token.word[-1] == "'":
            if len(token.word) == 4:
                for eachkey in characters.keys():
                    if eachkey in token.word:
                        Tokens.append(Token(token.word, characters[eachkey], token.lineNumber))
                    else:
                        continue
            else:
                Tokens.append(Token(token.word, 'Invalid Lexeme', token.lineNumber))

        elif re.match(re_of_id, token.word):
            if token.word not in keywords:
                if token.word[0] not in num and token.word[-1] != "_":
                    Tokens.append(Token(token.word, 'Identifier', token.lineNumber))
                else:
                    Tokens.append(Token(token.word, 'Invalid Lexeme', token.lineNumber))
            else:
                for eachkey in keywords.keys():
                    if eachkey == token.word:
                        Tokens.append(Token(token.word, keywords[eachkey], token.lineNumber))
                    else:
                        continue
        else:
            continue

    for token in Tokens:
        token.show()


ignore = '$'
listOfPunctutors = ['(', ')', '{', '}', '[', ']', ';', ':', '.', ',', '..', "'", '"']
listOfOperators = ['+', '-', '/', '*', '%', '=', '!', '==', '&', '|', '!=', '&&', '||', '<', '>', '<=', '>=']
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
    , "<", ">", "=="], "LOP": ["&&", "||", "&", "|"], "NOT": ["!"], "INC/DEC": ["++", "--"]}

characters={'\\n':'New Line Character', '\\t':'Tab Character'}


if __name__ == '__main__':
    main()
