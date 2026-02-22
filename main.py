import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

np.random.seed(42)

def generate_light_curve(has_planet):
    time = np.linspace(0, 30, 300)
    brightness = np.ones(300)

    if has_planet:
        dip_center = np.random.uniform(10, 20)
        dip_width = 0.5
        dip_depth = np.random.uniform(0.003, 0.02)
        dip = dip_depth * np.exp(-(time - dip_center)**2 / (2 * dip_width**2))
        brightness -= dip

    noise = np.random.normal(0, 0.01, 300)
    brightness += noise

    return brightness

# Create dataset
X = []
y = []

for _ in range(1000):
    has_planet = np.random.choice([0, 1])
    curve = generate_light_curve(has_planet)
    X.append(curve)
    y.append(has_planet)

X = np.array(X)
y = np.array(y)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")

