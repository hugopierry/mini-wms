import sys
import sqlite3

from banco import conectar, criar_tabelas

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from rich.console import Console  
from rich.panel import Panel  
from time import sleep
from pwinput import pwinput  


class Criar_acesso_usuario:

    def __init__(self):

        self.console = Console()

        self.console.print(
            Panel(
                "[bold white]   CRIAR USUÁRIO E SENHA\n\n"
                "   Preencha seus dados[/bold white]",
                border_style="cyan",
                width=30
            )
        )

        self.criar_usuario = input("\n👤 Crie um usuário: ")
        self.criar_senha = pwinput("🔐 Crie uma senha: ").strip()
        self.confirmar_senha = pwinput("🔁 Confirmar senha: ").strip()
        self.nome = input("👤 Nome completo: ").strip()

        # Validação da senha
        while self.confirmar_senha != self.criar_senha:

            self.console.print(
                "\n🔎[blue] Analisando cadastro...[/blue]"
            )

            sleep(1)

            self.console.print(
                Panel(
                    "\n❌ A senha criada não é igual a senha confirmada.",
                    border_style="red",
                    width=60
                )
            )

            print("Tente novamente.")

            self.criar_senha = pwinput("\nCrie uma senha: ").strip()
            self.confirmar_senha = pwinput(
                "Confirmar senha: "
            ).strip()

        self.console.print(
            "\n⏳[yellow] Processando dados...[/yellow]"
        )

        sleep(2)

        conexao = conectar()
        cursor = conexao.cursor()

        comando_sql = """
            INSERT INTO usuarios (matricula, senha, nome)
            VALUES (?, ?,?)
        """

        try:

            cursor.execute(
                comando_sql,
                (self.criar_usuario, self.criar_senha, self.nome)
            )

            conexao.commit()

            self.console.print(
                Panel(
                    f"\n✅ Usuário '{self.criar_usuario}' criado com sucesso!",
                    border_style="green",
                    width=38
                )
            )

        except sqlite3.IntegrityError:

            self.console.print(
                Panel(
                    "\n⚠️ Essa matrícula já está cadastrada!",
                    border_style="yellow",
                    width=38
                )
            )


class Acesso_usuario:

    def __init__(self, cadastro):

        self.console = Console()

        self.console.print(
            Panel(
                "\n🔐 USUÁRIO E SENHA\n",
                border_style="cyan",
                width=23
            )
        )

        self.usuario = input("\n👤 Usuário: ").strip()
        self.senha = pwinput("🔑 Senha: ").strip()

        self.console.print(
            "\n⏳[yellow] Processando dados...[/yellow]"
        )

        sleep(2)

        conexao = conectar()
        cursor = conexao.cursor()

        comando_sql = """
            SELECT matricula, senha
            FROM usuarios
            WHERE matricula = ? AND senha = ?
        """

        cursor.execute(
            comando_sql,
            (self.usuario, self.senha)
        )

        resultado = cursor.fetchone()

        while resultado is None:

            self.console.print(
                Panel(
                    "\n❌ Usuário ou senha incorretos.",
                    border_style="red",
                    width=30
                )
            )

            print("Tente novamente.")

            self.usuario = input("\n👤 Usuário: ").strip()
            self.senha = pwinput("🔑 Senha: ").strip()

            cursor.execute(
                comando_sql,
                (self.usuario, self.senha)
            )

            resultado = cursor.fetchone()

        self.console.print(
            "\n[green] Bem-vindo ao sistema![/green]\n"
        )

def login():
    console= Console()

    while True:
        console.print(
            Panel(
            "\n 🔐 MINI WMS\n\n"
            "[1] Entrar\n"
            "[2] Criar usuário\n"
            "[0] Sair\n",
            border_style ="cyan",width=30
            )
    )

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            usuario_cadastrado = Acesso_usuario(None)
            return usuario_cadastrado

        elif opcao == "2":
            Criar_acesso_usuario()

        elif opcao == "0":
            sleep(1)
            console.print("\n👋 Saindo do sistema...")
            break
        else:
            console.print(
                "\n❌ Opção inválida. Tente novamente."
            )

# Verifica se este arquivo está sendo executado diretamente.
if __name__ =="__main__":
    criar_tabelas()
    login()
    
    

            
    input("\n\n\n\n\nPressione ENTER para sair do programa.")
