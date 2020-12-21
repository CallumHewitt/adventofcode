from input_utils import *
import re
import copy


def solve_1(data):
    recipes = [parse_line(line) for line in data]
    risky_ingredients_by_allergen = calculate_risky_ingredients_by_allergen(
        recipes)
    all_risk_ingredients = set(
        [ingredient for ingredients in risky_ingredients_by_allergen.values() for ingredient in ingredients])
    safe_ingredients_occurrences = [
        ingredient for recipe in recipes for ingredient in recipe[0] if ingredient not in all_risk_ingredients]
    return len(safe_ingredients_occurrences)


def parse_line(line):
    search = re.search("(.*) \(contains (.*)\)", line)
    return (search.group(1).split(" "), search.group(2).split(", "))


def calculate_risky_ingredients_by_allergen(recipes):
    risky_ingredients_by_allergen = {}
    for recipe, allergens in recipes:
        for allergen in allergens:
            if (not allergen in risky_ingredients_by_allergen):
                risky_ingredients_by_allergen[allergen] = recipe
            else:
                existing_allergens = risky_ingredients_by_allergen[allergen]
                risky_ingredients_by_allergen[allergen] = list(
                    filter(lambda existing: existing in recipe, existing_allergens))
    return risky_ingredients_by_allergen


def solve_1(data):
    recipes = [parse_line(line) for line in data]
    unsafe_ingredients_by_allergen = calculate_unsafe_ingredients_by_allergen(recipes)
    unsafe_ingredients = [ingredient for _, ingredient in sorted(unsafe_ingredients_by_allergen.items())]
    return ",".join(unsafe_ingredients)


def calculate_unsafe_ingredients_by_allergen(recipes):
    risky_ingredients_by_allergen = calculate_risky_ingredients_by_allergen(
        recipes)
    change = True
    while(change):
        change = False
        updated_risky_ingredients_by_allergen = copy.deepcopy(
            risky_ingredients_by_allergen)
        for allergen, ingredients in risky_ingredients_by_allergen.items():
            if (len(ingredients) == 1):
                ingredient = ingredients[0]
                for other_allergen, other_ingredients in updated_risky_ingredients_by_allergen.items():
                    if (ingredient in other_ingredients and other_allergen != allergen):
                        other_ingredients.remove(ingredient)
                        change = True
        risky_ingredients_by_allergen = updated_risky_ingredients_by_allergen
    return dict(map(lambda item: (item[0], item[1][0]), risky_ingredients_by_allergen.items()))


print('Part 1')
print(f"Answer: {solve_1(get_input_as_list(1))}")
