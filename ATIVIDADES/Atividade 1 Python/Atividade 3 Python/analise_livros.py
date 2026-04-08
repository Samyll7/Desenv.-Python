import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Carregar o dataset
    print("Carregando dataset...")
    df = pd.read_csv('livros.csv', sep=';')

    print("\nPrimeiras 5 linhas:")
    print(df.head())

    # Estrutura dos dados
    print("\nInformações do dataset:")
    print(df.info())

    print("\nEstatísticas descritivas:")
    print(df.describe())

    # Comentário esperado
    print("\nObservação:")
    print("Verifique se 'isbn', 'ano' ou 'paginas' estão como object (deveriam ser numéricos).")

    # Valores nulos
    print("\nValores nulos por coluna:")
    print(df.isnull().sum())

    # Livros com 0 páginas
    livros_zero = df[df['paginas'] == 0]

    print("\nQuantidade de livros com 0 páginas:", len(livros_zero))
    print("\nRegistros com 0 páginas:")
    print(livros_zero)

    # Livros por ano
    livros_por_ano = df['ano'].value_counts().sort_index()

    print("\nQuantidade de livros por ano:")
    print(livros_por_ano)

    # Gráfico
    print("\nGerando gráfico...")
    livros_por_ano.plot(kind='bar')

    plt.title('Livros publicados por ano')
    plt.xlabel('Ano')
    plt.ylabel('Quantidade')

    plt.tight_layout()
    plt.show()


# Executa o programa
if __name__ == "__main__":
    main()