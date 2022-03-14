from nornir import InitNornir

nr = InitNornir("config.yaml")


nr_inventory = nr.inventory.hosts

data = []

print(list(nr.inventory.dict()["hosts"].values()))

# for host in nr_inventory:
#     host_dict = nr_inventory[host].dict()
#     device_data = [
#         host_dict["name"],
#         host_dict["hostname"],
#         host_dict["platform"],
#         host_dict["data"]["role"],
#         ",".join(host_dict["groups"])
#     ]
#     data.append(device_data)

# print(data)