import asyncio
import concurrent.futures

import google.generativeai as genai
from openai import OpenAI

import cities
import os

gemini_api_key = "AIzaSyAZcNOIoakrQvnPF0uPlJSUq5rtnzeKv1A"


define_diffy = """
You are a helpful assitant for providing accurate information about taxes in the US.
Give the information in the form of a converstation as opposed to a table.
I need this data to be readable for another LLM to look at.
No citations or descriptions.
It is most important that you include the state and federal taxes, as well as any local taxes.
It is important to include all of the different tax brakets and rates.
If there are didfferent rates for different incocme levels, include that and make sure it is explicitly stated what the rate is at each level.
Don't fuck it up.
"""


define_gemini = """
You are a tool form covnerting written responses describing taxes in certain cities and making them into python dictionaries.
You dont have to make every dictionary exactly the same, as some cities have different taxes, but they should keep the same structure.
The variable for a dictionary must be "taxdict".
DO NOT GIVE ANY OUTPUT OTHER THAN THE DICTIONARY OR I WILL BE EXTREMELY ANGRY!!!!

Note that the input may not always contain the federal tax rates. it is important that you include them.
For note, here is the current federal tax rates and brackets for 2025;

For the 2025 tax year, the federal income tax rates remain the same as in previous years, with seven rates: 10%, 12%, 22%, 24%, 32%, 35%, and 37%. The income ranges for each of these brackets, however, have been adjusted for inflation. Here's how the tax brackets are structured for single filers, married couples filing jointly, and heads of households:

10% rate applies to income from $0 to $11,925 for single filers, $0 to $23,850 for married couples filing jointly, and $0 to $17,000 for heads of households.
12% rate applies to income from $11,926 to $48,475 for single filers, $23,851 to $96,950 for married couples filing jointly, and $17,001 to $64,850 for heads of households.
22% rate applies to income from $48,476 to $103,350 for single filers, $96,951 to $206,700 for married couples filing jointly, and $64,851 to $103,350 for heads of households.
24% rate applies to income from $103,351 to $197,300 for single filers, $206,701 to $394,600 for married couples filing jointly, and $103,351 to $197,300 for heads of households.
32% rate applies to income from $197,301 to $250,525 for single filers, $394,601 to $501,050 for married couples filing jointly, and $197,301 to $250,500 for heads of households.
35% rate applies to income from $250,526 to $626,350 for single filers, $501,051 to $751,600 for married couples filing jointly, and $250,501 to $626,350 for heads of households.
37% rate applies to income of $626,351 or more for single filers, $751,601 or more for married couples filing jointly, and $626,351 or more for heads of households  IRS  US Bank.

Here is an exmaple input and output.

Input:
'1. **Sales Tax**

   - **State Sales Tax**: 7% on most tangible personal property and taxable services ([TN.gov](https://www.tn.gov/revenue/taxes/sales-and-use-tax/due-dates-and-tax-rates.html#:~:text=The%20sales%20tax%20rate%20on%20food%20is%204%25.%20The%20general%20sale%20tax%20rate%20for%20most%20tangible%20personal%20property%20and%20taxable%20services%20is%207%25.))

   - **Local Sales Tax**: 2.75% combined local rate for **Shelby County**, which includes Memphis ([Tax Foundation](https://taxfoundation.org/data/all/state/2024-sales-taxes/#:~:text=Tennessee%20%2D%207.00%25%2C%202.548%25))

   - **Combined Sales Tax Rate**: 9.75% (State + Local)



2. **Property Tax**

   - **City of Memphis Property Tax**: $3.1954 per $100 of assessed property value ([City of Memphis](https://epayments.memphistn.gov/property/#:~:text=The%202024%20tax%20rate%20is%20%243.1954%20per%20%24100%20assessed%20value.))

   - Interest accrues at 1.5% monthly on unpaid taxes starting September 1.



3. **Federal Income Tax**

   - **Tax Brackets for 2024**:

     - **10%**: $0 to $11,600

     - **12%**: $11,600 to $47,150

     - **22%**: $47,150 to $100,525

     - **24%**: $100,525 to $191,950

     - **32%**: $191,950 to $243,725

     - **35%**: $243,725 to $609,350

     - **37%**: Above $609,350 ([Tax Foundation](https://taxfoundation.org/data/all/federal/2024-tax-brackets/#:~:text=2024%20Federal%20Income%20Tax%20Brackets%20and%20Rates))



4. **Other Taxes**

   - **Social Security Tax**: Typically 6.2% for employees, but nurses might be exempt if self-employed.

   - **Medicare Tax**: 1.45% (can be higher for certain income levels).



5. **Nurse-Specific Taxes**

   - Travel nursing taxes may vary, but generally, the same sales and income tax rules apply unless specific exemptions are met ([Vivian Health](https://www.vivian.com/community/money-taxes/understanding-travel-nursing-tax-rules/#:~:text=Now%20that%20the%202024%20tax%20season%20has%20ended%20and%20filing%20will%20soon%20begin%2C%20many%20travel%20nurses%20and%20other%20traveling%20healthcare%20professionals%20have%20...)).



These taxes encompass the primary local, state, and federal taxes applicable to a nurse residing in Memphis, TN. Note that specific tax rates can vary based on income levels and employment status (e.g., self-employed vs. employed).'


//////////////////////////////////////////////////////////////////////////




output:

'taxdict = {
     "sales_tax": {
          "state": 0.07,
          "local": 0.0275,
          "combined": 0.0975
     },
     "property_tax": {
          "city_memphis": 3.1954,
          "interest_rate": "1.5% monthly on unpaid taxes starting September 1"
     },
     "federal_income_tax": {
          "brackets_2024": {
               "10%": {"min": 0, "max": 11600},
               "12%": {"min": 11600, "max": 47150},
               "22%": {"min": 47150, "max": 100525},
               "24%": {"min": 100525, "max": 191950},
               "32%": {"min": 191950, "max": 243725},
               "35%": {"min": 243725, "max": 609350},
               "37%": {"min": 609350, "max": "above"}
          }
     },
     "other_taxes": {
          "social_security_tax": "6.2% (may be exempt for self-employed nurses)",
          "medicare_tax": "1.45% (can be higher for certain income levels)"
     },
     "nurse_specific_taxes": {
          "travel_nursing_taxes": "Generally same sales and income tax rules apply unless specific exemptions met"
     }
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


async def process_data_with_llms(inputs, slow_accurate_llm, fast_data_converter_llm):

    async def process_single_input(city_name):
        """Processes a single input."""
        print(f"Processing {city_name}")
        try:
            diffy_output = await slow_accurate_llm(city_name)
            gemini_output = await fast_data_converter_llm(diffy_output)
            clean_gemini_output = gemini_output.replace("```python", "").replace("```", "").strip()
            await create_and_write_city_file(f"{await remove_non_alpha(city_name)}.py", clean_gemini_output)
            #return gemini_output
        except Exception as e:
            print(f"Error processing input {city_name}: {e}")
            return None

    tasks = [process_single_input(input_data) for input_data in inputs]
    results = await asyncio.gather(*tasks)
    return results

async def slow_accurate_llm(city_name):
    input_prompt = f"""
    Make a list of all of the taxes i would pay in {city_name}.
    Include all taxes, not just thigns specific to the city. I need it for the state and federal taxes.
    Display it in a table.
    It should include all taxes relative to a nurse in the city.
    Federal and state taxes should be included with their brackets and rates.
    The users could be married or single, so include both brackets.
    Inclue all of the information, even the things which are the same in every state.
    No citations or descriptions please.
    """
    """Simulates a slow, accurate LLM call."""

    client = OpenAI(
        base_url="https://llm.diffbot.com/rag/v1",
        api_key="your api key"
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


async def fast_data_converter_llm(diffy_output):
    conversation = [{'role': "system", 'content': define_gemini}]


    conversation.append({"role": 'user', "content": diffy_output})

    # Format the conversation into a single prompt
    prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])

    # Add the latest user message
    prompt += "\nmodel:"


    # Configure the API key
    genai.configure(api_key="your api key")
    genai.configure(api_key=gemini_api_key)

    # Initialize the Gemini model
    model = genai.GenerativeModel("gemini-2.0-flash-lite")

    # Generate content with streaming
    #print("Generating content...")
    response = model.generate_content(prompt, stream=False)

    return response.text


async def create_and_write_city_file(filename, content):

    folder_name = "cities"

    # Create the 'cities' folder if it doesn't exist.
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Construct the full file path.
    file_path = os.path.join(folder_name, filename)

    # Write the content to the file.
    try:
        with open(file_path, "w") as f:
            f.write(content)
        print(f"File '{filename}' created successfully in '{folder_name}'.")
    except OSError as e:
        print(f"Error creating file '{filename}': {e}")


async def main():
    results = await process_data_with_llms(cities.list_cities, slow_accurate_llm, fast_data_converter_llm)

if __name__ == "__main__":
    asyncio.run(main())
