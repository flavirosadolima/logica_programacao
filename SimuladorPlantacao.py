#!/usr/bin/env python
# coding: utf-8

# In[8]:





# In[8]:





# In[67]:


import random
import json
from datetime import datetime, timedelta

class PrecoMercado:
    """
    Simula uma API de mercado para obter preços de plantas.
    """
    @staticmethod
    def obter_preco_mercado(nome_planta):
        """
        Retorna um preço de mercado aleatório para uma planta.

        Args:
            nome_planta (str): O nome da planta.

        Returns:
            float: O preço de mercado da planta.
        """
        precos_base = {
            "Tomate": 5, "Alface": 3, "Cenoura": 4, "Batata": 4, 
            "Morango": 7, "Pepino": 4, "Abóbora": 6
        }
        preco = precos_base.get(nome_planta, 2)  # Preço base ou 2 se não encontrado
        return round(preco + random.uniform(-0.5, 0.5), 2) # Adiciona variação aleatória

class Planta:
    """
    Classe base para todas as plantas.
    """
    def __init__(self, nome, tempo_crescimento, rendimento_colheita):
        """
        Inicializa uma nova instância de Planta.

        Args:
            nome (str): O nome da planta.
            tempo_crescimento (int): O tempo que a planta leva para crescer (em dias).
            rendimento_colheita (int): A quantidade que a planta rende quando colhida.
        """
        self.nome = nome
        self.tempo_crescimento = tempo_crescimento
        self.rendimento_colheita = rendimento_colheita
        self.idade = 0
        self.saude = 100
        self.idade_madura = 0
        self.resistencia_doenca = random.randint(1, 10)
        self.colhida = False
        self.porcentagem_crescimento = 0
        self.crescimento_por_cuidado = 100 / tempo_crescimento

    def crescer(self):
        """
        Aumenta a idade da planta e atualiza o percentual de crescimento.
        """
        self.idade += 1
        self.atualizar_crescimento()

    def atualizar_crescimento(self):
        """
        Atualiza o percentual de crescimento da planta.
        """
        self.porcentagem_crescimento = min(self.porcentagem_crescimento + self.crescimento_por_cuidado, 100)
        print(f"{self.nome} cresceu! Percentual de crescimento: {self.porcentagem_crescimento:.2f}%")

    def esta_madura(self):
        """
        Verifica se a planta está madura o suficiente para ser colhida.

        Returns:
            bool: True se a planta estiver madura, False caso contrário.
        """
        return self.idade >= self.tempo_crescimento

    def colher(self):
        """
        Colhe a planta, se estiver madura e ainda não tiver sido colhida.

        Returns:
            int: A quantidade colhida da planta, ou 0 se não puder ser colhida.
        """
        if self.esta_madura() and not self.colhida:
            modificador_rendimento = self.saude / 100
            self.colhida = True
            return int(self.rendimento_colheita * modificador_rendimento)
        return 0

class Tomate(Planta):
    """
    Classe para a planta Tomate, herda de Planta.
    """
    def __init__(self):
        super().__init__("Tomate", 7, 10)
        self.tipo_tomate = random.choice(["Cereja", "Italiano", "Caqui"])

class Alface(Planta):
    """
    Classe para a planta Alface, herda de Planta.
    """
    def __init__(self):
        super().__init__("Alface", 5, 5)
        self.variedade_alface = random.choice(["Crespa", "Americana", "Roxa"])

class Cenoura(Planta):
    """
    Classe para a planta Cenoura, herda de Planta.
    """
    def __init__(self):
        super().__init__("Cenoura", 8, 8)
        self.cor_cenoura = random.choice(["Laranja", "Roxa", "Branca"])

class Batata(Planta):
    """
    Classe para a planta Batata, herda de Planta.
    """
    def __init__(self):
        super().__init__("Batata", 10, 12)
        self.tipo_batata = random.choice(["Inglesa", "Doce", "Roxa"])

