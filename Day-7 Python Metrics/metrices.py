from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import metrics
c="cat"
d="dog"
f="fox"
y_true=[c,c,c,c,c,c,f,f,f,f,f,f,f,f,f,f,d,d,d,d,d,d,d,d,d]
y_pred=[c,c,c,c,d,f,c,c,c,c,c,d,d,f,f,c,c,c,d,d,d,d,d,d,d]
print("confusion matrix")
print(confusion_matrix(y_true,y_pred))
print(classification_report(y_true, y_pred,digits=3))
y_test=[1,0,1,0,1,0]
y_pred=[1,0,0,1,0,1]
prop=[0.7,0.4,0.6,0.5,0.2,0.3]
print(f'Precision : {metrics.precision_score(y_test,y_pred)}')
print(f'Recall : {metrics.recall_score(y_test,y_pred)}')
print(f'F1 score : {metrics.f1_score(y_test,y_pred)}')
print(f'Roc_Auc : {metrics.roc_auc_score(y_test,prop)}')