MODEL_NAME = 'aditya_model1_adaboost.joblib'
ORIGINAL_FEATURES = ['age', 'sex', 'cp', 'trestbps', 'chol',
       'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope',
       'ca', 'thal']
FEATURES_TO_ENCODE = ['thal', 'slope', 'cp', 'restecg']
ONE_HOT_ENCODED_FEATURES = ['age', 'sex', 'trestbps', 'chol', 'fbs',
       'restecg', 'exang', 'oldpeak', 'ca', 'thal_0', 'thal_1',
       'thal_2', 'thal_3', 'slope_0', 'slope_1', 'slope_2',
       'cp_0', 'cp_1', 'cp_2',
       'cp_3', 'restecg_0', 'restecg_1', 'restecg_2']