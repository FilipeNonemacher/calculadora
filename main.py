import customtkinter as ctk  # Importa a biblioteca CustomTkinter para criar uma interface moderna com estilos do Windows 11

ctk.set_appearance_mode("Light")  # Mantém o modo claro para o efeito translúcido
ctk.set_default_color_theme("blue")  # Define o tema de cores padrão para os componentes do CustomTkinter

#Variáveis de controle
primeiro_numero = None
operador_atual = None
limpar_visor = False
veio_de_igual = False #controlar se viemos de um cálculo concluído

def clique_botao(valor):  # Função principal que gerencia a ação de clique de cada botão da calculadora
    global primeiro_numero, operador_atual, limpar_visor, veio_de_igual #permitir que a função altere as variáveis
    valor_atual = display_var.get()  # Pega o texto atual que está sendo exibido no visor da calculadora
    
    if valor == "CE":  # Verifica se o botão pressionado foi o 'CE'
        if veio_de_igual:
            # Se o último botão pressionado foi o '=', o CE limpa tudo por uma única vez
            display_var.set("0")
            historico_var.set("")
            primeiro_numero = None
            operador_atual = None
            limpar_visor = False
            veio_de_igual = False  # Reseta a bandeira para o CE voltar ao comportamento normal
        else:
            # Comportamento padrão do CE: limpa apenas o display atual
            display_var.set("0")

    elif valor == "⌫":  # Verifica se o botão pressionado foi o de apagar o último dígito (backspace)
        if len(valor_atual) > 1:  # Verifica se o visor possui mais de um caractere atualmente
            display_var.set(valor_atual[:-1])  # Remove o último caractere da string atual do display
        else:  # Caso o visor tenha apenas um caractere restando
            display_var.set("0")  # Reseta o display para "0" garantindo que ele nunca fique completamente vazio
        
    elif valor in "0123456789":  # Verifica se o botão pressionado é um dos números de 0 até 9
        veio_de_igual = False
        if limpar_visor or valor_atual == "0":  # Condição para verificar se o display está apenas com o zero inicial
            display_var.set(valor)  # Substitui o zero inicial pelo primeiro número digitado
            limpar_visor = False
        else:  # Caso o visor já contenha outros números digitados anteriormente
            display_var.set(valor_atual + valor)  # Concatena o novo número ao lado dos números já existentes no visor
           
    elif valor == ",":  # Verifica se o botão pressionado foi a vírgula decimal
        veio_de_igual = False
        if "," not in valor_atual:  # Garante que só pode existir uma vírgula por número no visor
            display_var.set(valor_atual + valor)  # Adiciona a vírgula ao final do valor atual do display
    
    elif valor in "+-×÷": #capturar quando o usuário clica em um operador matemático
        primeiro_numero = float(valor_atual.replace(",", "."))
        operador_atual = valor
        historico_var.set(f"{valor_atual} {operador_atual}")
        limpar_visor = True
    
    


    #Aqui coloquei a funçao de operação matemtática mas pode se puxado para o Back posteriormente
    elif valor == "=":
        if primeiro_numero is not None and operador_atual is not None:
            segundo_numero = float(valor_atual.replace(",", "."))
            
            if operador_atual == "+":
                resultado = primeiro_numero + segundo_numero
            elif operador_atual == "-":
                resultado = primeiro_numero - segundo_numero
            elif operador_atual == "×":
                resultado = primeiro_numero * segundo_numero
            elif operador_atual == "÷":
                resultado = primeiro_numero / segundo_numero if segundo_numero != 0 else "Erro"

            if isinstance(resultado, float) and resultado.is_integer():
                resultado = int(resultado)

            historico_var.set(f"{str(primeiro_numero).replace('.', ',')} {operador_atual} {valor_atual} =")
            display_var.set(str(resultado).replace(".", ","))
            primeiro_numero = None
            operador_atual = None
            limpar_visor = True
            veio_de_igual = True

    elif valor in ("CE", "C"):
        display_var.set("0")
        historico_var.set("")  # Limpa o histórico superior
        primeiro_numero = None
        operador_atual = None
        limpar_visor = False




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