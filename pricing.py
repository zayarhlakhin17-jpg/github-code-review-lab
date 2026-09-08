def total_price(price, quantity):
    return price*quantity
def apply_coupon(total, percent):
    if percent < 0 or percent > 100:
        raise ValueError("Coupon percentage must be between 0 and 100")
    return total - (total * percent / 100)
