# dict
# key value pairs
# ordered , changeable , does not allow duplicates
person_dict = {"name": "sam", "age": 32, "gender": "female"}
print(person_dict)
print(person_dict["name"])
print(person_dict.keys())
print(person_dict.get("age"))
person_dict.update({"insured": "yes"})
print(person_dict)
# nested dictionary example:
studentReport = {
    "Rohit": {
        "Math": 80,
        "Physics": 80,
        "Chemistry": 90
    },
    "Kavya": {
        "Math": 90,
        "Physics": 90,
        "Chemistry": 80
    },
    "Kiara": {
        "Math": 60,
        "Physics": 70,
        "Chemistry": 80
    }
}
print(studentReport["Rohit"]["Math"])