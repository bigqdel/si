import matplotlib.pyplot as plt 
from sklearn import datasets
iris=datasets.load_iris()
breast=datasets.load_breast_cancer()

x=breast.data
y=breast.target

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
from sklearn.metrics import confusion_matrix
print("Drzewo",accuracy_score(y_test,predictions))
print("Drzewo\n",confusion_matrix(y_test,predictions))

"""
k-somsiadow
"""

#klasyfikator 2: k-najblizszychc sasiadow
#from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
#tworzenie drzewa na zbiorze treningowym

classifier2=KNeighborsClassifier()
classifier2.fit(x_train,y_train)
#ewaluacja drzewa na zbiorze testowym

predictions2=classifier2.predict(x_test)
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
print("KNN",accuracy_score(y_test,predictions2))
print("KNN\n",confusion_matrix(y_test,predictions2))



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
from sklearn.metrics import confusion_matrix
print("Naive Bayes",accuracy_score(y_test,predictions3))
print("Naive Bayes\n",confusion_matrix(y_test,predictions3))

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
from sklearn.metrics import confusion_matrix
print("Multi-layer Perception",accuracy_score(y_test,predictions4))
print("Multi-layer Perception\n",confusion_matrix(y_test,predictions4))

"""
 Forests of randomized trees
"""

#klasyfikator xxx:  Forests of randomized trees

from sklearn.ensemble import RandomForestClassifier
#tworzenie drzewa na zbiorze treningowym

classifier5=RandomForestClassifier()
classifier5.fit(x_train,y_train)
#ewaluacja drzewa na zbiorze testowym

predictions5=classifier5.predict(x_test)
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
print(" Forests of randomized trees",accuracy_score(y_test,predictions5))
print(" Forests of randomized trees\n",confusion_matrix(y_test,predictions5))


"""
wykres

"""

os_x=["Drzewo","somsiad","Naive Bayes","multi-layer",]
os_y=[accuracy_score(y_test,predictions),accuracy_score(y_test,predictions2),accuracy_score(y_test,predictions3),accuracy_score(y_test,predictions4)]
plt.bar(os_x, os_y, width=0.1, label='dokladnosc', color='red')
#plt.bar(ypos+0.2, Printers, width=0.2, label='Printers', color='green')
#give title
plt.title('porownanie klasyfikatorow')
plt.xticks(os_x)
plt.xlabel('klasyfikatory')
plt.ylabel('dokladnosc')
#plt.plot(ypos, Year) will remove the numbers along the y-axis
#shows legend
plt.legend()
#show to show the graph
plt.show()