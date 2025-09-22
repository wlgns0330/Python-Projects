from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier

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

gauss = GaussianProcessClassifier()
gauss = gauss.fit(X, Y)

data = [[190, 90, 43]]
prediction = clf.predict(X)
nbr_prediction = nbr.predict(X)
gauss_prediction = gauss.predict(X)

if __name__ == "__main__":
    print(prediction)
    print(nbr_prediction)
    print(gauss_prediction)