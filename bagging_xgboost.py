from sklearn import model_selection
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
import pandas as pd
import numpy as np
import pickle
  
# load the data
dataset = pd.read_csv('dataset9000.data', header = None)
print(dataset.head())
X = np.array(dataset.iloc[:, 0:17]) 
print(X)
Y = np.array(dataset.iloc[:, 17])
print(Y)
dataset.columns = ["Database Fundamentals","Computer Architecture","Distributed Computing Systems",
"Cyber-Security","Networking","Development","Programming Skills","Project Management",
"Computer Forensics Fundamentals","Technical Communication","AI ML","Software Engineering","Business Analysis",
"Communication skills","Data Science","Troubleshooting-skills","Graphics Designing","Roles"]
dataset.dropna(how ='all', inplace = True)

# Encode the labels (convert job names to numeric values)
le = LabelEncoder()
Y = le.fit_transform(Y)

  
seed = 5 
kfold = model_selection.KFold(n_splits=15, random_state=seed, shuffle=True)

# XGBoost Classifier - Better than Bagging
model = XGBClassifier(
    n_estimators=100,           # Number of boosting rounds
    max_depth=6,                # Maximum depth of trees
    learning_rate=0.1,          # Learning rate
    subsample=0.8,              # Subsample ratio of training instances
    colsample_bytree=0.8,       # Subsample ratio of features
    random_state=seed,
    eval_metric='mlogloss',     # For multi-class classification
    verbosity=1
)
  
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print("Accuracy with XGBoost:", results.mean()*100)

# Train final model on full data
model.fit(X, Y)

# Save the model and label encoder
pickle.dump(model, open("careerlast.pkl", 'wb'))
pickle.dump(le, open("label_encoder.pkl", 'wb'))
print("Model saved as careerlast.pkl")
print("Label encoder saved as label_encoder.pkl")
