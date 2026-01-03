"""
JSON (JavaScript Object Notation)

1. JSON is a DATA FORMAT, not a programming language.
2. Used to store and exchange data between systems.
3. Human-readable and machine-friendly.
4. Extremely common in APIs, configs, databases, AI pipelines.

Think of JSON as:
- Python dict + list
- With STRICT rules

--------------------------------
JSON vs Python (IMPORTANT)
--------------------------------
JSON            Python
----            ------
object          dict
array           list
string          str
number          int / float
true / false    True / False
null            None

--------------------------------
STRICT JSON RULES (MEMORIZE)
--------------------------------
1. Keys MUST be in double quotes
2. Strings MUST be in double quotes
3. No trailing commas
4. true / false / null are lowercase
5. Comments are NOT allowed in real JSON files

If I break these rules → JSON is INVALID.


Main operations:

> json.dump() → write Python data to JSON file
> json.load() → read JSON file into Python
> json.dumps() → Python → JSON string
> json.loads() → JSON string → Python
"""
#Example
import json

"""
This program demonstrates:
1. Creating Python data
2. Saving data to a JSON file
3. Reading data back from JSON
"""

def save_student_data(data, filename="students.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def load_student_data(filename="students.json"):
    with open(filename, "r") as file:
        return json.load(file)


# -------------------- Program Execution --------------------

student_data = {
    "name": "Alish",
    "roll_no": 12,
    "subjects": ["Physics", "Chemistry", "Math"],
    "marks": {
        "Physics": 78,
        "Chemistry": 69,
        "Math": 85
    },
    "passed": True
}

# Save data to JSON file
save_student_data(student_data)

# Load data from JSON file
loaded_data = load_student_data()

print("Data loaded from JSON:")
print(loaded_data)
print("Type after loading:", type(loaded_data))
