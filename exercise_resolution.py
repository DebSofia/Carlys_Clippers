# names of the cuts offered at Carly’s Clippers
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
# price of each hairstyle in the hairstyles list.
prices = [30, 25, 40, 20, 20, 35, 50, 35]
# number of purchases for each hairstyle type in the last week.
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.
total_price = 0

for price in prices:
    total_price += price
    print(total_price)

average_price = total_price / len(prices)
print(average_price)

print('Average Haircut Price: ' + str(average_price))

# Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.

new_prices = [old_price - 5 for old_price in prices]
print(new_prices)

# Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
    print('Total Revenue: ' + str(total_revenue))

# Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

# Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30]
print(cuts_under_30)

print ('This project was fun to do')
