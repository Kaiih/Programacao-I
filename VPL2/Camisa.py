from Roupa import Roupa

##################################################

class Camisa(Roupa):
    __Cam_Tipo=None
    __Cam_Botoes=None
    __Cam_Bolsos=None
    __Cam_Gola=None

    def __init__(self):
        super().__init__()
        self.__Cam_Tipo=''
        self.__Cam_Botoes=0
        self.__Cam_Bolsos=0
        self.__Cam_Gola=True
        
    def Leitura(self):
        self.__Cam_Tipo=input('Digite o tipo da camisa:')
        self.__Cam_Botoes=int(input('Digite a quantidade de botões:'))
        self.__Cam_Bolsos=int(input('Digite a quantidade de bolsos:'))
        resp=input("A camisa possui gola(s/n): ")
        if resp=="S":
            self.__Cam_Gola=True
        else:
            self.__Cam_Gola=False
        super().Leitura()
        
    def toString(self):
        str=''
        str+=str+'\nImpressão das Camisas\nTipo de camisa=%s\nQuantidade de botões=%d\nQuantidade de bolsos=%d\nTem gola=%s\n%s' % (self.__Cam_Tipo,self.__Cam_Botoes,self.__Cam_Bolsos,self.__Cam_Gola,super().toString())
        return (str)
        
    def __del__(self):
        super().__del__()
        print("Passei no destrutor da classe Camisa...")

##################################################
