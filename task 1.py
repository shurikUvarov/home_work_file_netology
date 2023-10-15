import re
dishes = []
def GetData(file):
  recipes = {}
  dieshes = None
  ingredients = None
  with open(file, 'r+', encoding='utf-8') as f:
    for line in f.readlines():
      if len(line) > 1:
        if re.search(r'^\D+$', line):
          dieshes = re.search(r'^\D+$', line).group(0).replace('\n','')
          recipes[dieshes] = []
        elif re.search(r'(\w+)\s[|]\s(\w+)\s[|]\s(\w+)$', line):
          ingredients = re.search(r'(\w+)\s[|]\s(\w+)\s[|]\s(\w+)$', line)
          recipes[dieshes].append({'ingredient_name': ingredients.group(1), 'quantity': ingredients.group(2),
                                   'measure': ingredients.group(3)},)
  return recipes
cook_book = GetData('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
  cook_book = GetData('recipes.txt')
  shop_list = {}
  for dish in dishes:
    if dish in cook_book:
      ingredients = cook_book[dish]
      for ingredient in ingredients:
        ingredient_name = ingredient['ingredient_name']
        quantity = int(ingredient['quantity']) * person_count
        measure = ingredient['measure']

        if ingredient_name not in shop_list:
          shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
          shop_list[ingredient_name]['quantity'] += quantity
    else:
      print(f"Блюдо {dish} не найдено в книге рецептов.")
  return shop_list


shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель'], 2)
print(shop_list)

