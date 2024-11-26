# Список покупок
purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

# Функция для подсчёта общей выручки
def total_revenue(purchases):
    revenue = sum(item["price"] * item["quantity"] for item in purchases if item["item"] != "banana")
    return revenue

# Функция для группировки товаров по категориям
def items_by_category(purchases):
    categories = {}
    for item in purchases:
        category = item["category"]
        if category not in categories:
            categories[category] = []
        if item["item"] not in categories[category]:
            categories[category].append(item["item"])
    return categories

# Функция для фильтрации дорогих покупок
def expensive_purchases(purchases, min_price):
    return [item for item in purchases if item["price"] >= min_price]

# Функция для подсчёта средней цены товаров по категориям
def average_price_by_category(purchases):
    categories = {}
    for item in purchases:
        category = item["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(item["price"])
    return {category: round(sum(prices) / len(prices), 2) for category, prices in categories.items()}

# Функция для нахождения категории с наибольшим количеством проданных товаров
def most_frequent_category(purchases):
    category_sales = {}
    for item in purchases:
        category = item["category"]
        category_sales[category] = category_sales.get(category, 0) + item["quantity"]
    return max(category_sales, key=category_sales.get)

# Генерация отчёта
def generate_report(purchases):
    print(f"Общая выручка: {total_revenue(purchases)}")
    print(f"Товары по категориям: {items_by_category(purchases)}")
    print(f"Покупки дороже 1.0: {expensive_purchases(purchases, 1.0)}")
    print(f"Средняя цена по категориям: {average_price_by_category(purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")

# Вызов генерации отчёта
generate_report(purchases)