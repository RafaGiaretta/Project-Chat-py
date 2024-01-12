#front-end -> user interface / user experience
#back-end -> program logic
#framework -> conjunto de ferramentas para facilitar o desenvolvimento
#flet -> biblioteca para criar interfaces gráficas com o python em qualquer sistema operacional (multiplataforma).

#Titulo  do programa "FaiscaZap"
#Botao de Iniciar Chat
    # Pop up
    # Bem vindo ao FasicaZap
    # Escreva seu nome
#Chat
    # Escreva sua mensagem
    # Botao de enviar   

import flet as ft

def main(pagina):
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    titulo = ft.Text("FaíscaZap")
    nome_usuario = ft.TextField(label="Digite seu nome")
    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update() #atualizar pagina

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui")
   
    def enviar_mensagem(evento):
        texto_campo_mensagem = f'Usuario: {nome_usuario.value} \n Mensagem: {campo_mensagem.value}' #colocar nome do usuario na mensagem
       
        pagina.pubsub.send_all(texto_campo_mensagem)
        campo_mensagem.value = "" #limpar o campo mensagem
        pagina.update() #atualizar pagina

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    def entrar_chat(evento):
        popup.open = False #fechar o popup
        pagina.remove(botao_iniciar) #tirar o inciar da tela
        pagina.add(chat)
        pagina.vertical_alignment = ft.MainAxisAlignment.NONE
        pagina.horizontal_alignment = ft.CrossAxisAlignment.NONE
        linha_mensagem = ft.Row([campo_mensagem, botao_enviar])
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update() #atualizar pagina

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem-Vindo ao  FaíscaZap "),
        content= nome_usuario, 
        actions= [ft.ElevatedButton("Entrar", on_click=entrar_chat )]
        
        )
    
    def iniciar_chat(evento):
        pagina.dialog = popup 
        popup.open = True
        pagina.update()


    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
     
    pagina.add(titulo)
    pagina.add(botao_iniciar)

#ft.app(main)
ft.app(main, view=ft.WEB_BROWSER)
    
