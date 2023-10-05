# -*- coding: UTF-8 -*-
#cook_boock = open('recipes.txt','r+', encoding='utf-8')
import re
dishes = []
def GetData(file)->dict:
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
  local_cook_book = GetData('recipes.txt')
  shop_list = {}
  for k in dishes:
    if shop_list.get(local_cook_book[k][0]['ingredient_name']):
      shop_list[local_cook_book[k][0]['ingredient_name']] = { 'measure' : local_cook_book[k][0]['measure'],
                                                            'quantity':  shop_list[local_cook_book[k][0]['ingredient_name']]['quantity'] +
                                                                         (int(local_cook_book[k][0]['quantity'])*person_count)}
    else:
      shop_list[local_cook_book[k][0]['ingredient_name']] = {'measure': local_cook_book[k][0]['measure'],
                                                             'quantity': int(local_cook_book[k][0]['quantity']) * person_count}
  return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель'], 2))
#for k in cook_book:
#  dishes.append(k)
#print(dishes)

