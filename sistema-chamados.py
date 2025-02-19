chamados = []
historico = []
id_contador = 1

def adicionar_chamado(descricao, prioridade):
    global id_contador
    chamado = {
        'id': id_contador,
        'descricao': descricao,
        'prioridade': prioridade,
        'status': 'aberto'
    }
    chamados.append(chamado)
    id_contador += 1
    print(f"Chamado {chamado['id']} criado com sucesso!")

def buscar_chamado(termo):
    resultados = []
    try:
        id_busca = int(termo)
        for chamado in chamados:
            if chamado['id'] == id_busca:
                resultados.append(chamado)
    except ValueError:
        for chamado in chamados:
            if termo.lower() in chamado['descricao'].lower():
                resultados.append(chamado)
    return resultados

def remover_finalizados():
    global chamados
    chamados_ativos = [c for c in chamados if c['status'] != 'finalizado']
    removidos = len(chamados) - len(chamados_ativos)
    historico.extend([c for c in chamados if c['status'] == 'finalizado'])
    chamados = chamados_ativos
    print(f"{removidos} chamados finalizados foram removidos.")

def listar_por_prioridade():
    return sorted(chamados, key=lambda x: x['prioridade'])

def exibir_estatisticas():
    total = len(chamados)
    if total == 0:
        print("Não há chamados no sistema.")
        return

    abertos = len([c for c in chamados if c['status'] == 'aberto'])
    finalizados = len([c for c in chamados if c['status'] == 'finalizado'])
    
    print(f"\nEstatísticas:")
    print(f"Total de chamados: {total}")
    print(f"Chamados abertos: {abertos}")
    print(f"Chamados finalizados: {finalizados}")
    print(f"Chamados no histórico: {len(historico)}")

def reverter_lista():
    chamados.reverse()
    print("Lista de chamados revertida.")

def limpar_lista():
    global chamados
    historico.extend(chamados)
    chamados = []
    print("Lista de chamados limpa.")

def marcar_como_finalizado(id_chamado):
    for chamado in chamados:
        if chamado['id'] == id_chamado:
            chamado['status'] = 'finalizado'
            print(f"Chamado {id_chamado} marcado como finalizado.")
            return
    print(f"Chamado {id_chamado} não encontrado.")

def exibir_menu():
    """Exibe o menu de opções"""
    print("\n=== Sistema de Chamados ===")
    print("1. Adicionar novo chamado")
    print("2. Buscar chamado")
    print("3. Listar chamados por prioridade")
    print("4. Marcar chamado como finalizado")
    print("5. Remover chamados finalizados")
    print("6. Exibir estatísticas")
    print("7. Reverter lista")
    print("8. Limpar lista")
    print("0. Sair")
    print("========================")

def main():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            descricao = input("Digite a descrição do chamado: ")
            while True:
                try:
                    prioridade = int(input("Digite a prioridade (1 - Alta, 2 - Média, 3 - Baixa): "))
                    if prioridade in [1, 2, 3]:
                        break
                    print("Por favor, digite 1, 2 ou 3.")
                except ValueError:
                    print("Por favor, digite um número válido.")
            adicionar_chamado(descricao, prioridade)

        elif opcao == "2":
            termo = input("Digite o ID ou termo para busca: ")
            resultados = buscar_chamado(termo)
            if resultados:
                print("\nChamados encontrados:")
                for chamado in resultados:
                    print(f"ID: {chamado['id']}, Prioridade: {chamado['prioridade']}, "
                          f"Status: {chamado['status']}, Descrição: {chamado['descricao']}")
            else:
                print("Nenhum chamado encontrado.")

        elif opcao == "3":
            chamados_ordenados = listar_por_prioridade()
            if chamados_ordenados:
                print("\nChamados ordenados por prioridade:")
                for chamado in chamados_ordenados:
                    print(f"ID: {chamado['id']}, Prioridade: {chamado['prioridade']}, "
                          f"Status: {chamado['status']}, Descrição: {chamado['descricao']}")
            else:
                print("Não há chamados no sistema.")

        elif opcao == "4":
            try:
                id_chamado = int(input("Digite o ID do chamado a ser finalizado: "))
                marcar_como_finalizado(id_chamado)
            except ValueError:
                print("Por favor, digite um ID válido.")

        elif opcao == "5":
            remover_finalizados()

        elif opcao == "6":
            exibir_estatisticas()

        elif opcao == "7":
            reverter_lista()

        elif opcao == "8":
            confirmacao = input("Tem certeza que deseja limpar a lista? (s/n): ")
            if confirmacao.lower() == 's':
                limpar_lista()

        elif opcao == "0":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()