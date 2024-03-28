from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'calculator/index.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'РЕЦЕПТЫ': reverse('recipes'),
        #'КАЛЬКУЛЯТОР': reverse('calculator'),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


DATA = {
    'Омлет': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'Паста': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'Бутерброд': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },

}
def recipes_view(request):
    template_name = 'calculator/recipes.html'
    recipes = DATA.keys()
    context = {
        'recipes': recipes
    }
    return render(request, template_name, context)

def recipe_view(request, recipe):
    template_name = 'calculator/recipe.html'
    num = int(request.GET.get("servings", 1))
    name = recipe
    rec = DATA[recipe].copy()
    for k, v in rec.items():
        rec[k] = round(v * num, 2)
    context = {
        'name': name,
        'recipe': rec,
        'num': num,
    }
    return render(request, template_name, context)

