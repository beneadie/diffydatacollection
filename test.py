import tax_dicts

import codes


def get_city_info(city_name):
     if city_name and hasattr(tax_dicts, city_name):
          return getattr(tax_dicts, city_name)
     else:
          return "City not found."

for key in codes.norm_to_code:
    code = codes.norm_to_code[key]
    city_info = get_city_info(code)
    print(f"City: {key}, Info: {city_info}")
    break
