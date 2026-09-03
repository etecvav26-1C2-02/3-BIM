import json
import os
import csv
import shutil
from datetime import datetime


DATA_FILE = "lanchonete_dados.json"

products = []
orders = []


# =========================
# CARREGAR DADOS
# =========================

def load_data():
    global products, orders

    if not os.path.exists(DATA_FILE):
        products = []
        orders = []
        return

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

        products = data.get("products", [])
        orders = data.get("orders", [])


# =========================
# SALVAR DADOS
# =========================

def save_data():

    data = {
        "products": products,
        "orders": orders
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


# =========================
# ENCONTRAR PRODUTO PELO CÓDIGO
# =========================

def find_product_by_code(code):

    for product in products:

        if product["code"] == code:
            return product

    return None


# =========================
# 1 - CADASTRAR PRODUTO
# =========================

def register_product():

    code = input("Código do produto: ")

    if find_product_by_code(code) is not None:
        print("Já existe um produto com este código.")
        return

    name = input("Nome do produto: ")

    price = float(input("Preço do produto: "))

    stock = int(input("Quantidade em estoque: "))

    product = {
        "code": code,
        "name": name,
        "price": price,
        "stock": stock
    }

    products.append(product)

    save_data()

    print("Produto cadastrado com sucesso!")


# =========================
# 2 - LISTAR PRODUTOS
# =========================

def list_products():

    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return

    print("\n--- PRODUTOS CADASTRADOS ---")

    for product in products:

        print(f"Código: {product['code']}")
        print(f"Nome: {product['name']}")
        print(f"Preço: R$ {product['price']:.2f}")
        print(f"Estoque: {product['stock']}")

        print("-" * 30)


# =========================
# 3 - FAZER PEDIDO
# =========================

def make_order():

    if len(products) == 0:
        print("Nenhum produto cadastrado.")
        return

    customer_name = input("Nome do cliente: ")

    list_products()

    code = input("Digite o código do produto: ")

    product = find_product_by_code(code)

    if product is None:
        print("Produto não encontrado.")
        return

    quantity = int(input("Quantidade desejada: "))

    if quantity <= 0:
        print("Quantidade inválida.")
        return

    if quantity > product["stock"]:
        print("Estoque insuficiente.")
        return

    total = quantity * product["price"]

    product["stock"] -= quantity

    order = {
        "customer_name": customer_name,
        "product_code": product["code"],
        "product_name": product["name"],
        "quantity": quantity,
        "total": total,
        "datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    orders.append(order)

    save_data()

    print("Pedido realizado com sucesso!")

    print(f"Total: R$ {total:.2f}")


# =========================
# 4 - VER PEDIDOS
# =========================

def list_orders():

    if len(orders) == 0:
        print("Nenhum pedido realizado.")
        return

    print("\n--- PEDIDOS REALIZADOS ---")

    for order in orders:

        print(f"Cliente: {order['customer_name']}")
        print(f"Produto: {order['product_name']}")
        print(f"Quantidade: {order['quantity']}")
        print(f"Total: R$ {order['total']:.2f}")
        print(f"Data/Hora: {order.get('datetime', 'Não informada')}")

        print("-" * 30)


# =========================
# 5 - ALTERAR PREÇO
# =========================

def change_product_price():

    code = input("Digite o código do produto: ")

    product = find_product_by_code(code)

    if product is None:
        print("Produto não encontrado.")
        return

    print(f"Produto: {product['name']}")

    print(f"Preço atual: R$ {product['price']:.2f}")

    new_price = float(input("Digite o novo preço: "))

    product["price"] = new_price

    save_data()

    print("Preço alterado com sucesso!")


# =========================
# 6 - REMOVER PRODUTO
# =========================

def remove_product():

    code = input("Digite o código do produto que deseja remover: ")

    product = find_product_by_code(code)

    if product is None:
        print("Produto não encontrado.")
        return

    print(f"Produto encontrado: {product['name']}")

    confirm = input("Deseja realmente remover? (s/n): ").lower()

    if confirm == "s":

        products.remove(product)

        save_data()

        print("Produto removido com sucesso!")

    else:
        print("Operação cancelada.")


# =========================
# 7 - PESQUISAR PRODUTO POR NOME
# =========================

def search_product_by_name():

    name = input("Digite o nome do produto: ").lower()

    found = False

    for product in products:

        if name in product["name"].lower():

            print("-" * 30)

            print(f"Código: {product['code']}")
            print(f"Nome: {product['name']}")
            print(f"Preço: R$ {product['price']:.2f}")
            print(f"Estoque: {product['stock']}")

            found = True

    if found == False:
        print("Nenhum produto encontrado.")


# =========================
# 8 - RELATÓRIO DE VENDAS
# =========================

def sales_report():

    if len(orders) == 0:
        print("Nenhuma venda realizada.")
        return

    total_sales = 0

    total_products = 0

    for order in orders:

        total_sales += order["total"]

        total_products += order["quantity"]

    print("\n--- RELATÓRIO DE VENDAS ---")

    print(f"Quantidade de pedidos: {len(orders)}")

    print(f"Quantidade de produtos vendidos: {total_products}")

    print(f"Total vendido: R$ {total_sales:.2f}")


# =========================
# 9 - TOTAL VENDIDO POR DATA
# =========================

def total_sales_by_date():

    date_text = input(
        "Digite a data (DD/MM/AAAA) ou pressione Enter para a data atual: "
    )

    if date_text == "":
        date_text = datetime.now().strftime("%d/%m/%Y")

    try:
        selected_date = datetime.strptime(date_text, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida. Use o formato DD/MM/AAAA.")
        return

    total_sales = 0

    for order in orders:

        order_date = order.get("datetime", "")[:10]

        if order_date == date_text:
            total_sales += order["total"]

    print(f"\n--- TOTAL VENDIDO EM {date_text} ---")
    print(f"Total vendido: R$ {total_sales:.2f}")


# =========================
# 10 - EXPORTAR RELATÓRIO CSV
# =========================

def export_sales_report():

    try:
        with open("relatorio_vendas.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Cliente",
                "Código do Produto",
                "Nome do Produto",
                "Quantidade",
                "Total R$",
                "Data/Hora"
            ])

            for order in orders:
                writer.writerow([
                    order.get("customer_name", ""),
                    order.get("product_code", ""),
                    order.get("product_name", ""),
                    order.get("quantity", ""),
                    order.get("total", ""),
                    order.get("datetime", "")
                ])

        print("Relatório exportado com sucesso para relatorio_vendas.csv!")

    except OSError as error:
        print(f"Erro ao exportar o relatório: {error}")


# =========================
# 11 - BACKUP DOS DADOS
# =========================

def backup_data():

    if not os.path.exists(DATA_FILE):
        print("Arquivo de dados não encontrado.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"lanchonete_dados_backup_{timestamp}.json"

    try:
        shutil.copy(DATA_FILE, backup_file)
        print(f"Backup criado com sucesso: {backup_file}")

    except OSError as error:
        print(f"Erro ao criar o backup: {error}")


# =========================
# MENU
# =========================

def show_menu():

    print("\n=== SISTEMA PARA LANCHONETE ===")

    print("1 - Cadastrar produto")

    print("2 - Listar produtos")

    print("3 - Fazer pedido")

    print("4 - Ver pedidos realizados")

    print("5 - Alterar preço de produto")

    print("6 - Remover produto")

    print("7 - Pesquisar produto por nome")

    print("8 - Relatório de vendas")

    print("9 - Total vendido por data")

    print("10 - Exportar relatório para CSV")

    print("11 - Criar backup do arquivo JSON")

    print("12 - Sair")


# =========================
# PROGRAMA PRINCIPAL
# =========================

load_data()

rodando = True

while rodando:

    show_menu()

    option = input("\nEscolha uma opção: ")

    match option:

        case "1":
            register_product()

        case "2":
            list_products()

        case "3":
            make_order()

        case "4":
            list_orders()

        case "5":
            change_product_price()

        case "6":
            remove_product()

        case "7":
            search_product_by_name()

        case "8":
            sales_report()

        case "9":
            total_sales_by_date()

        case "10":
            export_sales_report()

        case "11":
            backup_data()

        case "12":

            save_data()

            print("Sistema encerrado.")

            rodando = False

        case _:
            print("Opção inválida.")
