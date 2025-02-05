import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Carregar os dados
most_popular_products = pd.read_csv("/mnt/data/most_popular_products.csv")
sales_by_country = pd.read_csv("/mnt/data/sales_by_country.csv")
sales_by_marketplace = pd.read_csv("/mnt/data/sales_by_marketplace.csv")

# Criar a aplicação Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard de Vendas Meganium"),
    
    dcc.Graph(
        figure=px.bar(most_popular_products, x='delivery_country', y='quantity', color='product_sold',
                      title='Produtos Mais Populares por País', labels={'quantity': 'Quantidade Vendida', 'delivery_country': 'País'})
    ),
    
    dcc.Graph(
        figure=px.pie(sales_by_country, names='delivery_country', values='quantity',
                      title='Distribuição de Vendas por País')
    ),
    
    dcc.Graph(
        figure=px.bar(sales_by_marketplace, x='Marketplace', y='quantity',
                      title='Vendas por Marketplace', labels={'quantity': 'Quantidade Vendida'})
    )
])

# Rodar o servidor
if __name__ == "__main__":
    app.run_server(debug=True)
