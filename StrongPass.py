"""

Author: DarkZer0
Name: StrongPass
Function: Strong Password Generator
Version: 1.0

"""

# importa as bibliotecas
import string
import random
from colorama import init, Fore

import os
import sys
import pyfiglet
from threading import Thread

# inicia o colorama
init()

# limpa a tela usando o comando do SO
os.system("cls" if sys.platform == "win32" else "clear")

# funcão com nome ascii grande e infos do Author
def banner():
    print(Fore.GREEN+pyfiglet.figlet_format("StrongPass"))
    
    print(Fore.RED+"Press CRTL'C OR 'sair' TO EXIT\n")
    print(Fore.YELLOW+"Author:", Fore.WHITE+"DarkZer0")
    print(Fore.YELLOW+"Github:", Fore.WHITE+"https://github.com/DarkZer0/")
    print(Fore.YELLOW+"Source:", Fore.WHITE+"https://github.com/DarkZer0/StrongPass/\n")
    
banner()

# funcão que gera a senha
def gerar_senha():
    try:
        gerar = string.ascii_letters + string.digits + string.punctuation
        
        while True:
            tamanho = input(Fore.CYAN+"tamanho da senha: ")
            
            if tamanho == "sair":
                print(Fore.RED+"\nvocê saiu do gerador!\n")
                exit()
            
            else:
                inteiro = int(tamanho)
                
                gerando = ''.join(random.choice(gerar) for _ in range(inteiro))
                print(Fore.BLUE+f"\nsenha gerada: {gerando}\n")
        
    except Exception as e:
        print(Fore.RED+f"\nerro: {e}\n")
        
if __name__=="__main__":
    Thread(target=gerar_senha).start()

# fim
