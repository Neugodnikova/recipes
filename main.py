def get_shop_list_by_dishes(dishes, person_count):
    with open('recipes.txt', encoding='utf-8') as f:
        cook_book = {}
        for line in f:
            dish = line.strip()
            count_ingredients = int(f.readline())
            ingredients = []
            for i in range(count_ingredients):
                ingredient = f.readline().strip()
                ingredient_name, quantity, measure = ingredient.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            f.readline()
            cook_book[dish] = ingredients
        print(f'cook_book = {cook_book}')
    shop_list_by_dishes = {}
    for every_dish in dishes:
        if every_dish in cook_book.keys():
            for every_ingredients in cook_book[every_dish]:
                key = every_ingredients['ingredient_name']
                if key not in shop_list_by_dishes.keys():
                    meas = every_ingredients['measure']

                    shop_list_by_dishes[key] = {'quantity': int(every_ingredients['quantity']) * person_count, 'measure': meas}
                else:
                    shop_list_by_dishes[key]['quantity'] += int(every_ingredients['quantity']) * person_count

    return (shop_list_by_dishes)
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
