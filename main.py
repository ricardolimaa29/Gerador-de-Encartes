import flet as ft
from tkinter import filedialog
import json

# Cria uma def ' main ' para rodar o flet

def main(pagina: ft.Page):
    # Dados de exemplo para a tabela
    data = [
        {"codigo": "001", "descricao": "Descrição do produto 1", "variacao": "Variação do produto 1"},
        {"codigo": "002", "descricao": "Descrição do produto 2", "variacao": "Variação do produto 2"},
        {"codigo": "003", "descricao": "Descrição do produto 3", "variacao": "Variação do produto 3"},
        {"codigo": "004", "descricao": "Descrição do produto 4", "variacao": "Variação do produto 4"},
        {"codigo": "005", "descricao": "Descrição do produto 5", "variacao": "Variação do produto 5"},
        {"codigo": "006", "descricao": "Descrição do produto 6", "variacao": "Variação do produto 6"},
        {"codigo": "007", "descricao": "Descrição do produto 4", "variacao": "Variação do produto 4"},
        {"codigo": "008", "descricao": "Descrição do produto 5", "variacao": "Variação do produto 5"},
        {"codigo": "009", "descricao": "Descrição do produto 6", "variacao": "Variação do produto 6"},
        {"codigo": "010", "descricao": "Descrição do produto 4", "variacao": "Variação do produto 4"},
        {"codigo": "011", "descricao": "Descrição do produto 5", "variacao": "Variação do produto 5"},
        {"codigo": "012", "descricao": "Descrição do produto 6", "variacao": "Variação do produto 6"},
        {"codigo": "013", "descricao": "Descrição do produto 6", "variacao": "Variação do produto 6"},
        {"codigo": "014", "descricao": "Descrição do produto 4", "variacao": "Variação do produto 4"},
        {"codigo": "015", "descricao": "Descrição do produto 5", "variacao": "Variação do produto 5"},
        {"codigo": "016", "descricao": "Descrição do produto 6", "variacao": "Variação do produto 6"},
        {"codigo": "017", "descricao": "Descrição do produto 6", "variacao": "Variação do produto 6"},
        {"codigo": "018", "descricao": "Descrição do produto 4", "variacao": "Variação do produto 4"},
        {"codigo": "019", "descricao": "Descrição do produto 5", "variacao": "Variação do produto 5"},
        {"codigo": "020", "descricao": "Descrição do produto 6", "variacao": "Variação do produto 6"},
        # Adicione mais linhas conforme necessário
    ]


    pagina.title = "Gerador de Encartes"
    pagina.theme_mode = "light"
    pagina.window_maximized = True

    Header_picker = ft.FilePicker()
    pagina.overlay.append(Header_picker)
    pagina.update()
    

    Footer_picker = ft.FilePicker()
    pagina.overlay.append(Header_picker)
    pagina.update()
    def this_seledted():
        pass

    def selectedall(e):
        pass
    mytable = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Codigo",color='black')),
            ft.DataColumn(ft.Text("Descrição",color='black')),
            ft.DataColumn(
                ft.Column([
                    ft.Text("Actions"),
                    ft.Checkbox(value=False,
                                on_change=selectedall)
                ])
                )
        ],
        rows=[]
    )
    # Função para criar uma linha na tabela com altura específica
    def create_row(item):
        return ft.DataRow(
            cells=[
                ft.DataCell(ft.Checkbox(value=False)),  # Checkbox
                ft.DataCell(ft.Container(content=ft.Text(item["codigo"]), height=40)),  # Código
                ft.DataCell(ft.Container(content=ft.Text(item["descricao"]), height=40)),  # Descrição
                ft.DataCell(ft.Container(content=ft.Text(item["variacao"]), height=40)),  # Variação
            ]
        )



    def inserir_test():
        print(Header_picker)


    # aqui fica as funções
    drop_emp = ft.Dropdown( label="Empresa",
                            width=350,
                            bgcolor="white",
                            options=[
                               ft.dropdown.Option(" "),
                               ft.dropdown.Option("NAVAS SP"),
                               ft.dropdown.Option("NAVAS MS"),
                               ft.dropdown.Option("NAVAS PR"),
                           ],
                           autofocus=True,
                           )
    
    drop_promo = ft.Dropdown( label="Promoção",
                              width=500,
                              bgcolor="white",
                              options=[
                               ft.dropdown.Option(" "),
                               ft.dropdown.Option("PROMO 1"),
                               ft.dropdown.Option("PROMO 2"),
                               ft.dropdown.Option("PROMO 3"),
                           ],
                           
                           )
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
                               on_click=lambda _:Header_picker.pick_files(allow_multiple=False))
    text_select = ft.Text("")
    footer = ft.ElevatedButton(text="FOOTER",width=450,bgcolor="white",height=45,
                               style=ft.ButtonStyle(
                                    color=ft.colors.BLUE,
                                    bgcolor=ft.colors.WHITE,
                                    overlay_color=ft.colors.BLUE_200,
                                    shape=ft.RoundedRectangleBorder(radius=10),
                               ),
                               on_click=lambda _:Footer_picker.pick_files(allow_multiple=False))
    botao_incluir = ft.ElevatedButton(text="Incluir",on_click=inserir_test)

    # DataTable
    table = ft.DataTable(
        columns=[
            ft.DataColumn(label=ft.Container(width=30)),  # Coluna do Checkbox sem título
            ft.DataColumn(label=ft.Text("Código")),
            ft.DataColumn(label=ft.Text("Descrição do produto")),
            ft.DataColumn(label=ft.Text("Variação do produto")),
        ],
        rows=[create_row(item) for item in data],
        border=ft.border.all(1, "blue"),  # Borda azul na tabela
        heading_row_height=30,  # Altura da linha de cabeçalho
        width=2000,
        
        
    )
    

    # Coluna com scroll
    scrollable_column = ft.Column(
        controls=[table],
        scroll=ft.ScrollMode.AUTO,  # Ativa scroll horizontal e vertical
        width=2000,  # Largura fixa para scroll horizontal
        height=700,  # Altura fixa para scroll vertical
    )
    layout = ft.Container(
        
            content=ft.Column(
                
                [
                    # Primeira linha com 2 colunas
                    ft.Row(
                        [
                            drop_emp,
                            drop_promo,
                            codigo,
                            desc_prod
                        ]
                    ),
                    
                    # Segunda linha com 2 colunas
                    ft.Row(
                        [
                            save_encarte,
                            header,
                            text_select,
                            footer,
                            botao_incluir
                            
                        ]
                    ),

 
                ],
                spacing=20  # Espaçamento entre os itens
            ),
            padding=40,
            margin=10,
            bgcolor="#D3D3D3",
            
        )
    
    pagina.add(layout,scrollable_column)


ft.app(target=main) #view=ft.WEB_BROWSER)