##################################################

class Roupa(object):
    
    __Roupa_Marca:str
    __Roupa_Cor:str
    __Roupa_Tam:int
    __Roupa_Quant:int
    __Roupa_Preco:float
    __Total_Roupa:float
   
    def __init__(self):
        self.__Roupa_Marca=''
        self.__Roupa_Cor=''
        self.__Roupa_Tam=0
        self.__Roupa_Quant=0
        self.__Roupa_Preco=0.0
        self.Calcula_Total()
    
    def Leitura(self):
        self.__Roupa_Marca=input("Digite a marca: ")
        self.__Roupa_Cor=input("Digite a cor: ")
        self.__Roupa_Tam=int(input("Digite o tamanho: "))
        self.__Roupa_Quant=int(input("Digite a quantidade: "))
        self.__Roupa_Preco=float(input("Digite o preço: "))

    def Calcula_Total(self):
        self.__Total_Roupa=self.__Roupa_Quant*self.__Roupa_Preco
    
    def toString(self):
        str=""
        str=str+"\nImpressão das Roupas\nMarca da roupa=%s\nCor da roupa=%s\nTamanho da roupa=%d\nQuantidade de roupas=%d\nPreço da peça de roupa=%.2f\nTotal=%.2f\n" % (self.__Roupa_Marca,self.__Roupa_Cor,self.__Roupa_Tam,self.__Roupa_Quant,self.__Roupa_Preco,self.__Total_Roupa)
        return(str)
    
    def __del__(self):
        print("Passei no destrutor da classe Roupa...")


##################################################
