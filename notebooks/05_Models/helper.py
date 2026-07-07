import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

from sklearn.model_selection import cross_val_score, train_test_split, GridSearchCV
from sklearn.metrics import recall_score, accuracy_score, f1_score, roc_auc_score, roc_curve, classification_report, confusion_matrix

from imblearn.pipeline import Pipeline
from imblearn.over_sampling import SMOTE

def roc_auc_curve(best_model, X_test, y_test):

    y_probs = best_model.predict_proba(X_test)[:, 1]

    fpr, tpr, thresholds = roc_curve(y_test, y_probs)
    roc_auc = roc_auc_score(y_test, y_probs)

    plt.figure(figsize=(8,6))
    plt.plot(fpr, tpr, color='blue', label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='red', linestyle='--')  
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic (ROC) Curve')
    plt.legend(loc="lower right")
    plt.show()

def heat_map(cm):

    plt.figure(figsize=(6,5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)

    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix Heatmap')
    plt.show()

def evaluate(model, X_test, y_test, y_pred):
        
        y_pred = model.predict(X_test)
        cm = confusion_matrix(y_test, y_pred)

        accuracy = accuracy_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        print(f'Accuracy: {accuracy:.3f}')
        print(f'Recall: {recall:.3f}')
        print(f'F1: {f1:.3f}')

        heat_map(cm=cm)



class build_PipieLine:

    def __init__(self, model, X, y):
        self.model = model 
        self.X = X 
        self.y = y 
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42, stratify=self.y)
        self.y_pred = None
        self.pipeline = None 
        self.best_model = None 

    def build(self):
        pipeline = Pipeline([
        ('smote', SMOTE(random_state=42)),
        (f'model_{self.model.__class__.__name__}', self.model)
    ])
        return pipeline

    def train(self):
        self.pipeline = self.build()
        self.pipeline.fit(self.X_train, self.y_train)
        return self.pipeline

    def cv(self, params_grid):
        
        if self.pipeline is None:
            self.pipeline = self.build()

        cv = GridSearchCV(
            self.pipeline,
            params_grid,
            cv=5,
            scoring='recall',  
            n_jobs=-1
        )
        

        cv.fit(self.X_train, self.y_train)

        self.best_model = cv.best_estimator_

        return cv 
    
    def evaluate(self, model):

        self.y_pred = model.predict(self.X_test)
        cm = confusion_matrix(self.y_test, self.y_pred)

        accuracy = accuracy_score(self.y_test, self.y_pred)
        recall = recall_score(self.y_test, self.y_pred)
        f1 = f1_score(self.y_test, self.y_pred)

        print(f'Accuracy: {accuracy:.3f}')
        print(f'Recall: {recall:.3f}')
        print(f'F1: {f1:.3f}')

        heat_map(cm=cm)