class Morango(Planta):
    """
    Classe para a planta Morango, herda de Planta.
    """
    def __init__(self):
        super().__init__("Morango", 6, 7)
        self.variedade_morango = random.choice(["Camarosa", "Oso Grande", "Albion"])

class Pepino(Planta):
    """
    Classe para a planta Pepino, herda de Planta.
    """
    def __init__(self):
        super().__init__("Pepino", 7, 9)
        self.tipo_pepino = random.choice(["Japonês", "Caipira", "Aodai"])

class Abobora(Planta):
    """
    Classe para a planta Abóbora, herda de Planta.
    """
    def __init__(self):
        super().__init__("Abóbora", 12, 15)
        self.tipo_abobora = random.choice(["Moranga", "Butternut", "Jacarezinho"])

class EventoNatural:
    """
    Representa um evento natural que pode afetar as plantas.
    """
    eventos_respostas = {
        "Chuva forte": "Drenar o solo",
        "Onda de calor": "Fornecer sombra",
        "Praga de insetos": "Usar pesticida natural",
        "Vento forte": "Instalar barreiras de vento",
        "Geada": "Cobrir com plástico",
        "Crise econômica": "Diversificar cultivos",
        "Ferrugem do tomateiro": "Remover folhas afetadas",
        "Míldio": "Reduzir a umidade",
        "Mosca da cenoura": "Usar armadilhas adesivas",
        "Requeima da batata": "Aplicar calda bordalesa",
        "Podridão cinzenta": "Remover frutos afetados",
        "Oídio do pepino": "Aplicar leite diluído",
        "Vírus do mosaico": "Remover plantas infectadas",
        "Antracnose": "Aplicar calda de bórax"
    }

    def __init__(self, nome, descricao, impacto_saude):
        """
        Inicializa um novo evento natural.

        Args:
            nome (str): O nome do evento.
            descricao (str): Uma descrição do evento.
            impacto_saude (int): O impacto negativo na saúde da planta se não for tratado corretamente.
        """
        self.nome = nome
        self.descricao = descricao
        self.impacto_saude = impacto_saude
        self.opcao_correta = self.eventos_respostas[nome]
        self.opcoes = self.gerar_opcoes()

    def gerar_opcoes(self):
        """
        Gera opções de resposta para o evento, incluindo a correta e outras aleatórias.

        Returns:
            list: Uma lista de opções de resposta.
        """
        opcoes = [self.opcao_correta]
        while len(opcoes) < 5:
            opcao = random.choice(list(self.eventos_respostas.values()))
            if opcao not in opcoes:
                opcoes.append(opcao)
        random.shuffle(opcoes)
        return opcoes

    def aplicar(self, planta, opcao_escolhida):
        """
        Aplica o efeito do evento na planta, dependendo da opção escolhida.

        Args:
            planta (Planta): A planta afetada pelo evento.
            opcao_escolhida (str): A opção escolhida pelo jogador.

        Returns:
            str: Uma mensagem informando o resultado da ação.
        """
        if opcao_escolhida == self.opcao_correta:
            return f"Você lidou com o evento {self.nome} corretamente! A saúde da planta não foi afetada."
        else:
            planta.saude = max(0, planta.saude - self.impacto_saude)
            return f"Você não lidou corretamente com o evento. A saúde da planta {planta.nome} diminuiu em {self.impacto_saude} pontos."

