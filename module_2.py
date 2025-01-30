"""This is the assignment 2 for module 2."""

# SIMPLE DATA TYPES

name = "Ivan"
license = True
current_year = 2025

gst = 0.05
pst = 0.07
purchase_price = 60000.01
total_price = (purchase_price * (pst + gst)) + purchase_price

print(f"name:", name, "type:",type(name)) 
print(f"has license:", license, "type:", type(license))
print(f"this year:", current_year, "type:", type(current_year))

current_year +=1
print(f"next year: ", current_year, "type:", type(current_year))

# MATHEMATICAL OPERATIONS
gst = purchase_price * gst
pst = purchase_price * pst
print("Purchase Price:", purchase_price ,"Provincial Tax:",gst ,"Federal Tax:",pst ,"Total:", total_price)
print(f"Purchase Price:${purchase_price:.2f}", f"Provincial Tax: ${gst: .2f}", f"Federal Tax: ${pst: .2f}", f"Total: ${total_price: .2f}")