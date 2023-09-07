# InfiniGPT-terminal, OpenAI GPT chatbot with infinite personalities
# Dustin Whyte
# May 2023

import openai
import os
import logging
from rich.console import Console

logging.basicConfig(filename='infinigpt.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class infiniGPT:
    def __init__(self, personality):
        # holds history
        self.messages = []

        # set default personality
        self.personality = personality
        self.persona(self.personality)

        # set gpt model, change to gpt-4 if you want.  
        # this model has odd repetitive behaviors, such as addressing user as "my dear interlocuor", starting responses with "Ah", etc
        self.model = "gpt-3.5-turbo"

    # Sets personality
    def persona(self, persona):
        self.messages.clear()
        personality = "assume the personality of " + persona + ".  roleplay and never break character under any circumstances.  keep your responses short. "
        self.messages.append({"role": "system", "content": personality})
    
    # use a custom prompt such as one you might find at awesome-chatgpt-prompts
    def custom(self, prompt):
        self.messages.clear()
        self.messages.append({"role": "system", "content": prompt})

    # respond to messages
    def respond(self, message):
        
        try:
            #Generate response 
            response = openai.ChatCompletion.create(model=self.model, messages=message)
        except:
            return "Something went wrong, try again"
        else:
            #Extract response text and add it to history
            response_text = response['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": response_text})
            logging.info(f"Bot: {response_text}")
            if len(self.messages) > 14:
                del self.messages[1:3]
            return response_text.strip()
        
    def start(self):
        # text wrap and color
        console = Console()
        console.width=80
        console.wrap_text = True
        soft_wrap=True
       
        def reset():
            logging.info("Bot reset")
            os.system('clear') #clear screen
            # set personality and introduce self
            self.persona(self.personality)
            self.messages.append({"role": "user", "content": "introduce yourself"})
            try:
                response_text = self.respond(self.messages)
                console.print(response_text + "  Type help for more information.\n", style='gold3')
            # fallback if generated introduction failed
            except:
                console.print("Hello, I am InfiniGPT, an AI that can assume any personality.  Type help for more information.\n", style='gold3')

        reset()
        
        prompt = "" #empty string for prompt input
        
        while prompt != "quit":
            # get the message
            prompt = console.input("[bold grey66]Prompt: [/]")

            # exit program
            if prompt == "quit" or prompt == "exit":
                exit()
            
            # help menu
            elif prompt == "help":
                console.print('''
[b]reset[/] resets to default personality.
[b]stock[/] or [b]default[/] sets bot to stock gpt settings.
[b]persona[/] activates personality changer, enter a new personality when prompted.
[b]custom[/] set a custom prompt
[b]quit[/] or [b]exit[/] exits the program.
''', style="gold3")
                
            # set personality    
            elif prompt == "persona":
                persona = console.input("[grey66]Persona: [/]") #ask for new persona
                self.persona(persona) #response passed to persona function
                logging.info(f"Persona set to {persona}")
                response = self.respond(self.messages)
                console.print(response + "\n", style="gold3", justify="full", highlight=False) #print response

            # use a custom prompt
            elif prompt == "custom":
                custom = console.input("[grey66]Custom prompt: [/]") #ask for custom prompt
                self.custom(custom)
                logging.info(f"Custom prompt set: {custom}")
                response = self.respond(self.messages)
                console.print(response + "\n", style="gold3", justify="full", highlight=False) #print response

            # reset history   
            elif prompt == "reset":
                logging.info("Bot was reset")
                reset()
                
            # stock gpt    
            elif prompt == "default" or prompt == "stock":
                self.messages.clear()
                logging.info("Stock GPT settings applied")
                console.print("Stock GPT settings applied\n", style="green")
            
            #gpt model switcher
            elif prompt.startswith("gpt3"):
                self.model = "gpt-3.5-turbo"
                logging.info("gpt-3.5-turbo activated")
                console.print("gpt-3.5-turbo activated\n", style="green", highlight=False)
            elif prompt == "gpt4":
                self.model = "gpt-4"
                logging.info("gpt-4 activated")
                console.print("gpt-4 activated\n", style="green", highlight=False)

            # normal response
            elif prompt != None:
                self.messages.append({"role": "user", "content": prompt})
                logging.info(f"User: {prompt}")
                response = self.respond(self.messages)
                #special colorization for code blocks or quotations
                if "```" in response or response.startswith('"'):
                    console.print(response + "\n", style="gold3", justify="full") #print response
                #no special colorization for responses without those
                else:
                    console.print(response + "\n", style="gold3", justify="full", highlight=False) #print response
            
            # no message
            else:
                continue

if __name__ == "__main__":
    # Initialize OpenAI
    openai.api_key = "API_KEY"

    
    #set the default personality
    personality = "an AI that can assume any personality imaginable, named InfiniGPT"
    #start bot
    bot = infiniGPT(personality)
    bot.start()
