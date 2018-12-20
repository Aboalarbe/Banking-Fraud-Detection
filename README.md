# Banking-Fraud-Detection
according the dataset most of 'isFruad'most of values is 0 that`s mean is not fruad "Normal Transaction" and there are less values is 1 that`s mean is fruad so the data is not balanced with ratio 90% not fruad and 10% fruad "Normal Case".
we will increase the values of is fraud using SMOTE algoirthm using imblearn to make the data balanced and avoiding Overfit.

Oversampling is a well-known way to potentially improve models trained on imbalanced data. But it’s important to remember that oversampling incorrectly can lead to thinking a model will generalize better than it actually does. Random forests are great because the model architecture reduces overfitting, but poor sampling practices can still lead to false conclusions about the quality of a model.
