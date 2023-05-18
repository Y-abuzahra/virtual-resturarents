from trre_node import TreeNode
from restaurantData import types, restaurant_data
from naive_pattern_search import naive_pattern_search

def welcome():
    print("Welcome to SoHo Restuarants")
    print("What type of food would you like to eat?")
    for type in types:
        print(type)
    return 

def building_the_tree():
    root = TreeNode(input("Type the beginning of that food and press enter to see if it's here.\n"))
    for type in types:
        type = TreeNode(type)
        root.add_child(type)

    for type in root.children:
        for restaurant in restaurant_data:
            if restaurant[0] == type.value:
                type.add_child(TreeNode(restaurant))
    return root

    
def searching_for_cuisuine():
    root = building_the_tree()
    resualts = []
    for child in root.children:
        if naive_pattern_search(child.value, root.value):
            resualts.append(child)
    if len(resualts) == 1:
        return resualts[0]
    elif len(resualts) == 0:
        print('there is no cusines starting with this letter(s)')
        return searching_for_cuisuine()
    else:
        print(f"With Those beginning letters, your choices are {[resault.value for resault in resualts]}")
        return searching_for_cuisuine()

def showing_restaurants(cuisuine):
    restaurants = input(f"The only option with those beginning letters is {cuisuine.value}. Do you want to look at {cuisuine.value} restaurants?. Enter 'y' for yes and 'n' for no\n")
    if restaurants == "y":
        for restuarant in cuisuine.children:
            print(f"Name: {restuarant.value[1]}\nPrice: {restuarant.value[2]}/5\nRating {restuarant.value[3]}/5\nAddress: {restuarant.value[4]}\n\n")
        goodbye()

    else:
        goodbye()


def goodbye():
    again = input("Do You want to find other restuarants. 'y' for yes 'n' for no\n")
    if again == "y":
        showing_restaurants(searching_for_cuisuine())
    else:
        print("Thanks you for using our app")

welcome()
showing_restaurants(searching_for_cuisuine())