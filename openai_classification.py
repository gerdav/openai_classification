import openai

openai.api_key = "YOUR KEY"
models = openai.Model.list()


aimeta =     {
    "rules": {
        "processCategory": {
            "content":"""I have a code which has multiple functionalities. based on the text I will send you find the correct component it should use. Answer only the categeory in capital. Here are the rules:
 - any requests i made is for creating a python script, then use this component: PYTHCODE
 - any requests I made is for running a specific python script, then use this component: PYTHEXEC
 - if you see any python script included in the text, then include the script also from the second line like this: 
     PYTHONEXEC
     <script>
 - on any other type of request, use : OTHER"""}}}

def getCategory(c):
    try:
        # create a chat completion
        chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": aimeta["rules"]["processCategory"]["content"]}, {"role":"user", "content": c}])
        
        # print the chat completion
        # print(chat_completion.choices[0].message.content)
        content = chat_completion.choices[0].message.content
    except Exception as e:
        print(str(e))
    return content

mycontent = "Create a python script which adds 3 numbers."
res = getCategory(mycontent)
assert res == 'PYTHCODE'

mycontent = "I would like to run a script"
res = getCategory(mycontent)
assert res == 'PYTHEXEC'

mycontent = "I would like to run this script:\nprint('Hello AI!')"
res = getCategory(mycontent)
assert res ==  "PYTHONEXEC\nprint('Hello AI!')"