import asyncio
import concurrent.futures

import google.generativeai as genai
from openai import OpenAI

import cities
import os
import json

from dotenv import load_dotenv
load_dotenv()
diffy_key = os.getenv("DIFFY_KEY")
gemini_api_key = os.getenv("GEMINI_KEY")


define_diffy = """
You are a helpful assitant for providing accurate information about cost of living in US cities.
Give the information in the form of a converstation as opposed to a table.
I need this data to be readable for another LLM to look at.
No citations or descriptions.
It is most important that you include each of the things asked for.
Don't fuck it up.
"""


define_gemini = """
You are a tool form converting written responses describing the cost of in certain cities and making them into python dictionaries.
Try to be consistent keep the same structure when you can, although there may be situations where the example structure won't capture all of the information.
If you are not given the required information, put that field value as "n/a"
The variable for a dictionary must be the the name of the city with nospaces or special characters, followed by the state abbreviation in capitals. eg OaklandCA, NewYorkNY, WashingtonDC, MiamiFL, ElPasoTX.
The name of the dictionary will be given to you.DO NOT GIVE ANY OUTPUT OTHER THAN THE DICTIONARY OR I WILL BE EXTREMELY ANGRY!!!!


input;

The cost of living in **New York, NY** is notably high compared to other parts of the country. Here's a detailed breakdown of various expenses you might incur:

#### Average Income
- The average salary for full-time workers in New York is $98,196, with a median salary of $68,891 ([Income by Zip Code](https://www.incomebyzipcode.com/newyork#:~:text=The%20average%20salary%20for%20full%2Dtime%20workers%20in%20New%20York%20is%20%2498%2C196)).

#### Housing Costs
- The average rent for an apartment in New York is $3,922 per month ([Apartments.com](https://www.apartments.com/rent-market-trends/new-york-ny#:~:text=the%20average%20rent%20in%20New%20York%2C%20NY%20is%20%243%2C922%20per%20month)).
- Specific rental rates by apartment size are as follows:
  - Studio: $3,171/month
  - One Bedroom: $3,922/month
  - Two Bedroom: $5,303/month
  - Three Bedroom: $6,596/month ([Apartments.com](https://www.apartments.com/rent-market-trends/new-york-ny#:~:text=Studio%20%243%2C171%2Fmonth%2C%20One%20Bedroom%20%243%2C922%2Fmonth%2C%20Two%20Bedroom%20%245%2C303%2Fmonth%2C%20Three%20Bedroom%20%246%2C596%2Fmonth)).

#### Food Costs
- Eggs (dozen): Approximately $2.50 - $3.50
- Steak (1 lb ribeye): Approximately $15.00 - $20.00
- Milk (1 gal): Approximately $3.50 - $4.50
- Beer (6-pack): Approximately $10.00 - $15.00

#### Gym Membership
- A gym membership in New York can cost around $12/month for a pass to every community pool and gym ([Reddit](https://www.reddit.com/r/AskNYC/comments/11wyq6h/how_much_are_you_paying_monthly_for_a_gym/)).

#### Public Transportation
- Subway and bus fares are $2.90 for most riders ([MTA](https://www.mta.info/fares-tolls#:~:text=Subway%20and%20bus%20fares.%20The%20fare%20is%20%242.90%20for%20most%20riders)).

#### Gasoline
- The average price of gasoline in New York City is around $3.42 per gallon as of 2024 ([EIA](https://www.eia.gov/dnav/pet/hist/LeafHandler.ashx?n=PET&s=EMM_EPMR_PTE_Y35NY_DPG&f=M#:~:text=3.234%2C%203.423%2C%203.563%2C%203.420%2C%203.439%2C%203.329%2C%203.117%2C%202.979%2C%202.923)).

#### Average Meal Price at a Restaurant
- The average price for takeaway food is around $13 for a basic cheeseburger and fries from Shake Shack ([Reddit](https://www.reddit.com/r/AskNYC/comments/1fbtuni/current_average_price_for_takeaway_food_in_ny/)).

These figures provide a comprehensive view of the expenses associated with living in New York City, helping you plan your budget accordingly.

Name dictionary variable 'MemphisTN'

//////////////////////////////////////////////////////////////////////////


output;

'MemphisTN = {
    "average_income": {
        "average_salary": 98196,
        "median_salary": 68891
    },
    "housing_costs": {
        "average_rent": 3922,
        "rent_by_size": {
            "studio": 3171,
            "one_bedroom": 3922,
            "two_bedroom": 5303,
            "three_bedroom": 6596
        }
    },
    "food_costs": {
        "eggs_dozen": {"min": 2.50, "max": 3.50},
        "steak_1lb_ribeye": {"min": 15.00, "max": 20.00},
        "milk_1gal": {"min": 3.50, "max": 4.50},
        "beer_6pack": {"min": 10.00, "max": 15.00}
    },
    "gym_membership": 12.00,
    "public_transportation": 2.90,
    "gasoline_per_gallon": 3.42,
    "average_meal_price": 13.00
}'

////////////////////////////////////////////////////////////////////////////
"""
async def remove_non_alpha(input_string):
    """Removes all non-alphabetical characters from a string."""
    result = ""
    for char in input_string:
        if char.isalpha():
            result += char
    return result

#async def process_data_with_llms(inputs, slow_accurate_llm, fast_data_converter_llm, batch_size=4):
#    """Processes inputs in batches."""
#    for i in range(0, len(inputs), batch_size):
#        batch = inputs[i:i + batch_size]
#        tasks = [process_single_input(city, slow_accurate_llm, fast_data_converter_llm) for city in batch]
#        await asyncio.gather(*tasks)

