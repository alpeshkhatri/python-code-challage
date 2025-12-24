def update_inventory(inventory, shipment):
    inventory_dict = {item: qty for qty, item in inventory}
    new_items = []
    
    for qty, item in shipment:
        if item in inventory_dict:
            inventory_dict[item] += qty
        else:
            new_items.append([qty, item])
            inventory_dict[item] = qty
    
    return [[inventory_dict[item], item] for _, item in inventory] + new_items
