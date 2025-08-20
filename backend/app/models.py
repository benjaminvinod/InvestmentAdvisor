import shap
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

# Dummy model setup
X, y = make_classification(n_samples=100, n_features=4, random_state=42)
model = RandomForestClassifier()
model.fit(X, y)

# SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

def generate_shap_plot():
    # Ensure the static directory exists
    shap_dir = os.path.join(os.path.dirname(__file__), 'static')
    os.makedirs(shap_dir, exist_ok=True)

    shap_path = os.path.join(shap_dir, 'shap_plot.png')

    # Generate SHAP summary plot
    plt.figure()
    shap.summary_plot(shap_values, X, show=False)
    plt.savefig(shap_path, bbox_inches='tight')
    plt.close()

    return shap_path  # full absolute path

