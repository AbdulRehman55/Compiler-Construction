
import pandas as pd
import regex
import json
import numpy as np
Opr=[]
Types=[]
stack = []
PL=''
CN=''
N=''
AM=''
TM=''
OP=''
CrP=''


fn_table = pd.DataFrame({'Name': [], 'Type': [], 'Scope': []})
Main_table = pd.DataFrame({'Name': [], 'Type': [], 'Parent': [], 'Ref': []})
scope=0
class classbodytable:

    def __init__(self,CN):
        self.CN=CN
        self.Classbodytable = pd.DataFrame({'Name': [], 'Type': [], 'AM': [], 'TM': []})

def lookUpMT(N):
    if(N in Main_table['Name'].values):
        return True
    else:
        return False
def lookupCDT(CN,N,Parent):
    if (CN in Main_table['Name'].values):
        mask = Main_table['Name'] == CN

        df = Main_table[mask]['Ref']
        if (N in df[0].Classbodytable['Name'].values):
            mas=df[0].Classbodytable['Name']==N
            value=df[0].Classbodytable['AM'][mas]

            if(value[0]=='public'):
                    return (df[0].Classbodytable['Type'][mas][0])
            elif(value[0]=='private' or value[0]=='protected'):
                print('cant access private or protected variable')
                return False
        elif(Parent in Main_table['Name'].values):

            mask = Main_table['Name'] == Parent

            df = Main_table[mask]['Ref']
            if (N in df[0].Classbodytable['Name'].values):
                mas = df[0].Classbodytable['Name'] == N
                value = df[0].Classbodytable['AM'][mas]
                if (value[0] == 'public' or value[0] == 'protected'):
                    return (df[0].Classbodytable['Type'][mas][0])
                elif (value[0] == 'private'):
                    print('cant access private or protected variable')
                    return False
                else:
                    print(N + ' is not declared')
                    return False
        else:
            print(N+ ' is not declared')
            return False
def lookupFT(N,PL,CN):
    global fn_table
    global Main_table

    if(N in fn_table['Name'].values):

        mas=fn_table['Name']==N
        df=fn_table[mas]['Scope']

        try:
            if(df[0]==PL):

                return(fn_table[mas]['Type'][0])

            else:
                return False

        except:
            if (df[1] == PL):

                return (fn_table[mas]['Type'][1])

            else:
                return False


    elif (CN in Main_table['Name'].values):
        mask = Main_table['Name'] == CN

        df = Main_table[mask]['Ref']

        if (N in df[0].Classbodytable['Name'].values):
            mas=df[0].Classbodytable['Name']==N
            value=df[0].Classbodytable['AM'][mas]

            if(value[0]=='public'):
                    return (df[0].Classbodytable['Type'][mas][0])
            elif(value[0]=='private' or value[0]=='protected'):
                print('cant access private and protected variables')
                return False

        elif(CrP in Main_table['Name'].values):

            mask = Main_table['Name'] == CrP

            df = Main_table[mask]['Ref']
            if (N in df[0].Classbodytable['Name'].values):
                mas = df[0].Classbodytable['Name'] == N
                value = df[0].Classbodytable['AM'][mas]
                if (value[0] == 'public' or value[0] == 'protected'):
                    return (df[0].Classbodytable['Type'][mas][0])
                elif (value[0] == 'private'):
                    print('cant access private and protected variable')
                    return False
                else:
                    print(N + '  not declared')
                    return False
            else:
                return False
        else:
            print(N+ '  not declared')
            return False


def createscope():
    global scope
    stack.append(scope)
    scope=scope+1
    return scope-1
def deletescope():
    global scope
    scope=stack.pop()
    return scope
def comp2(righttype,T):
    for i in range(len(T)):
        if(T[i]==righttype):
            return righttype

def compatibility(lefttype,righttype,opr):
    if(((((lefttype=='int' and righttype=='float')or(lefttype=='float' and righttype=='int') )or(lefttype == 'float' and righttype == 'float')) and( opr=='+' or opr=='-' or opr=='*'  or opr=='/' )) or ((lefttype == 'float' and (righttype == 'int' or righttype=='float')) and opr == '=')):
        return 'float'
    elif((lefttype=='int' and righttype=='int' and (opr=='+' or opr=='-' or opr=='*' or opr =='/')) or((lefttype=='int' and (righttype=='float' or righttype=='int')) and opr=='=')):
        return 'int'
    elif(lefttype == 'string' and righttype == 'string' and opr=='='):
        return 'string'
    elif (((lefttype == 'string' and righttype == 'string')or((lefttype == 'int' or lefttype=='float') and righttype == 'string')or (lefttype == 'string' and( righttype == 'int' or righttype=='float'))) and (  opr == '+')):
        return 'string'
    elif(lefttype=='char' and righttype=='char' and opr=='='):
        return 'char'
    elif(lefttype==righttype and righttype=='boolean' and (opr=='and' or opr =='or')):
        return 'boolean'
    else:
        return False
def compatibility2(operand,opr):
    if(operand=='boolean' and opr=='not'):
        return 'boolean'
    else:
        return False
def insertCDT(N,T,AM,TM,CN):
    global ClassTable
    if(AM==''):
        AM='public'
    if(CN in Main_table['Name'].values):
        mask=Main_table['Name']==CN

        df=Main_table[mask]['Ref']

        if(N in df[0].Classbodytable['Name'].values):
            return False
        else:
            df[0].Classbodytable=df[0].Classbodytable.append(pd.DataFrame({'Name':[N],'Type':[T],'AM':[AM],'TM':[TM]}))
            return True
    else:
        return False






def insertMT(Name,Type,Parent):
    global Main_table
    if (Name in Main_table['Name'].values):
        return False
    else:

        if(Parent!=''):

            if(Parent in Main_table['Name'].values):

                Main_table=Main_table.append(pd.DataFrame({'Name':[Name],'Type':[Type],'Parent':[Parent],'Ref':[classbodytable(Name)]}))

                return True
        else:
            Main_table = Main_table.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Parent': [Parent], 'Ref': [classbodytable(Name)]}))

            return True
def insertFT(Name, Type, Scope):
    global fn_table
    if (Name in fn_table['Name'].values):
        mask = fn_table['Name'] == Name

        df = fn_table[mask]['Scope']
        try:
            if(Scope==df[0]):

                return False
            else:
                fn_table = fn_table.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
                return True
        except:
            if (Scope == df[1]):

                return False
            else:
                fn_table = fn_table.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
                return True



    else:
       fn_table = fn_table.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
       return True

