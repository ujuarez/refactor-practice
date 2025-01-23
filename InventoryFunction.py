def InventoryFunction(inventory):
    inventory = {}
    inventory["apples"] = 10
    inventory["bananas"] = 5
    inventory["apples"] -= 3
    if inventory["apples"] <= 0:
        del inventory["apples"]
    print(inventory)