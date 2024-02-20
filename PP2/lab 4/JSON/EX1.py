import json
with open('sample-date.json','r') as file:
    data = json.load(file)
x = data["imdata"]
print("Interface Status")
print("="*80)
print("DN                                 Description              Speed   MTU")
print("---------------------------------- ----------------------- -------- -------- ")
for i in x:
    print(i["l1PhysIF"]["attributes"]["dn"]," "*23, i["i1PhysIF"]["attributes"]["speed"]," "*1, i["l1PhysIF"],["attributes"],["mtu"])
    