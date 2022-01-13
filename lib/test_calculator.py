def calculate_test(annual_usage, orientation):
    el_price = 2.3
    price = 0
    production = 0
    if orientation == 'west':
        price = el_price * 0.9 * annual_usage
        production = 1000
    elif orientation == 'east':
        price = el_price * 0.7 * annual_usage
        production = 2000

    return {
        "price": price,
        "production": production
    }
