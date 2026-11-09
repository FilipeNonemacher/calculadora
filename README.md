# 🧮 Calculadora Moderna 

Uma calculadora de desktop desenvolvida em **Python** utilizando a biblioteca **CustomTkinter**, trazendo uma interface elegante inspirada no design translúcido (Liquid Glass) com o suporte robusto de cálculos de alta precisão através da biblioteca nativa `decimal`.

---

## 🎨 Funcionalidades e Design

* **Interface Moderna:** Estilo limpo em modo claro, com cantos arredondados (estilo pílula) e bordas suaves simulando vidro fosco.
* **Precisão Decimal:** Operações matemáticas executadas com a classe `Decimal` para evitar imprecisões comuns de ponto flutuante.
* **Histórico Dinâmico:** Acompanhe a expressão do cálculo atual sendo processada em tempo real logo acima do visor principal.
* **Funções Avançadas:** 
  * Operações básicas (`+`, `-`, `×`, `÷`)
  * Porcentagem (`%`)
  * Raiz quadrada (`²√x`)
  * Quadrado de um número (`x²`)
  * Inversão multiplicativa (`1/x`)
  * Inversão de sinal (`+/-`)
  * Funções de limpeza (`C`, `CE`, e botão de apagar `⌫`)

---

## 📂 Estrutura do Projeto

```text
calculadora/
│
├── src/
│   ├── __pycache__/
│   └── calculos.py        # Lógica central e processamento matemático com Decimal
├── tests/                 # Testes unitários do sistema
├── .gitignore             # Arquivos ignorados pelo Git
├── comandos_úteis.txt     # Guia rápido de comandos git/terminal
├── main.py                # Arquivo principal da interface gráfica (CustomTkinter)
├── README.md              # Documentação do projeto
└── requirements.txt       # Dependências do projeto
```
## ⚙️ Como Instalar e Executar

### Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/FilipeNonemacher/calculadora.git
   cd nome-do-seu-repositorio
2. **Crie o ambiente virtual (venv)**
   ```bash
   python -m venv venv
   ```
3. **Ative o ambiente virtual**
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```
5. **Execute a aplicação**
   ```bash
   python app.py
   ```

## Créditos

Feito por João Figueiró e Filipe Nonemacher