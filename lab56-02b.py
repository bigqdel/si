from sklearn import datasets
iris=datasets.load_iris()

x=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)
"""
def myIrisClassifier(db):
    predictions = []
    for db_record in db:
        if db_record[3] < 1.0:
            predictions.append(0)
        elif db_record[2] < 5:    #zmiana z 6.5
            predictions.append(1)
        else:
            predictions.append(2)
    return predictions
"""

#klasyfikator 1: drzewo decyzyjne
from sklearn import tree
#tworzenie drzewa na zbiorze treningowym

classifier1=tree.DecisionTreeClassifier()
classifier1.fit(x_train,y_train)
#ewaluacja drzewa na zbiorze testowym

predictions=classifier1.predict(x_test)
from sklearn.metrics import accuracy_score
print("Drzewo",accuracy_score(y_test,predictions))

"""
k-somsiadow
"""

#klasyfikator 2: k-najblizszychc sasiadow
#from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
#tworzenie drzewa na zbiorze treningowym

classifier2=KNeighborsClassifier()
classifier2.fit(x_train,y_train)
#ewaluacja drzewa na zbiorze testowym

predictions2=classifier2.predict(x_test)
from sklearn.metrics import accuracy_score
print("KNN",accuracy_score(y_test,predictions2))


"""
Naive Bayes
"""
#klasyfikator 3: NAive Bayes

from sklearn.naive_bayes import GaussianNB
#tworzenie drzewa na zbiorze treningowym

classifier3=GaussianNB()
classifier3.fit(x_train,y_train)
#ewaluacja drzewa na zbiorze testowym

predictions3=classifier3.predict(x_test)
from sklearn.metrics import accuracy_score
print("Naive Bayes",accuracy_score(y_test,predictions3))

"""
Multi-layer Perceptron
"""

#klasyfikator 4: NAive Bayes

from sklearn.naive_bayes import GaussianNB
#tworzenie drzewa na zbiorze treningowym

classifier4=GaussianNB()
classifier4.fit(x_train,y_train)
#ewaluacja drzewa na zbiorze testowym

predictions4=classifier4.predict(x_test)
from sklearn.metrics import accuracy_score
print("Multi-layer Perception",accuracy_score(y_test,predictions4))


