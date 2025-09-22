from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier

# [height, weight, shoe size]
X = [[181, 80, 44],
     [177, 70, 43],
     [160, 60, 38],
     [154, 54, 37],
     [166, 64, 40],
     [190, 90, 47],
     [175, 64, 39],
     [177, 70, 40],
     [171, 75, 42],
     [181, 85, 43]]

Y = ['male', 'female', 'female', 'female', 'male',
     'male', 'male', 'female', 'female', 'male']

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

nbr = KNeighborsClassifier()
nbr = nbr.fit(X, Y)

data = [[190, 90, 43]]
prediction = clf.predict(data)
nbr_prediction = nbr.predict(data)

if __name__ == "__main__":
    print(prediction)
    print(nbr_prediction)