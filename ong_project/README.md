# Sistema de Gestão - ONG Assistencial 🏢🤝

Este projeto é um sistema web desenvolvido como parte do trabalho acadêmico para o curso de **ADS - CESMAC**. O objetivo é fornecer uma ferramenta segura e eficiente para o cadastro de famílias assistidas, garantindo a privacidade dos dados (LGPD).

## 👥 Integrantes do Grupo
* **Volnei Aurélio** 
* [Nome do Integrante 2]
* [Nome do Integrante 3]
* [Nome do Integrante 4]
* [Nome do Integrante 5]

## 🚀 Tecnologias Utilizadas
* **Python 3.14** (Linguagem base)
* **Django** (Framework Web)
* **SQLite** (Banco de dados)
* **Git/GitHub** (Versionamento)
* **Ambiente Virtual (venv)** (Isolamento de dependências)

## 🔒 Funcionalidades Atuais
- **Painel Administrativo:** Interface segura para gestão de dados.
- **Controle de Acesso:** A página inicial é protegida por login. Somente usuários cadastrados visualizam os CPFs e nomes das famílias.
- **Banco de Dados Relacional:** Tabela de famílias com validação de campos.

## 🛠️ Como rodar o projeto no seu computador

Se você é o professor ou um integrante do grupo, siga os passos abaixo para testar o sistema:

### 1. Clonar o repositório
git clone https://github.com/adsvolnei/Projeto-ONG.git
cd Projeto-ONG

### 2. Criar e Ativar o Ambiente Virtual
python -m venv venv
# No Windows (PowerShell): .\venv\Scripts\activate
# No Git Bash: source venv/Scripts/activate

### 3. Instalar o Django
pip install django

### 4. Rodar as Migrações (Preparar o Banco)
python manage.py migrate

### 5. Iniciar o Servidor
python manage.py runserver

O site estará disponível em: http://127.0.0.1:8000/

---
*Projeto desenvolvido para fins educacionais - CESMAC 2026*