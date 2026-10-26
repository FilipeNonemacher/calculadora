import customtkinter as ctk  # Importa a biblioteca CustomTkinter para criar uma interface moderna com estilos do Windows 11

ctk.set_appearance_mode("Light")  # Define o modo de aparência da interface como claro para combinar com a imagem de referência
ctk.set_default_color_theme("blue")  # Define o tema de cores padrão para os componentes do CustomTkinter

def clique_botao(valor):  # Função executada ao clicar em qualquer botão da calculadora
    pass  # Espaço reservado para a lógica futura dos botões

janela = ctk.CTk()  # Inicializa a janela principal da aplicação utilizando CustomTkinter
janela.title("Calculadora")  # Define o título exibido na barra de topo da janela
janela.geometry("320x450")  # Define as dimensões iniciais de largura e altura da janela
janela.resizable(False, False)  # Desativa a opção de redimensionar a janela pelo usuário
janela.configure(fg_color="#f3f3f3")  # Define a cor de fundo da janela principal como cinza claro

display_var = ctk.StringVar(value="0")  # Cria uma variável de texto vinculada ao display com o valor inicial zero

label_display = ctk.CTkLabel(janela, textvariable=display_var, font=("Segoe UI", 32, "bold"), anchor="e", text_color="#000000", fg_color="#f3f3f3")  # Cria o componente visual do visor numérico da calculadora
label_display.pack(fill="x", padx=15, pady=25)  # Posiciona o visor no topo da janela com margens e espaçamento adequados

quadro_botoes = ctk.CTkFrame(janela, fg_color="#f3f3f3")  # Cria um container/quadro para organizar os botões em formato de grade
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
        cor_fundo = "#ffb900" if texto == "=" else "#ffffff"  # Define a cor de fundo laranja para o botão de igual e branco para os demais
        cor_texto = "#ffffff" if texto == "=" else "#000000"  # Define a cor do texto como branca para o botão de igual e preta para os outros
        cor_hover = "#e0a100" if texto == "=" else "#e5e5e5"  # Define a cor de destaque ao passar o mouse por cima do botão
        
        botao = ctk.CTkButton(  # Instancia um objeto CTkButton modernizado para o botão atual
            quadro_botoes,  # Define o quadro container como o elemento pai do botão
            text=texto,  # Atribui o texto correspondente ao botão atual
            font=("Segoe UI", 14),  # Define a família e o tamanho da fonte do texto do botão
            fg_color=cor_fundo,  # Aplica a cor de fundo calculada para o botão
            text_color=cor_texto,  # Aplica a cor do texto calculada para o botão
            hover_color=cor_hover,  # Define a cor exibida quando o cursor passa por cima do botão
            corner_radius=6,  # Define o arredondamento suave das bordas do botão estilo Windows 11
            command=lambda t=texto: clique_botao(t)  # Define a função de callback acionada ao clicar no botão
        )  # Fecha a criação do botão
        
        botao.grid(row=linha_idx, column=coluna_idx, sticky="nsew", padx=3, pady=3)  # Posiciona o botão na grade utilizando o gerenciador grid com espaçamento

for i in range(6):  # Laço para configurar o comportamento dinâmico de redimensionamento das linhas da grade
    quadro_botoes.rowconfigure(i, weight=1)  # Permite que cada linha da grade expanda proporcionalmente

for j in range(4):  # Laço para configurar o comportamento dinâmico de redimensionamento das colunas da grade
    quadro_botoes.columnconfigure(j, weight=1)  # Permite que cada coluna da grade expanda proporcionalmente

janela.mainloop()  # Inicia o loop principal de execução da interface gráfica do CustomTkinter