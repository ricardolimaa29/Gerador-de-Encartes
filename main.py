import flet as ft
import os
import pyodbc
import time



def main(pagina: ft.Page):
    pagina.theme_mode = 'light'
    pagina.window_maximized = True
    def messageSuces():
        time.sleep(1)
        pagina.snack_bar = ft.SnackBar(ft.Text("Conexão com o banco bem sucedida! ", color="White",style="Arial"))
        pagina.snack_bar.open = True
        pagina.snack_bar.bgcolor = "green"
        pagina.update()

    def messageFail():
        pagina.snack_bar = ft.SnackBar(ft.Text("Conexão com o banco falhou!",color="White",style="Arial"))
        pagina.snack_bar.open = True
        pagina.snack_bar.bgcolor = "Red"
        pagina.update()

    def messageFailEmp():
        pagina.snack_bar = ft.SnackBar(ft.Text("Conexão com o banco falhou!",color="White",style="Arial"))
        pagina.snack_bar.open = True
        pagina.snack_bar.bgcolor = "Red"
        pagina.update()
        

    connection_string = (
        "Driver={SQL Server};"
        "Server=SRVSQL01;"
        "Database=MOINHO;"
        "UID=TargetAdmin;"  
        "PWD=dlh%9>?xiyh1QPB;"  
        "Trusted_Connection=no;"
    )

    # Conectando ao banco de dados
    try:
        conn = pyodbc.connect(connection_string)
        
        # Criando um cursor
        cursor = conn.cursor()

        messageSuces()
        # Executando a consulta SQL
        cursor.execute("SELECT pro.cd_prod, pro.descricao,	prd.PrecoFixo FROM produto pro JOIN kit_prom_prd prd ON prd.cd_prod = pro.cd_prod")

        
            # Iterando sobre os resultados e preenchendo a lista `data`
        data = [
            {"codigo": str(row.cd_prod), "descricao": row.descricao, "preco": str(row.PrecoFixo)}
            for row in cursor.fetchall()
            ]

        # Fechando o cursor
        cursor.close()
        
    except pyodbc.Error as e:
        messageFail({e})

    # Fechando a conexão
    finally:
        conn.close()
    def obter_seq_kit_e_descricao(cd_emp):
        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            
            # Consulta para obter seq_kit e descrição baseado no cd_emp
            query = """
            SELECT
                kpe.seq_kit,
                kp.descricao
            FROM
                kit_prom_emp kpe
            JOIN
                kit_prom kp
            ON
                kpe.seq_kit = kp.seq_kit
            WHERE
                kpe.cd_emp = ?
            """
            cursor.execute(query, (cd_emp,))
            informacao = cursor.fetchall()
            
            # Extraindo seq_kit e descrição e adicionando à lista
            resultado = [{'seq_kit': i[0], 'descricao': i[1]} for i in informacao]
            
            # Fechando o cursor
            cursor.close()
            
            return resultado
        except pyodbc.Error as e:
            messageFailEmp({e})
        finally:
            conn.close()

    def obter_cd_emp(nome_fant):
        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            
            # Consulta para obter o cd_emp baseado no nome_fant
            query = "SELECT cd_emp FROM empresa WHERE nome_fant = ?"
            cursor.execute(query, (nome_fant,))
            cd_emp = cursor.fetchone()
            
            # Fechando o cursor
            cursor.close()
            
            # Se cd_emp for encontrado, retorná-lo; caso contrário, retornar None
            if cd_emp:
                return cd_emp[0]
            else:
                return None
        except pyodbc.Error as e:
            messageFailEmp({e})
        finally:
            conn.close()


    def empresa():
        lista = []
        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            # Executando a consulta SQL
            query = "SELECT nome_fant FROM empresa"
            cursor.execute(query)
            informacao = cursor.fetchall()
            
            # Extraindo os nomes das empresas e adicionando à lista
            lista = [i[0] for i in informacao]

            # Fechando o cursor
            cursor.close()
        except pyodbc.Error as e:
            messageFailEmp({e})
        finally:
            conn.close()
        
        return lista

    def atualizar_dropdown():
        empresas = empresa()  # Obtém a lista de empresas
        drop_emp.options = [ft.dropdown.Option(emp) for emp in empresas]
        pagina.update() 

    def search():
        pass

    def arquivoHeader(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file = e.files[0].path  # Pega o caminho completo do arquivo
            directory = os.path.dirname(selected_file)  # Usa os.path.dirname para pegar o diretório do arquivo
            dialog = ft.AlertDialog(
                
                title=ft.Text(f"Diretório: {directory}"),
                actions=[
                    ft.TextButton("OK", on_click=lambda _: close_dialog())
                ],
            
            )

            pagina.dialog = dialog
            pagina.dialog.open = True
            pagina.update()


    def arquivoFooter(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file = e.files[0].path  # Pega o caminho completo do arquivo
            directory = os.path.dirname(selected_file)  # Usa os.path.dirname para pegar o diretório do arquivo
            dialog = ft.AlertDialog(
                
                title=ft.Text(f"Diretório: {directory}"),
                actions=[
                    ft.TextButton("OK", on_click=lambda _: close_dialog())
                ],
            
            )

            pagina.dialog = dialog
            pagina.dialog.open = True
            pagina.update()
    def close_dialog():
        pagina.dialog.open = False  # Fecha o diálogo
        pagina.update()

    Headerfile_picker = ft.FilePicker(on_result=arquivoHeader)

    pagina.overlay.append(Headerfile_picker)

    file_picker = ft.FilePicker(on_result=arquivoFooter)
    # Função para atualizar o dropdown de empresas

    def atualizar_dropdown_emp():
        empresas = empresa()
        drop_emp.options = [ft.dropdown.Option(emp) for emp in empresas]
        pagina.update()
    pagina.overlay.append(file_picker)
    # Função para atualizar o dropdown de seq_kit

    def atualizar_dropdown_kit(nome_fant):
        cd_emp = obter_cd_emp(nome_fant)
        if cd_emp:
            kits = obter_seq_kit_e_descricao(cd_emp)
            drop_promo.options = [ft.dropdown.Option(f"{kit['seq_kit']} - {kit['descricao']}") for kit in kits]
        else:
            drop_promo.options = []
        pagina.update()
# Função chamada quando o usuário seleciona uma empresa
    def on_empresa_change(event):
        nome_fant = drop_emp.value
        atualizar_dropdown_kit(nome_fant)


    def selectedall(e):
        for row in table.rows:
            row.cells[0].content.value = e.control.value
        pagina.update()

    # Função para criar uma linha na tabela com altura específica
    def create_row(item):
            return ft.DataRow(
                color="white",
                cells=[
                    ft.DataCell(ft.Checkbox(value=False)),  # Checkbox
                    ft.DataCell(ft.Container(content=ft.Text(item["codigo"]), height=40)), 
                    ft.DataCell(ft.Container(content=ft.Text(item["descricao"]), height=40)), 
                    ft.DataCell(ft.Container(content=ft.Text(item["preco"]), height=40)), 
                ],
                on_long_press=True,
            )



    drop_emp = ft.Dropdown(
        label="Empresa",
        width=350,
        bgcolor="white",
        options=[ft.dropdown.Option(" ")],
        autofocus=True,
        on_change=on_empresa_change  # Configurando a função de callback
    )
    atualizar_dropdown()
    

    drop_promo = ft.Dropdown( label="Promoção",
                              width=500,
                              bgcolor="white",
                              options=[
                               ft.dropdown.Option(" "),
                           ],
                           autofocus=True,
    )

    atualizar_dropdown_emp()


    codigo = ft.TextField(label= "Código de produto",width=425,bgcolor="white")
    desc_prod = ft.TextField(label= "Descrição de produto",width=500,bgcolor="white")
    save_encarte = ft.TextField(label="Nome do Encarte", width=600,bgcolor="white")
    header = ft.ElevatedButton(text="HEADER",width=450,height=45,
                               style=ft.ButtonStyle(
                                    color=ft.colors.BLUE,
                                    bgcolor=ft.colors.WHITE,
                                    overlay_color=ft.colors.BLUE_200,
                                    shape=ft.RoundedRectangleBorder(radius=10), 
                               ),
                               on_click=lambda _:Headerfile_picker.pick_files())
    text_select = ft.Text("")
    footer = ft.ElevatedButton(text="FOOTER",width=450,bgcolor="white",height=45,
                               style=ft.ButtonStyle(
                                    color=ft.colors.BLUE,
                                    bgcolor=ft.colors.WHITE,
                                    overlay_color=ft.colors.BLUE_200,
                                    shape=ft.RoundedRectangleBorder(radius=10),
                                    
                               ),
                               on_click=lambda _:file_picker.pick_files())
    botao_incluir = ft.ElevatedButton(text="Pesquisar",on_click=search,
                                      width=260,height=45,
                                      style=ft.ButtonStyle(
                                        color=ft.colors.BLACK,
                                        bgcolor=ft.colors.WHITE,
                                        overlay_color=ft.colors.GREEN_300,
                                        
                                        shape=ft.RoundedRectangleBorder(radius=10))
                                      )
    color_preco = ft.TextField(label="Digite a cor para os preços",width=400,bgcolor="white",hint_text="#")
    color_cod = ft.TextField(label="Digite a cor para os códigos:",width=400,bgcolor="white",hint_text="#")

    limpar = ft.ElevatedButton(text="Limpar",height=45,width=500,
                                    style=ft.ButtonStyle(
                                      color=ft.colors.WHITE,
                                      bgcolor="red",
                                      overlay_color=ft.colors.RED_400,
                                      shape=ft.RoundedRectangleBorder(radius=10))
                                      )

    gerar_encarte = ft.ElevatedButton(text="Gerar Encarte",height=45,width=500,
                                    style=ft.ButtonStyle(
                                      color=ft.colors.WHITE,
                                      bgcolor="green",
                                      overlay_color=ft.colors.GREEN_400,
                                      shape=ft.RoundedRectangleBorder(radius=10))
                                      )

    # DataTable
    table = ft.DataTable(
        
        columns=[
            
            ft.DataColumn(
                label=ft.Checkbox(
                    value=False,
                    on_change=selectedall  # Checkbox na linha de cabeçalho
                )
            ),  # Coluna do Checkbox
            ft.DataColumn(label=ft.Text("CÓDIGO")),
            ft.DataColumn(label=ft.Text("DESCRIÇÃO DO PRODUTO")),
            ft.DataColumn(label=ft.Text("PREÇO")),
        ],
         rows=[create_row(item) for item in data],
        border=ft.border.all(2, "#002B6B"),
        heading_row_height=40,  # Altura da linha de cabeçalho
        width=2000,
        heading_row_color="red",
        show_bottom_border=True,
        show_checkbox_column=True  
        
    )
    

    # Coluna com scroll
    scrollable_column = ft.Column(
        controls=[table],
        scroll=ft.ScrollMode.AUTO, 
        width=1800,
        height=700,  
    )

    layout = ft.Container(
        
            content=ft.Column(
                
                [
                    
                    ft.Row(
                        [
                            drop_emp,
                            drop_promo,
                            codigo,
                            desc_prod
                        ]
                    ),
                    
                    
                    ft.Row(
                        [
                            save_encarte,
                            header,
                            text_select,
                            footer,
                            botao_incluir
                            
                        ]
                    ),
                    ft.Row(
                        [
                            scrollable_column
                        ]
                    )

 
                ],
                spacing=20  # Espaçamento entre os itens
            ),
            padding=40,
            margin=5,
            bgcolor="#75ACFF",
            
        )
    footer = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [
                        color_preco,
                        color_cod,
                        limpar,
                        gerar_encarte
                    ]
                )
            ]
        ),
        padding=10
    )
    
    pagina.add(layout,footer)


ft.app(target=main,assets_dir="fonts") #view=ft.WEB_BROWSER)
