def shopping_list(item):
    shopping_list = ["apples", "bananas", "carrots"]
    shopping_list.append("dates")
    shopping_list.remove("bananas")
    for item in shopping_list:
        print(item)