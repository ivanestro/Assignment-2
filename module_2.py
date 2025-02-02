"""This is the assignment 2 for module 2."""

# SIMPLE DATA TYPES

name = "Ivan" 
license = True
current_year = 2025
print(f"name:", name, "type:",type(name)) 
print(f"has license:", license, "type:", type(license))
print(f"this year:", current_year, "type:", type(current_year))

current_year +=1
print(f"next year: ", current_year, "type:", type(current_year))

# MATHEMATICAL OPERATIONS
gst = 0.05 
pst = 0.07
purchase_price = 60000.01
total_price = (purchase_price * (pst + gst)) + purchase_price

gst = purchase_price * gst
pst = purchase_price * pst
print("Purchase Price:", purchase_price ,"Provincial Tax:",gst ,"Federal Tax:",pst ,"Total:", total_price)
print(f"Purchase Price: ${purchase_price:.2f}", f"Provincial Tax: ${gst: .2f}", f"Federal Tax: ${pst: .2f}", f"Total: ${total_price: .2f}")

# LISTS
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

numbers.insert(6,name)
print(numbers)

numbers.remove(9)
print(numbers)

new_list = ["A","B","C"]

both_list = new_list + numbers
print(both_list)

provinces_and_territories = ("MB", "AB", "BC", "ON")
ontario = provinces_and_territories[3]
print(ontario)

# DICTIONARIES

money = {'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}
catch_money = money['quarter']
print(type(money))
print(catch_money)

money['nickel'] = 5
money['dime'] = 10
money['quarter'] = 25
print(money)

money['Loonie'] = 100 
money['Toonie'] = 200
print(money)
