"""Calclating teabag info for amount of guest at tea party"""

__author__: str = "730766558"


# Step 4: Defining main_planner Function
def main_planner(guests: int) -> None:
    """Purpose is to be main entrypoint of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    return None


# printing cost was is confusing.
# cost has tea_count and treat_count but uses tea-bags and treats
# took so long to figure out i thought you needed parameter names to call it idk why. Understand now after watching vids + slides.


# Step 1: Defining a teabag function
def tea_bags(people: int) -> int:
    """Plan for amount of tea bags per person (2 per person)"""
    return people * 2


# Step 2: Defining a treats function
def treats(people: int) -> int:
    """Plan for amount of treats. For each tea bag, 1.5 treats."""
    return round(
        tea_bags(people=people) * 1.5
    )  # took longer than 2 mins. Had to figure out keyword argument


# Questions: Calling tea_bags allows for
# us to not have to repeat equations.
# If we need to edit we would only have to edit tea_bags.


# Step 3: Defining the cost Function
def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


# Took me the longest prob like 25 mins. I tried to make the parameters the previous functions & had issues w/ step 4

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))

# Questions: The if statement needs above info as it's read top down. it'll look for main_planner but it won't find it. It's not in the frame yet.
