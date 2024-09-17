import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import smtplib
from email.mime.text import MIMEText

class InventoryManager:
    def __init__(self, stock_data):
        self.stock_data = pd.DataFrame(stock_data)
        self.model = None

    def train_model(self):
        self.stock_data['date'] = pd.to_datetime(self.stock_data['date'])
        self.stock_data['day'] = self.stock_data['date'].dt.dayofyear
        X = self.stock_data[['day']].values
        y = self.stock_data['stock_level'].values
        self.model = LinearRegression().fit(X, y)
    
    def predict_stock(self, days_in_advance):
        last_day = self.stock_data['day'].max()
        future_days = np.array([[last_day + i] for i in range(1, days_in_advance + 1)])
        return self.model.predict(future_days)
    
    def reorder_trigger(self, threshold):
        future_stock = self.predict_stock(7)  # Predicting 7 days in advance
        if future_stock[-1] < threshold:
            self.send_reorder_notification()
    
    def send_reorder_notification(self):
        msg = MIMEText("Stock level is below threshold. Time to reorder.")
        msg['Subject'] = 'Reorder Alert'
        msg['From'] = 'inventory@yourcompany.com'
        msg['To'] = 'manager@yourcompany.com'

        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)

# Sample usage
stock_data = {
    'date': ['2024-09-01', '2024-09-02', '2024-09-03'],
    'stock_level': [100, 90, 80]
}

manager = InventoryManager(stock_data)
manager.train_model()
manager.reorder_trigger(threshold=50)
