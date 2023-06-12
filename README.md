# OpenAI Power Demo

This short script demonstrates the power of OpenAI's language model in categorizing requests based on provided text. It utilizes the OpenAI Python library and the GPT-3.5-turbo model.

## Prerequisites

Before running the script, make sure you have the OpenAI Python library installed. You can install it using the following command:

```shell
pip install openai
```

Additionally, you need to have an API key from OpenAI. If you don't have one, sign up on the OpenAI website to obtain your API key.

## Setup


1. Clone this repository and navigate to the project directory.

```shell
git clone git@github.com:gerdav/openai_classification.git
cd openai_classification
```

2. Open the script file (openai_classificatino.py) in a text editor.
3. Replace "YOUR KEY" with your actual OpenAI API key. This will enable communication with the OpenAI API.
If you have not got key, please visit this page to get one: https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key

## Usage

The script provides a getCategory function that categorizes requests based on the provided text. The categories are defined according to the given rules.

To use the function, call it with a string parameter representing the request you want to categorize.

Example usage:

```python
mycontent = "Create a python script which adds 3 numbers."
res = getCategory(mycontent)
assert res == 'PYTHCODE'

mycontent = "I would like to run a script"
res = getCategory(mycontent)
assert res ==  'PYTHEXEC'

mycontent = "I would like to run this script:\nprint('Hello AI!')"
res = getCategory(mycontent)
assert res ==  "PYTHONEXEC\nprint('Hello AI!')"

```

The function will return the category of the request as a string.


## Output

The script sends the provided text to the OpenAI API, which utilizes the GPT-3.5-turbo model to generate a response.
The response contains the category determined by the model based on the given rules.

## License

This project is licensed under the MIT License.
