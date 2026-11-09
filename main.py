import customtkinter as ctk  # Importa a biblioteca CustomTkinter para criar uma interface moderna com estilos do Windows 11
from src.calculos import Calculadora

calculadora = Calculadora()

ctk.set_appearance_mode("Light")  # Mantém o modo claro para o efeito translúcido
ctk.set_default_color_theme("blue")  # Define o tema de cores padrão para os componentes do CustomTkinter

#Variáveis de controle
primeiro_numero = None
operador_atual = None
limpar_visor = False
veio_de_igual = False #controlar se viemos de um cálculo concluído

def clique_botao(valor):
    visor, historico = calculadora.pressionar(valor)

    display_var.set(visor)
    historico_var.set(historico)



janela = ctk.CTk()  # Inicializa a janela principal da aplicação utilizando CustomTkinter
janela.title("Calculadora")  # Define o título exibido na barra de topo da janela
janela.geometry("320x450")  # Define as dimensões iniciais de largura e altura da janela
janela.resizable(False, False)  # Desativa a opção de redimensionar a janela pelo usuário
janela.configure(fg_color="#E8EEF2")  # Tom suave de vidro/gelo inspirado no fundo da imagem

display_var = ctk.StringVar(value="0")  # Cria uma variável de texto vinculada ao display com o valor inicial zero

# Cria a variável reativa e o rótulo do histórico que fica acima do visor principal
historico_var = ctk.StringVar(value="")
label_historico = ctk.CTkLabel(janela, textvariable=historico_var, font=("Segoe UI", 14), text_color="#86868B", anchor="e", fg_color="#E8EEF2")
label_historico.pack(fill="x", padx=15, pady=(10, 0))

label_display = ctk.CTkLabel(janela, textvariable=display_var, font=("Segoe UI", 36, "bold"), anchor="e", text_color="#1D1D1F", fg_color="#E8EEF2")  # Cria o componente visual do visor numérico da calculadora
label_display.pack(fill="x", padx=15, pady=25)  # Posiciona o visor no topo da janela com margens e espaçamento adequados

quadro_botoes = ctk.CTkFrame(janela, fg_color="#E8EEF2")  # Cria um container/quadro para organizar os botões em formato de grade
quadro_botoes.pack(fill="both", expand=True, padx=10, pady=5)  # Posiciona o container dos botões preenchendo o espaço restante

botoes = [  # Inicia a matriz contendo o layout completo dos botões idênticos à imagem de referência
    ["%", "CE", "C", "⌫"],  # Define os botões da primeira linha com funções de porcentagem e limpeza
    ["1/x", "x²", "²√x", "÷"],  # Define os botões da segunda linha com operações matemáticas avançadas
    ["7", "8", "9", "×"],  # Define os botões da terceira linha com números e o operador de multiplicação
    ["4", "5", "6", "-"],  # Define os botões da quarta linha com números e o operador de subtração
    ["1", "2", "3", "+"],  # Define os botões da quinta linha com números e o operador de adição
    ["+/-", "0", ",", "="]  # Define os botões da sexta linha com inversão de sinal, zero, vírgula e igual
]  # Fecha a matriz com a estrutura de botões

for linha_idx, linha in enumerate(botoes):  # Laço de repetição externo para percorrer cada linha da matriz
    for coluna_idx, texto in enumerate(linha):  # Laço de repetição interno para percorrer cada botão da linha atual
        # Define as cores baseadas no padrão iOS da Apple
        # Cores inspiradas no Liquid Glass (Vidro fosco limpo com reflexos)
        if texto in ("=", "+", "-", "×", "÷"):
            cor_fundo = "#0071E3"     # Azul translúcido moderno da Apple para ações principais
            cor_texto = "#FFFFFF"     
            cor_hover = "#0077ED"     
            borda_cor = "#47A0FF"     # Reflexo de luz na borda do botão
        elif texto in ("CE", "C", "⌫", "%", "1/x", "x²", "²√x", "+/-"):
            cor_fundo = "#D2D2D7"     # Vidro fosco secundário claro
            cor_texto = "#1D1D1F"     
            cor_hover = "#C7C7CC"     
            borda_cor = "#FFFFFF"     # Reflexo branco superior
        else:
            cor_fundo = "#FFFFFF"     # Branco puro translúcido (efeito vidro limpo)
            cor_texto = "#1D1D1F"     
            cor_hover = "#F5F5F7"     
            borda_cor = "#E5E5EA"     # Borda sutil de vidro

        botao = ctk.CTkButton(
            quadro_botoes,
            text=texto,
            font=("Segoe UI", 14, "bold"),
            fg_color=cor_fundo,
            text_color=cor_texto,
            hover_color=cor_hover,
            border_width=1,          # Adiciona a borda fina característica do vidro
            border_color=borda_cor,  # Cor do reflexo da borda
            corner_radius=25,        # Cantos bem arredondados estilo pílula/cápsula
            command=lambda t=texto: clique_botao(t)
        )

        
        botao.grid(row=linha_idx, column=coluna_idx, sticky="nsew", padx=3, pady=3)  # Posiciona o botão na grade utilizando o gerenciador grid com espaçamento

for i in range(6):  # Laço para configurar o comportamento dinâmico de redimensionamento das linhas da grade
    quadro_botoes.rowconfigure(i, weight=1)  # Permite que cada linha da grade expanda proporcionalmente

for j in range(4):  # Laço para configurar o comportamento dinâmico de redimensionamento das colunas da grade
    quadro_botoes.columnconfigure(j, weight=1)  # Permite que cada coluna da grade expanda proporcionalmente

janela.mainloop()  # Inicia o loop principal de execução da interface gráfica do CustomTkinter