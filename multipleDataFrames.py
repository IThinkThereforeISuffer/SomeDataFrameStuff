import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

all_data = visits.merge(cart, how="left").merge(checkout, how="left").merge(purchase, how="left")

null_cart = all_data[all_data.cart_time.isnull()]
percent_not_carting = 1.0 * len(null_cart)/len(all_data)
print(percent_not_carting)

null_checkout = all_data[all_data.checkout_time.isnull() & ~all_data.cart_time.isnull()]
percent_not_checkout = 1.0 * len(null_checkout)/len(all_data)
print(percent_not_checkout)

null_purchase = all_data[all_data.purchase_time.isnull() & ~all_data.checkout_time.isnull()]
percent_not_purchase = 1.0 * len(null_purchase)/len(all_data)
print(percent_not_purchase)

all_data["time_to_purchase"] = all_data.purchase_time - all_data.visit_time

print(all_data.time_to_purchase.mean())
