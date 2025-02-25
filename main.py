from scripts.data_loader import data_load
from scripts.data_cleaner import cleaner
from scripts.analyzer import calculate_metric
from scripts.visualize import visualize

def main():
    # Caminhos
    caminho_dados = "data/vendas.csv"
    caminho_saida = "outputs/graficos"

    # Carregar dados
    dados = data_load(caminho_dados)
    if dados is None:
        return

    # Limpar dados
    dados_limpos = cleaner(dados)

    # Calcular métricas
    metricas = calculate_metric(dados_limpos)

    for chave, valor in metricas.items():
        print(f"{chave}: {valor}")

    # Gerar gráficos
    visualize(dados_limpos, caminho_saida)

if __name__ == "__main__":
    main()