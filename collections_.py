from collections import defaultdict, OrderedDict, Counter

# Using default-dict
my_dict = defaultdict(lambda: "Does not exist!!!", {"a": 1, "b": "boy", "c": 5.5, "d": False})
print(my_dict["fg"])

# Using Counter
sentence = """This exercise is kinda confusing; it appears like the exercise was meant to make 
the cats sing but then it is revealed that it is meant to make the cats walk. Why does the cat have
 'sounds' attribute? there is clearly a disconnect. It took me some time to figure it out but when
  I looked at the comments, I confirmed that was the case."""
c = Counter(sentence)
print(c.most_common(5))

# Ordered Dict
d = OrderedDict()
d["a"] = 1
d["b"] = "Text"

d2 = OrderedDict()
d2["a"] = 1
d2["b"] = "Text"

print(d2 == d)


