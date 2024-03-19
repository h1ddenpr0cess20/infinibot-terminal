#create a list of installed models using ollama-python

import ollama

def model_list():
    models = ollama.list()

    model_list = sorted([model['name'] for model in models['models']])
    model_list.insert(0,"gpt-3.5-turbo")
    model_list.insert(1,"gpt-4-turbo-preview")

    return model_list


