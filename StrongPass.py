"""

Author: DarkZer0
Name: StrongPass
Function: Strong Password Generator
Version: 1.5

"""

# importa as bibliotecas
import string
import random
import time

import os
import sys
import pyfiglet

from colorama import init, Fore
from datetime import datetime
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
        
        tempo_inicial = time.time()
        
        while True:
            tamanho = input(Fore.CYAN+"tamanho da senha: ")
            
            if tamanho == "sair":
                print(Fore.RED+"\nvocê saiu do gerador!\n")
                exit()
            
            else:
                inteiro = int(tamanho)
                
                gerando = ''.join(random.choice(gerar) for _ in range(inteiro))
                print(Fore.BLUE+f"\nsenha gerada: {gerando}\n")
                
                salvar = str(input(Fore.YELLOW+"\nDeseja salvar a senha em .txt? (y ou n): "))
                
                if salvar == "y":
                    with open("/sdcard/dcim/senha.txt", "w") as f:
                        f.write(gerando)
                        print(Fore.GREEN+"\nsenha salva com sucesso em /sdcar/dcim/senha.txt\n")
                        
                        print(Fore.CYAN+"data e hora: ", datetime.now())
                        tempo_final = time.time()
                        
                        total_tempo = int(tempo_final - tempo_inicial)
                        
                        h, remainder = divmod(total_tempo, 3600)
                        m, s = divmod(remainder, 60)
                        
                        print(Fore.CYAN+f"tempo de execução: {h}h {m}m {s}s\n")
                        exit()
                    
                if salvar == "n":
                    print(Fore.RED+"\nbeleza, senha não salva.\n")
                    
                    print(Fore.CYAN+"data e hora: ", datetime.now())
                    
                    tempo_final = time.time()
                    
                    total_tempo = int(tempo_final - tempo_inicial)
                    h, remainder = divmod(total_tempo, 3600)
                    
                    m, s = divmod(remainder, 60)
                    print(Fore.CYAN+f"tempo de execução: {h}h {m}m {s}s\n")
                    
                    exit()
        
    except Exception as e:
        print(Fore.RED+f"\nerro: {e}\n")
        quit()
    
if __name__=="__main__":
    Thread(target=gerar_senha).start()

# fim
