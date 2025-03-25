from openai import OpenAI


client = OpenAI(
        base_url="your api key",
        api_key="a3b011f40fde0a5331edecd0f7bd9874"
    )


system_prompt = """
You are a helpful assitant for providing accurate information about taxes in the US.
Give the information in the form of a converstation as opposed to a table.
I need this data to be readable for another LLM to look at.
No citations or descriptions.
If there are didfferent rates for different incocme levels, include that and make sure it is explicitly stated what the rate is at each level.
Don't fuck it up.
"""

input_prompt1 = """
Tell me the difference in taxes in los angeles and san franciscso.
Don't display it as a table. it needs to be in parapgraph form.
It should include all taxes relative to a nurse in the city.
Inclue all of the information, even the things which are the same.
No citations or descriptions please.
"""


input_prompt = """
Make a list of all of the taxes i would pay in San Jose, CA.
Include all taxes, not just thigns specific to the city. I need it for the state and federal taxes.
Display it in a table.
It should include all taxes relative to a nurse in the city.
Inclue all of the information, even the things which are the same in every state.
No citations or descriptions please.
"""

conversation = [{'role': "system", 'content': system_prompt}]
conversation.append({'role': 'user', 'content': input_prompt})




completion = client.chat.completions.create(
        model="diffbot-small-xl",
        temperature=0,
        messages=conversation
    )

print(completion.choices[0].message.content)
