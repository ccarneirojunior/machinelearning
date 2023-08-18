
#Calculating the Mean Absolute Error (MAE) from the KPI's 
import pandas as pd
# Load data
KPI_file_path = '../input/datapathway'
KPI_data = pd.read_csv(KPI_file_path) 
# Filter rows with missing values
filtered_KPI_data = KPI_data.dropna(axis=0)
# Choose target and features
y = filtered_KPI_data.Price
KPI_features = ['This', 'That']
X = filtered_KPI_data[KPI_features]

from sklearn.tree import DecisionTreeRegressor
# Define model
KPI_model = DecisionTreeRegressor()
# Fit model
KPI_model.fit(X, y)

from sklearn.metrics import mean_absolute_error

#Calculating the mean absolute error 
predicted_value = KPI_model.predict(X)
mean_absolute_error(y, predicted_value)