class SistemaEventosNaturais:
    """
    Gerencia a ocorrência de eventos naturais.
    """
    def __init__(self):
        """
        Inicializa o sistema de eventos naturais com eventos gerais e específicos.
        """
        self.eventos_gerais = [
            EventoNatural("Chuva forte", "As plantas estão encharcadas.", 10),
            EventoNatural("Onda de calor", "As plantas estão ressecando.", 15),
            EventoNatural("Praga de insetos", "Insetos estão atacando as plantas.", 20),
            EventoNatural("Crise econômica", "Os preços dos alimentos estão instáveis.", 5)
        ]
        self.eventos_especificos = {
            "Tomate": [EventoNatural("Ferrugem do tomateiro", "Uma doença fúngica está afetando os tomateiros.", 25)],
            "Alface": [EventoNatural("Míldio", "Um fungo está causando manchas nas folhas de alface.", 20)],
            "Cenoura": [EventoNatural("Mosca da cenoura", "Insetos estão atacando as raízes das cenouras.", 30)],
            "Batata": [EventoNatural("Requeima da batata", "As batatas estão desenvolvendo manchas escuras.", 25)],
            "Morango": [EventoNatural("Podridão cinzenta", "Os morangos estão apodrecendo antes de amadurecer.", 20)],
            "Pepino": [EventoNatural("Oídio do pepino", "Um pó branco está cobrindo as folhas dos pepinos.", 15)],
            "Abóbora": [EventoNatural("Vírus do mosaico", "As folhas das abóboras estão com um padrão de mosaico.", 20)]
        }

    def disparar_evento(self, planta):
        """
        Dispara um evento natural aleatório para a planta, com chance de ser um evento específico para o tipo de planta.

        Args:
            planta (Planta): A planta que pode ser afetada pelo evento.

        Returns:
            EventoNatural: O evento que foi disparado, ou None se nenhum evento ocorrer.
        """
        if random.random() < 0.4:  # 40% de chance de ocorrer um evento
            eventos_especificos = self.eventos_especificos.get(planta.nome, [])
            todos_eventos = self.eventos_gerais + eventos_especificos
            return random.choice(todos_eventos)
        return None

class Inventario:
    """
    Gerencia o inventário do jardineiro, incluindo sementes, colheita e dinheiro.
    """
    def __init__(self, capacidade=20):
        """
        Inicializa um novo inventário com uma capacidade máxima.

        Args:
            capacidade (int): A capacidade máxima do inventário.
        """
        self.sementes = {}
        self.colheita = {}
        self.capacidade = capacidade
        self.dinheiro = 0

    def adicionar(self, item, quantidade, eh_semente=False):
        """
        Adiciona um item ao inventário.

        Args:
            item (str): O nome do item.
            quantidade (int): A quantidade a ser adicionada.
            eh_semente (bool): True se o item for uma semente, False caso contrário.
        """
        if item == "dinheiro":
            self.dinheiro += quantidade
            return

        alvo = self.sementes if eh_semente else self.colheita
        if self.obter_total_itens() + quantidade > self.capacidade:
            quantidade = self.capacidade - self.obter_total_itens()
            print(f"Inventário cheio! Apenas {quantidade} de {item} foram adicionados.")
        if quantidade > 0:
            alvo[item] = alvo.get(item, 0) + quantidade

    def remover(self, item, quantidade, eh_semente=False):
        """
        Remove um item do inventário.

        Args:
            item (str): O nome do item.
            quantidade (int): A quantidade a ser removida.
            eh_semente (bool): True se o item for uma semente, False caso contrário.

        Returns:
            bool: True se a remoção foi bem-sucedida, False caso contrário.
        """
        alvo = self.sementes if eh_semente else self.colheita
        if item in alvo and alvo[item] >= quantidade:
            alvo[item] -= quantidade
            if alvo[item] == 0:
                del alvo[item]
            return True
        return False

    def mostrar(self, jardineiro):
        """
        Exibe o conteúdo do inventário.

        Args:
            jardineiro (Jardineiro): O jardineiro cujo inventário será exibido.
        """
        print("Inventário:")
        print(f"Dinheiro: R$ {self.dinheiro:.2f}")
        print("Sementes:")
        for semente, quantidade in self.sementes.items():
            print(f" {semente}: {quantidade}")
        print("Colheita:", ", ".join(f"{k}: {v}" for k, v in self.colheita.items()))
        print(f"Espaço total: {self.obter_total_itens()}/{self.capacidade}")
        print(f"Nível do Jardineiro: {jardineiro.nivel}")
        print(f"Experiência atual: {jardineiro.experiencia}/{jardineiro.experiencia_para_proximo_nivel()}")

    def obter_total_itens(self):
        """
        Calcula o número total de itens no inventário.

        Returns:
            int: O número total de itens.
        """
        return sum(self.sementes.values()) + sum(self.colheita.values())

