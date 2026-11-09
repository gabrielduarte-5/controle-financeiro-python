
print("=== SISTEMA DE CONTROLE FINANCEIRO ===")

descricoes = []
valores = []
tipos = []

saldo = 0

while True:
    print("\n========== MENU ==========")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Consultar saldo")
    print("4 - Histórico de movimentações")
    print("5 - Resumo financeiro")
    print("6 - Excluir movimentação")
    print("7 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        print("\n--- NOVA RECEITA ---")

        descricao = input("Descrição: ")
        valor = float(input("Valor: R$ "))

        if valor > 0 and descricao != "":
            descricoes.append(descricao)
            valores.append(valor)
            tipos.append("Receita")

            saldo = saldo + valor
            print("Receita registrada!")
        else:
            print("Dados inválidos!")

    elif opcao == "2":
        print("\n--- NOVA DESPESA ---")

        descricao = input("Descrição: ")
        valor = float(input("Valor: R$ "))

        if valor <= 0 or descricao == "":
            print("Dados inválidos!")

        elif valor > saldo:
            print("Saldo insuficiente!")

        else:
            descricoes.append(descricao)
            valores.append(valor)
            tipos.append("Despesa")

            saldo = saldo - valor
            print("Despesa registrada!")

    elif opcao == "3":
        print("\n--- SALDO ATUAL ---")
        print(f"Saldo disponível: R$ {saldo:.2f}")

    elif opcao == "4":
        print("\n--- HISTÓRICO ---")

        if len(descricoes) == 0:
            print("Nenhuma movimentação!")
        else:
            for i in range(len(descricoes)):
                print(
                    f"{i + 1} - {tipos[i]} | "
                    f"{descricoes[i]} | R$ {valores[i]:.2f}"
                )

    elif opcao == "5":
        print("\n--- RESUMO FINANCEIRO ---")

        total_receitas = 0
        total_despesas = 0

        for i in range(len(valores)):
            if tipos[i] == "Receita":
                total_receitas = total_receitas + valores[i]

            elif tipos[i] == "Despesa":
                total_despesas = total_despesas + valores[i]

        print(f"Total de receitas: R$ {total_receitas:.2f}")
        print(f"Total de despesas: R$ {total_despesas:.2f}")
        print(f"Saldo final: R$ {saldo:.2f}")

        if saldo > 0:
            print("Situação: saldo positivo!")

        elif saldo == 0:
            print("Situação: saldo zerado!")

        else:
            print("Situação: saldo negativo!")

    elif opcao == "6":
        print("\n--- EXCLUIR MOVIMENTAÇÃO ---")

        for i in range(len(descricoes)):
            print(
                f"{i + 1} - {tipos[i]} | "
                f"{descricoes[i]} | R$ {valores[i]:.2f}"
            )

        if len(descricoes) == 0:
            print("Nenhuma movimentação!")
        else:
            numero = int(input("Número da movimentação: "))

            if numero >= 1 and numero <= len(descricoes):
                indice = numero - 1

                if tipos[indice] == "Receita":
                    saldo = saldo - valores[indice]
                else:
                    saldo = saldo + valores[indice]

                descricoes.pop(indice)
                valores.pop(indice)
                tipos.pop(indice)

                print("Movimentação excluída!")
            else:
                print("Número inválido!")

    elif opcao == "7":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida!")
