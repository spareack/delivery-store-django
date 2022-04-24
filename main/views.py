from django.shortcuts import render
from django.http import HttpResponseNotFound
from .models import Food, Categories
from django.template.defaulttags import register

import json
import traceback


@register.filter
def get_v(dictionary, key):
    return dictionary[key].get('filename')


@register.filter
def get_n(dictionary, key):
    return dictionary[key].get('name')


@register.filter
def get_p(dictionary, key):
    return dictionary[key].get('price')


@register.filter
def get_w(dictionary, key):
    return dictionary[key].get('weight')


@register.filter
def get_i(dictionary, key):
    return dictionary[key].get('id')


def main_page(request):
    if request.method == 'GET':
        try:
            all_categories = Categories.objects.all()
            all_categories = list(all_categories.values())

            cat_len = len(all_categories)
            data = {'categories': all_categories,
                    'range1': range(0, cat_len // 4 + (1 if cat_len % 4 != 0 else 0)),
                    'range2': range(0, 4),
                    'range0': range(0, cat_len // 2 + (1 if cat_len % 2 != 0 else 0)),
                    'range3': range(0, 2)}

            return render(request, "main/index.html", data)

        except Exception as e:
            print(str(e))
            print(traceback.format_exc())
            return HttpResponseNotFound('<h1>An error has occurred</h1>')


def show_category(request, category_id):
    if request.method == 'GET':
        try:
            category = Categories.objects.get(id=category_id)
            foods_ids = json.loads(category.food_list)

            all_foods = Food.objects.all()
            all_foods = list(all_foods.values())

            food_list = []
            for food in all_foods:
                if food['id'] in foods_ids:
                    food_list.append(food)

            food_len = len(food_list)

            data = {'food_list': food_list,
                    'category_name': category.name,
                    'range1': range(0, food_len // 4 + (1 if food_len % 4 != 0 else 0)),
                    'range2': range(0, 4),
                    'range0': range(0, food_len // 2 + (1 if food_len % 2 != 0 else 0)),
                    'range3': range(0, 2)}

            return render(request, "main/category.html", data)

        except Exception as e:
            print(str(e))
            print(traceback.format_exc())
            return HttpResponseNotFound('<h1>An error has occurred</h1>')


def show_meal(request, food_id):
    if request.method == 'GET':
        try:
            food = Food.objects.get(id=food_id)
            data = {'food': food}
            return render(request, "main/meal.html", data)

        except Exception as e:
            print(str(e))
            print(traceback.format_exc())
            return HttpResponseNotFound('<h1>An error has occurred</h1>')


def open_sales(request):
    if request.method == 'GET':
        return render(request, "main/sales.html")


# @application.route("/favicon.ico")
# def get_favicon():
#     return send_from_directory("static/media", 'favicon.ico')


