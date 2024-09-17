#Initialize the Inventory Manager:
from inventory_manager import InventoryManager

stock_data = {
    'date': ['2024-09-01', '2024-09-02', '2024-09-03'],
    'stock_level': [100, 90, 80]
}

manager = InventoryManager(stock_data)

#Train the Model:
manager.train_model()

#Check for Reordering Triggers:
manager.reorder_trigger(threshold=50)
