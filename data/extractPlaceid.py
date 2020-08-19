import json
import populartimes

with open('data/94134_grocery.json', 'r', encoding="utf8") as f:
    pid_json_list= json.load(f)

results = pid_json_list.get('results')
grocery_info= {}
api_key = "key"

for entry in results:
    pid = entry.get("place_id")
    p_level = entry.get("price_level")
    x = populartimes.get_id(api_key, pid)
    x["price_level"] = p_level
    grocery_info[pid] = x
# print(grocery_info)
with open('finalData/94134_final_data.json', 'w') as fp:
    json.dump(grocery_info, fp, indent=4)