class Jardineiro:
    """
    Gerencia as ações do jardineiro, como plantar, cuidar e colher.
    """
    tipos_plantas = {
        "tomate": Tomate, "alface": Alface, "cenoura": Cenoura,
        "batata": Batata, "morango": Morango, "pepino": Pepino, "abobora": Abobora
    }

    plant_id_counter = 1  # Initialize the plant ID counter

    def __init__(self, nome):
        """
        Inicializa um novo jardineiro.

        Args:
            nome (str): O nome do jardineiro.
        """
        self.nome = nome
        self.nivel = 1
        self.experiencia = 0
        self.plantas_plantadas = {}
        self.inventario = Inventario()
        self.sistema_eventos_naturais = SistemaEventosNaturais()
    
    def plantar(self, tipo_planta):
        """
        Planta uma nova planta, removendo uma semente do inventário e adicionando a planta ao jardim.

        Args:
            tipo_planta (str): O tipo de planta a ser plantada.

        Returns:
            str: Uma mensagem informando o resultado da ação.
        """
        if tipo_planta in self.inventario.sementes and self.inventario.sementes[tipo_planta] > 0:
            nova_planta = self.tipos_plantas[tipo_planta]()
            plant_id = Jardineiro.plant_id_counter  # Get the next plant ID
            Jardineiro.plant_id_counter += 1  # Increment the counter
            self.plantas_plantadas[plant_id] = nova_planta
            self.inventario.remover(tipo_planta, 1, eh_semente=True)
            self.ganhar_experiencia(10)
            return f"{self.nome} plantou um(a) {nova_planta.nome} (ID: {plant_id})! Você ganhou 10 pontos de experiência."
        else:
            return f"{self.nome} não tem sementes de {tipo_planta} para plantar!"
    
    def cuidar(self, id_planta):
        """
        Cuida de uma planta no jardim, aumentando sua idade e lidando com eventos naturais.

        Args:
            id_planta (int): O ID da planta a ser cuidada.

        Returns:
            str: Uma mensagem informando o resultado da ação.
        """
        if id_planta not in self.plantas_plantadas:
            return f"Planta com ID {id_planta} não encontrada no jardim."

        planta = self.plantas_plantadas[id_planta]
        mensagens = []

        if planta.colhida:
            return f"{planta.nome} (ID: {id_planta}) já foi colhido(a) e está pronto(a) para venda."

        planta.crescer()

        evento = self.sistema_eventos_naturais.disparar_evento(planta)
        if evento:
            print(f"Um evento natural ocorreu: {evento.nome} - {evento.descricao}")
            print("Como você lida com isso?")
            for i, opcao in enumerate(evento.opcoes, 1):
                print(f"{i}. {opcao}")
            escolha = input("Escolha uma opção (1-5): ")
            try:
                opcao_escolhida = evento.opcoes[int(escolha) - 1]
                resultado = evento.aplicar(planta, opcao_escolhida)
                mensagens.append(resultado)
                if opcao_escolhida == evento.opcao_correta:
                    self.ganhar_experiencia(20)
                    mensagens.append("Você ganhou 20 pontos de experiência por lidar corretamente com o evento!")
                else:
                    self.experiencia = max(0, self.experiencia - 10)
                    mensagens.append(f"Você perdeu 10 pontos de experiência. Experiência atual: {self.experiencia}")
            except (ValueError, IndexError):
                mensagens.append("Opção inválida! A planta sofre as consequências da sua indecisão.")
                planta.saude = max(0, planta.saude - evento.impacto_saude)

        if planta.saude <= 0:
            mensagens.append(f"{planta.nome} (ID: {id_planta}) morreu e foi removido(a) do jardim.")
            del self.plantas_plantadas[id_planta]
        elif planta.esta_madura() and not planta.colhida:
            mensagens.append(f"{planta.nome} (ID: {id_planta}) está pronto(a) para ser colhido(a)!")
        
        mensagens.append(f"Saúde atual de {planta.nome} (ID: {id_planta}): {planta.saude}%")
        mensagens.append(f"Percentual de crescimento de {planta.nome} (ID: {id_planta}): {planta.porcentagem_crescimento:.2f}%")
        return "\n".join(mensagens)
    
    def colher(self, id_planta):
        """
        Colhe uma planta madura no jardim e adiciona a colheita ao inventário.

        Args:
            id_planta (int): O ID da planta a ser colhida.

        Returns:
            str: Uma mensagem informando o resultado da ação.
        """
        if id_planta not in self.plantas_plantadas:
            return f"Planta com ID {id_planta} não encontrada no jardim."
        
        planta = self.plantas_plantadas[id_planta]
        if planta.esta_madura() and not planta.colhida:
            quantidade_colhida = planta.colher()
            self.inventario.adicionar(planta.nome, quantidade_colhida)
            self.ganhar_experiencia(10)
            return f"Você colheu {quantidade_colhida} {planta.nome}(s) (ID: {id_planta})! Você ganhou 10 pontos de experiência."
        elif planta.colhida:
            return f"{planta.nome} (ID: {id_planta}) já foi colhido(a) e está pronto(a) para venda."
        else:
            return f"{planta.nome} (ID: {id_planta}) ainda não está pronto(a) para ser colhido(a)."
    
    def vender_planta(self, id_planta):
        """
        Vende uma planta colhida, removendo-a do jardim e adicionando dinheiro ao inventário.

        Args:
            id_planta (int): O ID da planta a ser vendida.

        Returns:
            str: Uma mensagem informando o resultado da ação.
        """
        if id_planta not in self.plantas_plantadas:
            return f"Planta com ID {id_planta} não encontrada no jardim."
        
        planta = self.plantas_plantadas[id_planta]
        if not planta.colhida:
            return f"{planta.nome} (ID: {id_planta}) ainda não foi colhido(a). Colha a planta antes de vender."
        
        if planta.saude < 80:
            perda_experiencia = 50
            perda_dinheiro = planta.rendimento_colheita * 15
            self.experiencia = max(0, self.experiencia - perda_experiencia)
            self.inventario.dinheiro = max(0, self.inventario.dinheiro - perda_dinheiro)
            del self.plantas_plantadas[id_planta]
            return f"{planta.nome} (ID: {id_planta}) foi descartado(a) e a safra perdida. Você perdeu {perda_experiencia} pontos de experiência e R$ {perda_dinheiro:.2f}. Você deve estudar mais para melhorar suas habilidades de jardinagem."
        
        preco = PrecoMercado.obter_preco_mercado(planta.nome)
        quantidade_colhida = planta.rendimento_colheita
        preco_total = preco * quantidade_colhida
        self.inventario.adicionar("dinheiro", preco_total)
        del self.plantas_plantadas[id_planta]
        self.ganhar_experiencia(40)
        return f"Vendido {quantidade_colhida} {planta.nome}(s) (ID: {id_planta}) por R${preco_total:.2f} (R${preco:.2f} cada)! Você ganhou 40 pontos de experiência."
    
    def procurar_sementes(self):
        """
        Procura sementes aleatórias e as adiciona ao inventário.

        Returns:
            str: Uma mensagem informando o resultado da ação.
        """
        semente = random.choice(list(self.tipos_plantas.keys()))
        quantidade = random.randint(1, 3)
        self.inventario.adicionar(semente, quantidade, eh_semente=True)
        self.ganhar_experiencia(5)
        return f"{self.nome} encontrou {quantidade} semente(s) de {semente}! Você ganhou 5 pontos de experiência."
    
    def ganhar_experiencia(self, quantidade):
        """
        Adiciona experiência ao jardineiro e verifica se ele subiu de nível.

        Args:
            quantidade (int): A quantidade de experiência a ser adicionada.
        """
        self.experiencia += quantidade
        while self.experiencia >= self.experiencia_para_proximo_nivel():
            mensagem_nivel_acima = self.nivel_acima()
            if mensagem_nivel_acima:
                print(mensagem_nivel_acima)
    
    def nivel_acima(self):
        """
        Aumenta o nível do jardineiro, redefine a experiência e aumenta a capacidade do inventário.

        Returns:
            str: Uma mensagem informando que o jardineiro subiu de nível.
        """
        self.nivel += 1
        self.experiencia -= self.experiencia_para_proximo_nivel()
        self.inventario.capacidade += 20
        mensagem = f"Parabéns! {self.nome} alcançou o nível {self.nivel}!"
        mensagem += f"\nSua capacidade de inventário aumentou para {self.inventario.capacidade}!"
        return mensagem
    
    def experiencia_para_proximo_nivel(self):
        """
        Calcula a quantidade de experiência necessária para o próximo nível.

        Returns:
            int: A quantidade de experiência necessária.
        """
        return 150 * min(self.nivel, 5)
    
    def exibir_jardim(self):
        """
        Exibe uma representação visual do jardim.

        Returns:
            str: Uma string representando o jardim.
        """
        exibicao_jardim = "\nSeu Jardim:"
        for id_planta, planta in self.plantas_plantadas.items():
            indicador_saude = "🌿" if planta.saude > 50 else "🍂"
            emoji_planta = "🧺" if planta.colhida else "🌱"
            status_colheita = "Colhido" if planta.colhida else ("Pronto para colheita" if planta.esta_madura() else "Em crescimento")
            exibicao_jardim += f"\n{emoji_planta} {planta.nome} (ID: {id_planta}) {indicador_saude} [{'#' * int(planta.porcentagem_crescimento / 10):<10}] {planta.porcentagem_crescimento:.0f}% | Saúde: {planta.saude}% | {status_colheita}"
        return exibicao_jardim

