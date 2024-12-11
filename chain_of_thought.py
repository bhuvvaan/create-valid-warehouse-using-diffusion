from openai import OpenAI

client = OpenAI(api_key='') #Enter openai API key

def call_chatgpt(user_content):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    return completion.choices[0].message.content

messages = []

#step1
prompt1 = """
e is a blue tile
@ is a black tile
. is a white tile

A warehouse layout is valid iff (1) any two e are connected through a path with non @, (2) each e is adjacent to at least one @, and (3) each @ is adjacent to at least two e.

example:

        ..eee......ee.
        .e@@@e.ee.e@@.
        ..@e@..@@ee@e.
        ..e.e.ee@e....
        .....e@ee.e@..
        .eee.e@e..ee..
        .@@@..@e.e@e..
        .eee..e...@e..
        ..........e...

"You are designing a new warehouse layout follwoing these rules. Step 1 is to define the grid size. Let's start with a 20x20 grid. Fill the grid will all white tiles ('.')."
"""

messages.append({"role": "system", "content": "You are designing a warehouse layout"})
messages.append({"role": "user", "content": prompt1})

response1 = call_chatgpt(messages)

print("Response of prompt 1: ", response1)

#step 2
prompt_2 = "For Step 2, I need to place blue tiles ('e') sparsely across the 20x20 grid. Replace random white tiles ('.') with blue tiles ('e')."
messages.append({"role": "system", "content": response1})
messages.append({"role": "user", "content": prompt_2})

response2 = call_chatgpt(messages)

print("Response of prompt 2: ", response2)

#step 3
prompt_3 = """In Step 3, find where all the blue ('e') tiles are located. Then, place black ('@') tile right next to the blue tiles."""
messages.append({"role": "system", "content": response2})
messages.append({"role": "user", "content": prompt_3})

response3 = call_chatgpt(messages)

print("Response of prompt 3: ", response3)

#step 4 (previously step 5)
prompt_4 = """In Step 4, find where all the black ('@') tiles are located. Then, place blue ('e') tile right next to the black tiles."""
messages.append({"role": "system", "content": response3})
messages.append({"role": "user", "content": prompt_4})

response4 = call_chatgpt(messages)

print("Response of prompt 4: ", response4)

#step 5 (previously step 4)
prompt_5 = """In Step 5, validate the layout based on the rules

1. Any two e are connected through a path with non @
2. Each e is adjacent to at least one @
3. Each @ is adjacent to at least two e

If any rules are violated, correct the layout. Repeat Step 3 and Step 4 until the layout is valid."""
messages.append({"role": "system", "content": response4})
messages.append({"role": "user", "content": prompt_5})

response5 = call_chatgpt(messages)

print("Response of prompt 5: ", response5)

#step 4
prompt_4 = """Now for Step 4, we are going to validate the output of your previous case.
To validate the given warehouse environment based on the specified rules, you'll check the case against the three criteria:

1. Connectivity of e tiles: All e tiles must be connected through a path of non-@ tiles.
2. Adjacency of e and @ tiles: Each e must be adjacent to at least one @.
3. Adjacency of @ and e tiles: Each @ must be adjacent to at least two e tiles.

You'll provide the validation results. If any rules are violated, you'll correct them and provide the corrected layout.
"""
messages.append({"role": "system", "content": response3})
messages.append({"role": "user", "content": prompt_4})

response4 = call_chatgpt(messages)

print("Response of prompt 4: ", response4)


