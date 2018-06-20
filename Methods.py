# -*- coding: utf-8 -*-
# @Time    : 18-6-20 下午4:48
# @Author  : BlvinDon
# @Email   : wenbingtang@hotmail.com
# @File    : Methods.py
# @Software: PyCharm
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
from HAR.Get_Data import Get_data
X,Y = Get_data()
# print(Y)
le.fit(Y)
X,Y = X,le.transform(list(Y))
from collections import Counter
values_counts = Counter(Y)
print("样本类别统计：",values_counts)
# from imblearn.over_sampling import RandomOverSampler
# ros = RandomOverSampler(random_state=0)
# from imblearn.combine import SMOTEENN
# smote_tomek = SMOTEENN(random_state=0)
# X_resampled, y_resampled = smote_tomek.fit_sample(X, Y)
# values_counts = Counter(y_resampled)
# print("SMOTE采样后样本类别统计：",values_counts)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)
# values_counts = Counter(y_train)
# print("训练集样本类别统计：",values_counts)
# values_counts = Counter(y_test)
# print("测试集样本类别统计：",values_counts)

from sklearn import svm
#
clf1 = svm.SVC(kernel='rbf')
clf1.fit(X_train,y_train)
y_predict = clf1.predict(X_test)


# from sklearn.ensemble import RandomForestClassifier
# clf2 = RandomForestClassifier(n_estimators=4)
# clf2.fit(X_train,y_train)
# y_predict = clf2.predict(X_test)
#
# from sklearn.naive_bayes import GaussianNB
# clf3 = GaussianNB()
# y_predict = clf3.fit(X_train, y_train).predict(X_test)

# from sklearn import tree
# clf4 = tree.DecisionTreeClassifier()
# clf4.fit(X_train,y_train)
# y_predict = clf4.predict(X_test)

# from sklearn.neural_network import MLPClassifier
# clf5 = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(15, 3), random_state=1)
# clf5.fit(X_train,y_train)
# y_predict = clf5.predict(X_test)

# from sklearn import tree
# clf6 = tree.DecisionTreeClassifier(class_weight={5:5.99,4:8.91,3:9.83,2:197,1:6.59,0:8.93})
# clf6.fit(X_train,y_train)
# y_predict = clf6.predict(X_test)

target_names = le.inverse_transform([0,1,2,3,4,5])
from sklearn.metrics import classification_report
print(classification_report(y_test,y_predict))
# print(le.inverse_transform([1,2,3,4,5]))
from collections import Counter
values_counts = Counter(Y)
print("样本类别统计：",values_counts)
values_counts = Counter(y_train)
print("训练集样本类别统计：",values_counts)
values_counts = Counter(y_test)
print("测试集样本类别统计：",values_counts)
print(le.inverse_transform([0,1,2,3,4,5]))
print([0,1,2,3,4,5])