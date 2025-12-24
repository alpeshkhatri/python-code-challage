def update_inventory(inventory, shipment):
    newinventory=[]
    shipment_items = {i:q for q, i in shipment}
    for quantity, item in inventory:
        if item in shipment_items:  
            newinventory.append([quantity+shipment_items[item],item])
            shipment_items.pop(item)
        else:
            newinventory.append([quantity, item])
    for item, quantity in shipment_items.items():
        newinventory.append([quantity, item])
    print(shipment_items)
    print(newinventory)
    print("\n")
    return newinventory