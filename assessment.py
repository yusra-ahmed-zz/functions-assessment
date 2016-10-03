# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 
def item_total_cost(state, cost, tax=0.05):
    """Returns the final cost of an item after tax."""
    if state == "CA":
        tax = 0.07
    item_tax = tax * cost
    total_cost = cost + item_tax
    print "In the state of {}, the final cost would be {}".format(state, total_cost)
    

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".
def is_berry(fruit):
    """Returns True or False depending on fruit input"""
    if fruit == "strawberry":
        return True
    elif fruit == "blackberry":
        return True
    elif fruit == "cherry":
        return True
    else:
        return False
#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.
def shipping_cost(fruit):
    """Returns shipping cost using the is_berry function"""
    if is_berry(fruit) is True:
        return 0
    elif is_berry(fruit) is False:
        return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
def is_hometown(town_name):
    """Determines whether hometown given is True(mine) or False"""
    if town_name == "Hyderabad":
        return True
    else:
        return False

#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
def full_name(first, last):
    """Concatenates first and last name."""
    return first + " " + last
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you 
#        from?" depending on what `is_hometown()` evaluates to.
def hometown_greeting(town_name, first, last):
    """Prints a sentence using previous functions is_hometown and full_name"""
    if is_hometown(town_name) is True:
        print "Hi, {} {}, we're from the same place!".format(first, last)
    elif is_hometown(town_name) is False:
        print "Hi, {} {}, where are you from?".format(first, last)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.
def increment(x=1):
    def add(y):
        """Returns sum of two numbers."""
        return x+y
    return add
# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addfive with y = 5. Call again with y = 20.
addfive = increment(5)
print addfive(5)
print addfive(20)
# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################