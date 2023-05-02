from sklearn.linear_model import LinearRegression

# Dados de treinamento
X_train = [[100], [150], [200], [250], [300]] # Área da casa em metros quadrados
y_train = [100000, 150000, 200000, 250000, 300000] # Preço da casa em reais

# Criação do modelo de regressão linear
model = LinearRegression()

# Treinamento do modelo
model.fit(X_train, y_train)

# Previsão do preço de uma casa com base em sua área
area = [[175]] # Área da casa que queremos prever o preço
price = model.predict(area)

print('Preço estimado da casa:', price[0])