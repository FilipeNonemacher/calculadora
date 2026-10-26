import customtkinter as ctk  # Importa a biblioteca CustomTkinter para criar uma interface moderna com estilos do Windows 11

ctk.set_appearance_mode("Light")  # Define o modo de aparência da interface como claro para combinar com a imagem de referência
ctk.set_default_color_theme("blue")  # Define o tema de cores padrão para os componentes do CustomTkinter

def clique_botao(valor):  # Função principal que gerencia a ação de clique de cada botão da calculadora
    valor_atual = display_var.get()  # Pega o texto atual que está sendo exibido no visor da calculadora
    
    if valor == "CE":  # Verifica se o botão pressionado pelo usuário foi o 'CE' (limpeza da entrada atual)
        display_var.set("0")  # Reseta o valor do display da calculadora de volta para o número zero
    elif valor == "⌫":  # Verifica se o botão pressionado foi o de apagar o último dígito (backspace)
        if len(valor_atual) > 1:  # Verifica se o visor possui mais de um caractere atualmente
            display_var.set(valor_atual[:-1])  # Remove o último caractere da string atual do display
        else:  # Caso o visor tenha apenas um caractere restando
            display_var.set("0")  # Reseta o display para "0" garantindo que ele nunca fique completamente vazio
        
    elif valor in "0123456789":  # Verifica se o botão pressionado é um dos números de 0 até 9
        if valor_atual == "0":  # Condição para verificar se o display está apenas com o zero inicial
            display_var.set(valor)  # Substitui o zero inicial pelo primeiro número digitado
        else:  # Caso o visor já contenha outros números digitados anteriormente
            display_var.set(valor_atual + valor)  # Concatena o novo número ao lado dos números já existentes no visor
            
    elif valor == ",":  # Verifica se o botão pressionado foi a vírgula decimal
        if "," not in valor_atual:  # Garante que só pode existir uma vírgula por número no visor
            display_var.set(valor_atual + valor)  # Adiciona a vírgula ao final do valor atual do display

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