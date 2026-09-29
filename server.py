def get_fabrics():
    return [{"id": 1, "name": "Шелк"}]

def create_order(order):
    print(f"Заказ принят: {order}")
    return {"status": "created"}