def salvar_jogo(jardineiro):
    """
    Salva o estado atual do jogo em um arquivo JSON.

    Args:
        jardineiro (Jardineiro): O jardineiro cujo jogo será salvo.

    Returns:
        str: Uma mensagem informando o resultado da operação.
    """
    dados_jogo = {
        "jardineiro": {
            "nome": jardineiro.nome,
            "nivel": jardineiro.nivel,
            "experiencia": jardineiro.experiencia,
            "inventario": {
                "sementes": jardineiro.inventario.sementes,
                "colheita": jardineiro.inventario.colheita,
                "capacidade": jardineiro.inventario.capacidade,
                "dinheiro": jardineiro.inventario.dinheiro
            },
            "plantas_plantadas": {id_planta: planta.__dict__ for id_planta, planta in jardineiro.plantas_plantadas.items()}
        }
    }
    try:
        with open("jogo_salvo.json", "w") as f:
            json.dump(dados_jogo, f)
        return "Jogo salvo com sucesso!"
    except Exception as e:
        return f"Erro ao salvar o jogo: {e}"

def carregar_jogo():
    """
    Carrega um jogo salvo de um arquivo JSON.

    Returns:
        tuple: Uma tupla contendo o jardineiro e uma mensagem informando o resultado da operação.
    """
    try:
        with open("jogo_salvo.json", "r") as f:
            dados_jogo = json.load(f)
        
        dados_jardineiro = dados_jogo["jardineiro"]
        jardineiro = Jardineiro(dados_jardineiro["nome"])
        jardineiro.nivel = dados_jardineiro["nivel"]
        jardineiro.experiencia = dados_jardineiro["experiencia"]
        jardineiro.inventario.sementes = dados_jardineiro["inventario"]["sementes"]
        jardineiro.inventario.colheita = dados_jardineiro["inventario"]["colheita"]
        jardineiro.inventario.capacidade = dados_jardineiro["inventario"]["capacidade"]
        jardineiro.inventario.dinheiro = dados_jardineiro["inventario"]["dinheiro"]

        dados_plantas_plantadas = dados_jardineiro["plantas_plantadas"]
        for id_planta, dados_planta in dados_plantas_plantadas.items():
            tipo_planta = dados_planta["nome"].lower()
            if tipo_planta in Jardineiro.tipos_plantas:
                classe_planta = Jardineiro.tipos_plantas[tipo_planta]
                planta = classe_planta()
                planta.__dict__.update(dados_planta)
                jardineiro.plantas_plantadas[int(id_planta)] = planta
            else:
                print(f"Tipo de planta desconhecido encontrado no save: {tipo_planta}")

        return jardineiro, "Jogo carregado com sucesso!"
    except FileNotFoundError:
        return None, "Nenhum jogo salvo encontrado."
    except Exception as e:
        return None, f"Erro ao carregar o jogo: {e}"

