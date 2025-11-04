import time

def get_product_details(product_id):
    # Simulate slow DB/API call
    time.sleep(2)
    return f"Product {product_id} - Data loaded from DB"
