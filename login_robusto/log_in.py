import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from rich.console import Console # type: ignore
from rich.panel import Panel # type: ignore


from time import sleep

from  pwinput import pwinput # type: ignore



class Criar_acesso_usuario:
    
    def __init__(self):
        self.console = Console()

        self.console.print(Panel("[bold white]   CRIAR USUÁRIO E SENHA"+"\n\n   Preencha seus dados[bold white]",border_style="cyan",width=30))
                                
        
        self.criar_usuario = input("\n👤 Crie um usuário: ")
        self.criar_senha = pwinput("🔐 Crie uma senha: ").strip()
        self.confirmar_senha = pwinput("🔁 Confirmar senha: ").strip()
        
         # validação # usar time

        while self.confirmar_senha != self.criar_senha:
                
                self.console.print("\n🔎[blue] Analisando cadastro...[/blue]")
                sleep(1)
                self.console.print(Panel("\n❌ A senha criada não é igual a senha confirmada.",border_style="red",width=60))
                print("Tente novamente.")
                self.criar_senha = pwinput("\nCrie uma senha: ").strip()
                self.confirmar_senha = pwinput("Confirmar senha: ").strip()
               
        self.console.print("\n⏳[yellow] Processando dados...[/yellow]")
        sleep(2)
        self.console.print(Panel(f"\n✅ Usuário '{self.criar_usuario}' criado com sucesso!",border_style="green",width=38))

                

class Acesso_usuario:
    
    def __init__(self,cadastro):
        self.console = Console()
        self.console.print(Panel("\n🔐 USUÁRIO E SENHA\n",border_style="cyan",width=23))
        self.usuario = input("\n👤 Usuário: ").strip()
        self.senha = pwinput("🔑 Senha: ").strip()
        self.console.print("\n⏳[yellow] Processando dados...[/yellow]")
        sleep(2)

        while self.usuario != cadastro.criar_usuario or self.senha != cadastro.criar_senha:
            self.console.print(Panel("\n❌ Usuário ou senha incorretos.",border_style="red",width=30))
            print("Tente novamente.")
            self.usuario = input("\n👤 Usuário: ").strip()
            self.senha = pwinput("🔑 Senha: ").strip()
        
        self.console.print("\n[green] Bem-vindo ao sistema![/green]\n")
        


def login():
    cadastro = Criar_acesso_usuario()
    

    usuario_cadastrado = Acesso_usuario(cadastro)

    return usuario_cadastrado


if __name__ == "__main__":
    login()


















