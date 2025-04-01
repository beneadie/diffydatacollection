import cities


def remove_non_alpha(input_string):
    """Removes all non-alphabetical characters from a string."""
    result = ""
    for char in input_string:
        if char.isalpha():
            result += char
    return result

output_dict_1={}

output_dict_2 = {}

for i in range(len(cities.list_cities)):
     key = remove_non_alpha(cities.list_cities[i])
     output_dict_1[key] = cities.list_cities[i]
     output_dict_2[cities.list_cities[i]] = key

print(output_dict_1)
print("\n\n\n\n\n\n////////////////////////////////////////////////////////////////////////////////////\n\n\n\n\n\n")
print(output_dict_2)
