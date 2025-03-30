import google.generativeai as genai

import os
from dotenv import load_dotenv
load_dotenv()
gemini_api_key = os.getenv("GEMINI_KEY")

define_agent = """
You are a tool form covnerting written responses describing taxes in certain cities and making them into python dictionaries.
You dont have to make every dictionary exactly the same, as some cities have different taxes, but they should keep the same structure.
The variable for a dictionary must be "taxdict".
DO NOT GIVE ANY OUTPUT OTHER THAN THE DICTIONARY OR I WILL BE EXTREMELY ANGRY!!!!

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
real_data = """
#### Federal Taxes

- **Income Tax Brackets**: The federal income tax has seven tax rates in 2024: 10%, 12%, 22%, 24%, 32%, 35%, and 37%. The top marginal income tax rate of 37% applies to single filers with taxable income above $609,350 and married couples filing jointly above $731,200 ([Tax Foundation](https://taxfoundation.org/data/all/federal/2024-tax-brackets/#:~:text=2024%20Federal%20Income%20Tax%20Brackets%20and%20Rates)).

- **Social Security Tax**: 6.2% tax on the first $160,100 of earnings, with no tax on amounts above this threshold ([IRS](https://www.irs.gov/pub/irs-pdf/p15.pdf#search=Social%20Security%20Wage%20Limitation)).

- **Medicare Tax**: 1.45% tax on all earnings, with an additional 0.9% tax on earnings above $200,000 for single filers and $250,000 for joint filers ([IRS](https://www.irs.gov/individuals/what-is-employment-taxes)).

#### State Taxes (California)

- **Income Tax Rates**: California has nine state income tax rates ranging from 1% to 12.3%, depending on income and filing status ([NerdWallet](https://www.nerdwallet.com/article/taxes/california-state-tax#:~:text=California%20has%20nine%20state%20income%20tax%20rates)).

#### Local Taxes (San Jose, CA)

- **Sales Tax**: The combined sales tax rate for San Jose, CA, is 9.375% ([CDTFA](https://www.cdtfa.ca.gov/taxes-and-fees/rates.aspx#:~:text=San%20Jose%209.375%25)).

- **Business Tax**: San Jose imposes a business license tax based on gross receipts, with rates varying by business type ([City of San Jose](https://www.sanjoseca.gov/your-government/departments-offices/finance/business-tax-registration/business-tax-rates)).

#### Other Taxes

- **Property Tax**: Varies by location; generally around 0.8% to 1.2% of assessed property value annually ([Avalara](https://www.avalara.com/taxrates/en/state-rates/california/cities/san-jose.html#:~:text=The%20minimum%20combined%202025%20sales%20tax%20rate%20for%20San%20Jose)).

These taxes collectively impact the overall tax liability for a nurse residing in San Jose, CA. The specific tax rates applied depend on individual circumstances such as income level, filing status, and business ownership.
"""

def clean_dictionary_output(text):
        text = text.replace("```python", "").replace("```", "").strip()
        return text

def gemini_format(real_data):
     conversation = [{'role': "system", 'content': define_agent}]

     #conversation.append({"role": 'system', "content": template})

     #real_data = "This is the real data;\n" + real_data


     conversation.append({"role": 'user', "content": real_data})

     # Format the conversation into a single prompt
     prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])

     # Add the latest user message
     prompt += "\nmodel:"


     # Configure the API key
     genai.configure(api_key="your api key")

     # Initialize the Gemini model
     model = genai.GenerativeModel("gemini-2.0-flash-lite")

     # Generate content with streaming
     #print("Generating content...")
     response = model.generate_content(prompt, stream=False)
     output = clean_dictionary_output(response.text)
     return output

#print(response.text)
#
#print(type(response.text))
print(gemini_format(real_data))
