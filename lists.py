emptyAnimals = list()
print(emptyAnimals)  # []
emptyAnimals = []
print(emptyAnimals)  # []

domesticAnimals = ["Dog", "Cat", "Parrot"]
wildAnimals = ["Tiger"]

# Sequence operator:
print("domesticAnimals[1]", domesticAnimals[1])  # Cat
print("domesticAnimals[0:2]", domesticAnimals[0:2])  # [Dog, Cat]
print("Hello, World![:7:2]", "Hello, World!"[:7:2])  # Output: "Hlo"
print("Dog" in domesticAnimals)  # True
print("Dog" not in wildAnimals)  # True
print(domesticAnimals * 2)  # ['Dog', 'Cat', 'Monkey', 'Dog', 'Cat', 'Monkey']
print(domesticAnimals + ["Cow"])  # ['Dog', 'Cat', 'Monkey', 'Cow']
print(domesticAnimals == wildAnimals)  # False
print(domesticAnimals != wildAnimals)  # True
# Lexicographic order
## 6 is less than 7. So, the second element comparison indicates that the second element is greater.
# The rest of the elements are not compared because the comparison has already determined the result based on the second elements.
print("[5, 6, 9] < [ 5, 7] =", [5, 6, 9] < [5, 7])  # true
print("[ 5, 7] > [5, 6, 9] =", [5, 7] > [5, 6, 9])  # true
print("[5, 6, 9] <= [ 5, 7] =", [5, 6, 9] < [5, 7])  # true
print("[ 5, 7] >= [5, 7, 9] =", [5, 7] > [5, 6, 9])  # true

# Equality Operator:

referenceDomesticAnimals = domesticAnimals

print(
    "referenceDomesticAnimals == domesticAnimals =",
    referenceDomesticAnimals == domesticAnimals,
)  # True, Comparison element by elements

print(
    "referenceDomesticAnimals is domesticAnimals =",
    referenceDomesticAnimals is domesticAnimals,
)  # True, Comparison with reference

print(
    "referenceDomesticAnimals == ['Dog', 'Cat'] =",
    referenceDomesticAnimals == ["Dog", "Cat"],
)  # True

print(
    "referenceDomesticAnimals is  ['Dog', 'Cat'] =",
    referenceDomesticAnimals is ["Dog", "Cat"],
)  # False
