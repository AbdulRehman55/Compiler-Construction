#import LexSyntax as lx
#import CC1
import pandas as pd
import regex
import json
import numpy as np

stack = []
CrP=''
CN=''
CT=''
CS=''
N=''
N2=''
CDrT=''
AM=''
TM=''
ST=''
OP=''
Types=[]
Opr=[]
comp={('float','int'):['int','float','+','-','*','/','='],('string'):['char','string','+'],('int'):['int','int','+','-','*','/'],('string'):['char','char','+']}
ScopeTable = pd.DataFrame({'Name': [], 'Type': [], 'Scope': []})
ClassTable = pd.DataFrame({'Name': [], 'Type': [], 'Parent': [], 'Ref': []})
scope=0
#class body table
class classreftable:

    def __init__(self,CN):
        self.CN=CN
        self.Classreftable = pd.DataFrame({'Name': [], 'Type': [], 'AM': [], 'TM': []})

def lookUpCT(N):
    if(N in ClassTable['Name'].values):
        return True
    else:
        return False
def lookupCDT(CN,N,Parent):
    if (CN in ClassTable['Name'].values):
        mask = ClassTable['Name'] == CN

        df = ClassTable[mask]['Ref']
        if (N in df[0].Classreftable['Name'].values):
            mas=df[0].Classreftable['Name']==N
            value=df[0].Classreftable['AM'][mas]

            if(value[0]=='public'):
                    return (df[0].Classreftable['Type'][mas][0])
            elif(value[0]=='private' or value[0]=='protected'):
                print('You can\'t it because  you access private or protected varibale')
                return False
        elif(Parent in ClassTable['Name'].values):

            mask = ClassTable['Name'] == Parent

            df = ClassTable[mask]['Ref']
            if (N in df[0].Classreftable['Name'].values):
                mas = df[0].Classreftable['Name'] == N
                value = df[0].Classreftable['AM'][mas]
                if (value[0] == 'public' or value[0] == 'protected'):
                    return (df[0].Classreftable['Type'][mas][0])
                elif (value[0] == 'private'):
                    print('You can\'t it because  you access private or protected varibale')
                    return False
                else:
                    print(N + ' is not declared')
                    return False
        else:
            print(N+ ' is not declared')
            return False
def lookupST(N,SS,CN):
    global ScopeTable
    global ClassTable

    if(N in ScopeTable['Name'].values):

        mas=ScopeTable['Name']==N
        df=ScopeTable[mas]['Scope']
      #  print(int(df[1]))
        #print(SS)
       # t=int(df[1])==SS

        try:
            if(df[0]==SS):

                return(ScopeTable[mas]['Type'][0])

            else:
                return False

        except:
            if (df[1] == SS):

                return (ScopeTable[mas]['Type'][1])

            else:
                return False


    elif (CN in ClassTable['Name'].values):
        mask = ClassTable['Name'] == CN

        df = ClassTable[mask]['Ref']

        if (N in df[0].Classreftable['Name'].values):
            mas=df[0].Classreftable['Name']==N
            value=df[0].Classreftable['AM'][mas]

            if(value[0]=='public'):
                    return (df[0].Classreftable['Type'][mas][0])
            elif(value[0]=='private' or value[0]=='protected'):
                print('You can\'t it because  you access private or protected varibale')
                return False

        elif(CrP in ClassTable['Name'].values):

            mask = ClassTable['Name'] == CrP

            df = ClassTable[mask]['Ref']
            if (N in df[0].Classreftable['Name'].values):
                mas = df[0].Classreftable['Name'] == N
                value = df[0].Classreftable['AM'][mas]
                if (value[0] == 'public' or value[0] == 'protected'):
                    return (df[0].Classreftable['Type'][mas][0])
                elif (value[0] == 'private'):
                    print('You can\'t it because  you access private or protected varibale')
                    return False
                else:
                    print(N + ' is not declared')
                    return False
            else:
                return False
        else:
            print(N+ ' is not declared')
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
    if(CN in ClassTable['Name'].values):
        mask=ClassTable['Name']==CN

        df=ClassTable[mask]['Ref']

        if(N in df[0].Classreftable['Name'].values):
            return False
        else:
            df[0].Classreftable=df[0].Classreftable.append(pd.DataFrame({'Name':[N],'Type':[T],'AM':[AM],'TM':[TM]}))
            return True
    else:
        return False
    #print(ClassTable[mask]['Ref'].Classreftable)
  #  df.Classreftable=(df.Classreftable).append(pd.DataFrame({'Name':[N],'Type':[T],'AM':[AM],'TM':[TM]}))






def insertCT(Name,Type,Parent):
    global ClassTable
    if (Name in ClassTable['Name'].values):
        return False
    else:

        if(Parent!=''):

            if(Parent in ClassTable['Name'].values):

                ClassTable=ClassTable.append(pd.DataFrame({'Name':[Name],'Type':[Type],'Parent':[Parent],'Ref':[classreftable(Name)]}))

                return True
        else:
            ClassTable = ClassTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Parent': [Parent], 'Ref': [classreftable(Name)]}))

            return True
def insertST(Name, Type, Scope):
    global ScopeTable
    if (Name in ScopeTable['Name'].values):
        mask = ScopeTable['Name'] == Name

        df = ScopeTable[mask]['Scope']
        try:
            if(Scope==df[0]):

                return False
            else:
                ScopeTable = ScopeTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
                return True
        except:
            if (Scope == df[1]):

                return False
            else:
                ScopeTable = ScopeTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
                return True



    else:
       ScopeTable = ScopeTable.append(pd.DataFrame({'Name': [Name], 'Type': [Type], 'Scope': [Scope]}),ignore_index='True')
       return True

print(ScopeTable)
check=insertST('a', 'int', '7')
print(check)
check=insertST('b', 'int', '7')
print(check)
insertCT('I','class','')
check=insertCDT('b','char','public','static','I')
print(check)
type=lookupST('b',7,'I')
print(type)

insertCT('I','class','')
insertCT('J','class','I')

insertCT('D','class','E')
check=insertCDT('a','int','public','static','J')
check=insertCDT('d','float','private','static','I')
check=insertCDT('b','char','public','static','I')
check=insertCDT('c','string','protected','static','I')
type=lookupCDT('J','d','I')
print(type)
type=lookupCDT('J','b','I')
print(type)
type=lookupCDT('J','c','I')
print(type)
check=insertCDT('a','int','public','static','A')
print(check)
print(ClassTable[0:3])
# def main():
#   global TS

#  TS=lx.main()


# main()
