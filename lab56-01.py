from sklearn import datasets
iris=datasets.load_iris()

x=iris.data
y=iris.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)

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





from sklearn.metrics import accuracy_score
predictions = myIrisClassifier(x_test)
print(accuracy_score(y_test,predictions))
#print (iris)