#async def process_data_with_llms(inputs, slow_accurate_llm, fast_data_converter_llm, concurrent_tasks=4):
#    """Processes inputs concurrently with a specified number of tasks."""
#    semaphore = asyncio.Semaphore(concurrent_tasks)
#    async def process_with_semaphore(input_data):
#        async with semaphore:
#            await process_single_input(input_data)
#    tasks = [process_with_semaphore(input_data) for input_data in inputs]
#    await asyncio.gather(*tasks)

async def process_data_with_llms(inputs, slow_accurate_llm, fast_data_converter_llm):
    """Processes inputs concurrently using asyncio.gather."""
    tasks = [process_single_input(input_data) for input_data in inputs]
    await asyncio.gather(*tasks)

async def process_single_input(city_name):
    print(f"Processing {city_name}")
    city_code = await remove_non_alpha(city_name)
    try:
        diffy_output = await slow_accurate_llm(city_name)
        gemini_output = await fast_data_converter_llm(diffy_output, city_code)
        clean_gemini_output = gemini_output.replace("```python", "").replace("```", "").strip()
        await append_string_dictionary_to_file(clean_gemini_output)
    except Exception as e:
        print(f"Error processing input {city_name}: {e}")
        return None

#async def process_single_input(city_name):
#    """Processes a single input."""
#    print(f"Processing {city_name}")
#    city_code = await remove_non_alpha(city_name)
#    try:
#        diffy_output = await slow_accurate_llm(city_name)
#        gemini_output = await fast_data_converter_llm(diffy_output, city_code)
#        clean_gemini_output = gemini_output.replace("```python", "").replace("```", "").strip()
#        await append_string_dictionary_to_file(clean_gemini_output)
#        #return gemini_output
#    except Exception as e:
#        print(f"Error processing input {city_name}: {e}")
#        return None
#
#    tasks = [process_single_input(input_data) for input_data in inputs]
#    results = await asyncio.gather(*tasks)
#    return results

async def slow_accurate_llm(city_name):
    print(f"slow running {city_name}")
    input_prompt = f"""
    give me a detailed description of the cost of living in {city_name}.
    it should include average income, average rent for an apartment, average rent for a house, cost of common foods (include eggs, steak, milk, beer), cost of gym membership, cost of public transport, cost of gasoline.
    try make it detialed, include the cost of the average meal at a restaurant separate to the foods list.
    give the repsonse in natural language."""


    client = OpenAI(
        base_url="https://llm.diffbot.com/rag/v1",
        api_key=diffy_key #"your api key for diffychat"
    )

    conversation = [{'role': "system", 'content': define_diffy}]
    conversation.append({'role': 'user', 'content': input_prompt})
    completion = client.chat.completions.create(
            model="diffbot-small-xl",
            temperature=0,
            messages=conversation
        )
    response = completion.choices[0].message.content
    print(response)
    return response


async def fast_data_converter_llm(diffy_output, city_code):

    diffy_output += f"\n\nName dictionary variable {city_code}"
    conversation = [{'role': "system", 'content': define_gemini}]
    conversation.append({"role": 'user', "content": diffy_output})
    # Format the conversation into a single prompt
    prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])
    # Add the latest user message
    prompt += "\nmodel:"
    # Configure the API key
    #genai.configure(api_key="your api key")
    genai.configure(api_key=gemini_api_key)
    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-2.0-flash-lite")
    # Generate content with streaming
    #print("Generating content...")
    response = model.generate_content(prompt, stream=False)

    return response.text


#async def create_and_write_city_file(filename, content):
#
#    folder_name = "cities"
#
#    # Create the 'cities' folder if it doesn't exist.
#    if not os.path.exists(folder_name):
#        os.makedirs(folder_name)
#
#    # Construct the full file path.
#    file_path = os.path.join(folder_name, filename)
#
#    # Write the content to the file.
#    try:
#        with open(file_path, "w") as f:
#            f.write(content)
#        print(f"File '{filename}' created successfully in '{folder_name}'.")
#    except OSError as e:
#        print(f"Error creating file '{filename}': {e}")


async def append_string_dictionary_to_file(dictionary_string):
    """
    Appends a dictionary (in string form) to a .txt file, each dictionary on a new line.
    """

    filename = "col_dicts.txt"  # Changed to .txt
    folder_name = "cities_data"

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, filename)

    try:
        # Format the dictionary as a string for writing to the .txt file.
        dictionary_str = dictionary_string + "\n\n"  # Add newline for each dictionary

        with open(file_path, "a") as f: #append mode
            f.write(dictionary_str)

        print(f"Dictionary appended to '{filename}' successfully in '{folder_name}'.")

    except OSError as os_error:
        print(f"Error appending to file '{filename}': {os_error}")
    except TypeError as type_error:
        print(f"Error, invalid dictionary string: {type_error}")

async def main():
    results = await process_data_with_llms(cities.cities_col, slow_accurate_llm, fast_data_converter_llm)

def finalize_txt_to_py(folder_name="cities_data", txt_filename="col_dicts.txt", py_filename="col_dicts.py"):
    """
    Converts the .txt file to a .py file by adding brackets and renaming.
    """
    txt_path = os.path.join(folder_name, txt_filename)
    py_path = os.path.join(folder_name, py_filename)

    try:
        with open(txt_path, "r+") as f:
            content = f.read()
            #Remove the last comma and newline if the file is not empty.
            if len(content) > 0:
              content = content[:-2]
            content += "\n]" #add the closing bracket for a list.
            f.seek(0)
            f.write(content)
            f.truncate()

        os.rename(txt_path, py_path)
        print(f"File '{txt_filename}' renamed to '{py_filename}'.")

    except OSError as e:
        print(f"Error finalizing file: {e}")

if __name__ == "__main__":
    asyncio.run(main())
    finalize_txt_to_py()


