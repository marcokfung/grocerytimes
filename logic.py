import json
zipcode = "94103"
user_price_level= "All"
week_day = "Sunday"
hour = 12

if week_day== "Sunday":
    week_day_index = 6
elif week_day== "Saturday":
    week_day_index = 5
elif week_day== "Friday":
    week_day_index = 4
elif week_day== "Thursday":
    week_day_index = 3
elif week_day== "Wednesday":
    week_day_index = 2
elif week_day== "Tuesday":
    week_day_index = 1
elif week_day== "Monday":
    week_day_index = 0

# Step 1: Zipcode Logic Filter
zipcode_filepath = "finalData/" + zipcode+"_final_data.json"

with open(zipcode_filepath, 'r') as fp:
    data = json.load(fp)

# Step 2: Price Level in Zipcode
price_list = []
print(len(data))
if user_price_level == "All":
    price_list = data.keys()
else:
    for shop in data.values():
        if shop.get("price_level") == user_price_level:
            price_list.append(shop.get("id"))

print (len(price_list))

# Step 3: return sorted list by populatrtimes
pid_pt_dict = {}
for shop_pid in price_list:
    #print(shop_pid)
    shop = data.get(shop_pid) 
    pt_list = shop.get("populartimes")
    if pt_list != None:
        pop_time = pt_list[week_day_index].get('data')[hour]
        pid_pt_dict[shop_pid] = pop_time

pid_pt_dict = sorted(pid_pt_dict.items(), key=lambda x: x[1])

#print (pid_pt_dict)

# Step 4 Return Values
for pid,pt in pid_pt_dict:
    shop = data.get(pid)
    name = shop.get("name")
    address = shop.get("address")
    phone = shop.get("international_phone_number")
    rating = shop.get("rating")
    number_of_rating = shop.get("rating_n")
    keywords = shop.get("types")
    price_level_display = shop.get("price_level")
    print("pid : " + pid)
    print (name, address, phone, rating, number_of_rating, keywords, price_level_display)