from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# carregar dataset
iris = load_iris()

X = iris.data  # caracteristicas 
y = iris.target # rótulos ()

# print()
# dividir os dados
# 70% treino x 30 % teste
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

# criar o modelo
model =  DecisionTreeClassifier()
model.fit(X_train, y_train)

# previsão 
y_pred = model.predict(X_test)
# print(y_test)


# acuracia qualidade do aprendizado
accuracy = accuracy_score(y_test, y_pred)
print(y_pred)
print('Acuracia do modelo', accuracy)



