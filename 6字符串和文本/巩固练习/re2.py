types_of_people = 10
x = f"There are {types_of_people} types of people."     # here!

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."  # here!

print(x)
print(y)

print(f"I said: {x}")                                   # here!
print(f"I also said: '{y}")                             # here!

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))                # here! (confused)

w = "This is the left side of..."
e = "a string wirh a right side"

print(w + e)                                            # here! (confused)