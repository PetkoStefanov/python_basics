holiday_price = float(input())
puzzles = int(input())
talk_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

order_price = ((puzzles * 2.60) + (talk_dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2))

order_number = puzzles + talk_dolls + bears + minions + trucks

if order_number >= 50:
    discounted_price = order_price - (order_price * 0.25)
    order_price = discounted_price

total_order_price = order_price - (order_price * 0.10)

if total_order_price >= holiday_price:
    total = "%.2f" % (total_order_price - holiday_price)
    print(f"Yes! {total} lv left.")
else:
    total = "%.2f" % (holiday_price - total_order_price)
    print(f"Not enough money! {total} lv needed.")
