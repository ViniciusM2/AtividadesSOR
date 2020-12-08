import colorama
import os
from lib.servidor.conversor import VolumeUnit, SpeedUnit, AllowedGrandezas
# TESTE

class Manager:
    grandeza = None
    origem = None
    destino = None

    @classmethod
    def menu_inicial(cls):
        linha()
        print("+{:^125}+".format('Bem-vindo ao conversor de medidas'))
        linha()
        print("+{:^125}+".format('Selecione um tipo de conversão'))
        linha()
        print("+{:^125}+".format("1 - velocidade"))
        linha()
        print("+{:^125}+".format("2 - volume"))
        linha()
        print("{:^127}".format("Sua opção:"))
        try:
            op = int(input(' '*62))
            os.system('cls')
            if op == 1:
                Manager.grandeza = AllowedGrandezas.speed
                Manager.escolhe_origem(AllowedGrandezas.speed)
            elif op == 2:
                Manager.grandeza = AllowedGrandezas.volume
                Manager.escolhe_origem(AllowedGrandezas.volume)
            else:
                Manager.grandeza = None
                raise IOError()
            #
            #

        except:
            Manager.opcao_invalida()

    @classmethod
    def escolhe_origem(self, grandeza):
        try:
            linha()
            print(
                "+{:^125}+".format(f"Você escolheu a grandeza {grandeza.value[1]} - {grandeza.value[0]}"))
            linha()
            print(
                "+{:^125}+".format(f"Agora, escolha a unidade de {grandeza.value[0]} de partida na conversão"))
            linha()
            if grandeza == AllowedGrandezas.speed:
                nomeunidade = SpeedUnit.mph.value[0]
                print("+{:^125}+".format(f'1 - {nomeunidade}'))
                linha()
                nomeunidade = SpeedUnit.mps.value[0]
                print("+{:^125}+".format(f'2 - {nomeunidade}'))
                nomeunidade = SpeedUnit.kmph.value[0]
                linha()
                print("+{:^125}+".format(f'3 - {nomeunidade}'))
                linha()
                print("{:^127}".format("Sua opção:"))
                try:
                    op = int(input(' '*62))
                    os.system('cls')
                    if op == 1:
                        Manager.origem = SpeedUnit.mph
                        
                    elif op == 2:
                        Manager.origem = SpeedUnit.mps
                      
                    elif op == 3:
                        Manager.origem = SpeedUnit.kmph
                       
                    else:
                        Manager.origem = None
                        raise IOError()
                    Manager.escolhe_destino(AllowedGrandezas.speed)
                    #
                    #

                except:
                    Manager.opcao_invalida()
            elif grandeza == AllowedGrandezas.volume:
                nomeunidade = VolumeUnit.m3.value[0]
                print("+{:^125}+".format(f'1 - {nomeunidade}'))
                linha()
                nomeunidade = VolumeUnit.liter.value[0]
                print("+{:^125}+".format(f'2 - {nomeunidade}'))
                nomeunidade = VolumeUnit.barrel.value[0]
                linha()
                print("+{:^125}+".format(f'3 - {nomeunidade}'))
                linha()
                print("{:^127}".format("Sua opção:"))
                try:
                    op = int(input(' '*62))
                    os.system('cls')
                    if op == 1:
                        Manager.origem = VolumeUnit.m3
                    elif op == 2:
                        Manager.origem = VolumeUnit.liter
                    elif op == 3:
                        Manager.origem = VolumeUnit.barrel
                    else:
                        raise IOError()
                    Manager.escolhe_destino(AllowedGrandezas.volume)
                    #
                    #

                except:
                    Manager.opcao_invalida()
            else:
                raise Exception()
        except:
            Manager.opcao_invalida()

        #     linha()
        # linha()
        # input(' '*62)

    @classmethod
    def escolhe_destino(self, grandeza):
        try:
            if grandeza.value:
                linha()
                print(
                    "+{:^125}+".format(f"Você escolheu a grandeza {grandeza.value[1]} - {grandeza.value[0]}"))
                linha()
                print(
                    "+{:^125}+".format(f"Agora, escolha a unidade de {grandeza.value[0]} de destino na conversão"))
                linha()
                if grandeza == AllowedGrandezas.speed:
                    nomeunidade = SpeedUnit.mph.value[0]
                    print("+{:^125}+".format(f'1 - {nomeunidade}'))
                    linha()
                    nomeunidade = SpeedUnit.mps.value[0]
                    print("+{:^125}+".format(f'2 - {nomeunidade}'))
                    nomeunidade = SpeedUnit.kmph.value[0]
                    linha()
                    print("+{:^125}+".format(f'3 - {nomeunidade}'))
                    linha()
                    print("{:^127}".format("Sua opção:"))
                    try:
                        op = int(input(' '*62))
                        os.system('cls')
                        if op == 1:
                            Manager.destino = SpeedUnit.mph
                        elif op == 2:
                            Manager.destino = SpeedUnit.mps
                        elif op == 3:
                            Manager.destino = SpeedUnit.kmph
                        else:
                            Manager.destino = None
                            raise IOError()
                        Manager.insere_dados()
                        #
                        #

                    except Exception as e:
                        print(e)
                        print(e.with_traceback)
                        input()
                        Manager.opcao_invalida()
                elif grandeza == AllowedGrandezas.volume:
                    nomeunidade = VolumeUnit.m3.value[0]
                    print("+{:^125}+".format(f'1 - {nomeunidade}'))
                    linha()
                    nomeunidade = VolumeUnit.liter.value[0]
                    print("+{:^125}+".format(f'2 - {nomeunidade}'))
                    nomeunidade = VolumeUnit.barrel.value[0]
                    linha()
                    print("+{:^125}+".format(f'3 - {nomeunidade}'))
                    linha()
                    print("{:^127}".format("Sua opção:"))
                    try:
                        op = int(input(' '*62))
                        os.system('cls')
                        if op == 1:
                            Manager.destino = VolumeUnit.m3
                        elif op == 2:
                            Manager.destino = VolumeUnit.liter
                            # Navigator.escolhe_origem(AllowedGrandezas.volume)
                        elif op == 3:
                            Manager.destino = VolumeUnit.barrel
                            # Navigator.escolhe_origem(AllowedGrandezas.volume)
                        else:
                            Manager.destino = None
                            raise IOError()
                        Manager.insere_dados()
                        #
                        #

                    except:
                        Manager.opcao_invalida()
                else:
                    raise Exception()
            else:
                raise Exception()
        except:
            Manager.opcao_invalida()

    @classmethod
    def insere_dados(self):
        try:
            linha()
            print("+{:^125}+".format(f'A conversão realizada será da grandeza {Manager.grandeza.value[0]} partindo da unidade {Manager.origem.value[0]} para a unidade {Manager.destino.value[0]}'))
            linha()
            print("+{:^125}+".format(f"Insira o valor a ser convertido, em {Manager.origem.value[0]}"))
            x = float(input(' '*62))
        except:
            Manager.opcao_invalida()

        


    @classmethod
    def opcao_invalida(cls):
        os.system('cls')
        linha()
        print("{:^127}".format(f"Opção inválida!"))
        linha()
        print("{:^127}".format("Aperte ENTER para continuar"))
        linha()
        input(' '*62)
        os.system('cls')

        Manager.menu_inicial()


def linha():
    print('+'+'-'*20+'+'+'-'*20+'+'+'-'*20 +
          '+'+'-'*20+'+'+'-'*20+'+'+'-'*20+'+')


def desenhar_primeiro_menu():
    colorama.init()
    Manager.menu_inicial()


desenhar_primeiro_menu()