def main():
    """
    Função principal do jogo.
    """
    print("Bem-vindo ao Jogo de Jardinagem!")
    
    load_choice = input("Deseja carregar um jogo salvo? (s/n): ").lower()
    if load_choice == 's':
        jardineiro, message = carregar_jogo()
        print(message)
        if not jardineiro:
            jardineiro_nome = input("Nenhum jogo salvo. Qual é o seu nome, jardineiro? ")
            jardineiro = Jardineiro(jardineiro_nome)
    else:
        jardineiro_nome = input("Qual é o seu nome, jardineiro? ")
        jardineiro = Jardineiro(jardineiro_nome)

    print(f"Olá, {jardineiro.nome}! Vamos começar a jardinar!")

    while True:
        print("\nO que você gostaria de fazer?")
        print("1. Plantar")
        print("2. Cuidar do jardim")
        print("3. Colher")
        print("4. Vender")
        print("5. Procurar sementes")
        print("6. Verificar inventário")
        print("7. Exibir jardim")
        print("8. Salvar jogo")
        print("9. Sair")

        try:
            choice = int(input("Escolha uma opção (1-9): "))
            if choice == 1:
                plant_type = input("Que tipo de planta você quer plantar? (tomate/alface/cenoura/batata/morango/pepino/abobora): ").lower()
                if plant_type in Jardineiro.tipos_plantas:
                    message = jardineiro.plantar(plant_type)
                    print(message)
                else:
                    print("Tipo de planta inválido.")
            elif choice == 2:
                print(jardineiro.exibir_jardim())
                plant_id = int(input("Digite o ID da planta que você quer cuidar: "))
                message = jardineiro.cuidar(plant_id)
                print(message)
            elif choice == 3:
                print(jardineiro.exibir_jardim())
                plant_id = int(input("Digite o ID da planta que você quer colher: "))
                message = jardineiro.colher(plant_id)
                print(message)
            elif choice == 4:
                print(jardineiro.exibir_jardim())
                plant_id = int(input("Digite o ID da planta que você quer vender: "))
                message = jardineiro.vender_planta(plant_id)
                print(message)
            elif choice == 5:
                message = jardineiro.procurar_sementes()
                print(message)
            elif choice == 6:
                jardineiro.inventario.mostrar(jardineiro)
            elif choice == 7:
                print(jardineiro.exibir_jardim())
            elif choice == 8:
                message = salvar_jogo(jardineiro)
                print(message)
            elif choice == 9:
                print("Obrigado por jogar! Até a próxima!")
                break
            else:
                print("Opção inválida. Por favor, escolha um número entre 1 e 9.")
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




