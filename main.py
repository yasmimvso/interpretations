import csv
import json

# action_ref + unit_num_ref +  unit_obj_ref + obj_ref + action_dt + obj_num_dt + unit_impact + obj_d
data = []

with open("data.json", mode="r") as fl:
    data = json.load(fl)

with open("interpretations.csv", mode="w") as fl:
    fields = [
        "action_ref", "obj_ref", "obj_num_ref", "unit_obj_ref", "action_dt",
        "obj_dt", "obj_num_dt", "unit_impact", "category", "reference"
    ]

    wr = csv.DictWriter(fl, fieldnames=fields)
    wr.writeheader() 

    for row in data["data"]:
        wr.writerow(row)