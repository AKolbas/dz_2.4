

#from pprint import pprint
cook_book = {}
with open('menu.txt', encoding='utf-8') as f:
    while True:
        dish = f.readline().strip()
        if not dish:
            break
        number_of_ingredients = f.readline().strip()
        ingredients = []
        for ingredient in range(int(number_of_ingredients)):
            ingredient_dictionary = {}
            ingredient = f.readline().strip().split('|')
            ingredient_name, quantity, measure = ingredient
            ingredient_dictionary['ingredient_name'] = ingredient_name
            ingredient_dictionary['quantity'] = int(quantity)
            ingredient_dictionary['measure'] = measure
            ingredients.append(ingredient_dictionary)
        cook_book[dish] = ingredients
        f.readline()
print(cook_book)
print('#' * 10)

def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish in dishes:
        #print(dish)
        for key, value in cook_book.items():
            if dish == key:
                #print(key)
                for description in value:
                    order_name = description['ingredient_name']
                    order_measure = description['measure']
                    order_quantity = int(description['quantity'])
                    if order_name in order.keys():
                        order[order_name]['quantity'] += order_quantity * person_count
                    else:
                        order[order_name] = {'measure': order_measure, 'quantity': order_quantity * int(person_count)}
    print(order)


get_shop_list_by_dishes(["Запеченный картофель", "Фахитос"], 4)


