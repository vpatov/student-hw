# People Science (Who are they really?)

Let's analyze some data, crunch some numbers, and answer some questions about people. You can find a couple of datasets in `assignments/people_science`, that vary in size. You can practice with these datasets first (easier to inspect the data manually), but ultimately we want to answer questions about the largest dataset, which is too large to store in git, so you can download it [here](http://vas.nyc/large_data.json).

If the smallest datasets are too big to reason about or inspect when debugging, it could be helpful to work/prototype with your own small subset of the data, and save it in a file for easy use. You are encouraged to save/store any subset or intermediate representation of the data you want, whatever helps you work with it.

The datasets are stored in the [JSON format](https://www.json.org/json-en.html). You can load JSON data from a file into a python object like this:

```python
import json

with open('my_json_file.json', 'r') as f:
    data = json.load(f)
```

You can also load JSON data in from a string like this:
```python
import json

json_string = """
{"key1": "a", "key2": [1, 2, 3], "key3": {"a": 2}}
"""
data = json.loads(json_string)
print(data["key2"]) # [1, 2, 3]
```

The dataset consists of a list of people. People have some simple attributes like their name, weight, height, etc, as well as a universally unique identifier, `"uuid"`. They also have a list of things that they own, under the `"possessions"` key, as well as a list of friends, under `"friends"`.

Below you'll find a list of questions that we want to answer about the data. There a few datasets of various sizes with different people in them, so the answers to each question is different for each dataset (unless the answers happen to be the same by coincedence).

1. What is the average male height?
1. What is the median male height?
1. What is the median male height for males who have more than 20 friends?
1. Who is the densest male?
1. What is the standard deviation of female weight?
1. Who has the most money?
1. How many people have the first name John?
1. What is the positive difference between the average amount of money a man has vs the average amount a woman has? 
1. What is the name of the 201st fattest person (1st fattest being the most fat)?
1. Who has the largest amount of possessions (could be more than one answer) ?
6. Who owns the most expensive possession?
7. Who has the highest net worth (price of all possessions and their money)?
9. How many total cars do the women have?
15. What is the most popular possession?
16. What color is the heaviest hackysack?
17. What are the first names of the people that own only a chessboard?
18. How many people have tires but no car?
19. What are all the different types of possessions in this dataset? Format the answer in a lexicographically sorted list.
20. What is the sum of the weights of every person that owns either a guitar, a piano, marijuana, or cocaine?
21. Out of the people that have no possessions, who has the most friends (could be more than one answer)? 
22. What is the median price per pound of a boat?
23. What is the difference in weight of the most expensive purple object and the heaviest backpack that belongs to the poorest person that is taller than the average height?
25. What is the difference in price of the heaviest pizza and the cheapest teal condoms?
26. What is the average price of a car by color? i.e. average price of a red car, of a blue car, etc...
12. How many people have the most money in their friend group?
13. How many people are the tallest in their friend group?
14. What is the sum net worth of the people who have more kitty cats than anyone else in their friend group?













