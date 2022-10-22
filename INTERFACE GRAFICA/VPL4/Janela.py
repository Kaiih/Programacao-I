from tkinter import *

##################################################

class Janela(Tk):
    __Lb_valor1=None
    __Lb_valor2=None
    __Lb_result=None
    __Et_valor1=None
    __Et_valor2=None
    __Et_result=None
    __Bt_adic=None
    __Bt_sub=None
    __Bt_mult=None
    __Bt_div=None
    
    def __init__(self,Str="Minha Calculadora",xl="",yl="",dx="",dy="",cor="orange"):
        super().__init__()
        super().title(Str)
        super().geometry("%sx%s+%s+%s" % (dx,dy,xl,yl))
        super().configure(bg=cor)
        
        self.inicialize()
    
    def action_exit(self):
        print("Destruindo a janela...")
        self.destroy()
    
    def action_Bt_adic(self):
        ## Questão 04: (Criar o evento que calcula a adição dos valores numéricos)
        pass
    
    def action_Bt_sub(self):
        ## Questão 05: (Criar o evento que calcula a subtração dos valores numéricos)
        pass
    
    def action_Bt_mult(self):
        ## Questão 06: (Criar o evento que calcula a multiplicação dos valores numéricos)
        pass
    
    def action_Bt_div(self):
        ## Questão 07: (Criar o evento que calcula a divisão dos valores numéricos)
        pass
    
    def inicialize(self):
        ## Questão 08: (Realize a alocação dos componentes gráficos)
        pass
        
        self.__Bt_adic=Button(self, text='Add' ", command= Questão 09")
        ## Questão 09: (Qual o comando que associa o botão Bt_Adic ao evento que realiza
        ##              os cálculos da Questão 04?)
        
        self.__Bt_sub=Button(self, text='Sub' "command= Questão 10" )
        ## Questão 10: (Qual o comando que associa o botão Bt_Sub ao evento que realiza
        ##              os cálculos da Questão 05?)
        
        self.__Bt_mult=Button(self, text='Mult' "command= Questão 11" )
        ## Questão 11: (Qual o comando que associa o botão Bt_Mult ao evento que realiza
        ##              os cálculos da Questão 06?)
        
        self.__Bt_div=Button(self, text='Div' "command= Questão 12" )
        ## Questão 12: (Qual o comando que associa o botão Bt_Div ao evento que realiza
        ##              os cálculos da Questão 07?)
        
        ############# Grid #############
        ## Questão 13: (Acrescentar os componentes gráficos na Tela) 
        
        self.protocol("WM_DELETE_WINDOW", self.action_exit)

##################################################
