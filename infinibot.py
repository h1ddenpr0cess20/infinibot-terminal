import openai
import os
from rich.console import Console

class infiniGPT:
    def __init__(self, personality):
        # holds history
        self.messages = []

        # set default personality
        self.personality = personality
        self.persona(self.personality)
        
    #Sets personality
    def persona(self, persona):
        self.messages.clear()
        personality = "assume the personality of " + persona + ".  roleplay and always stay in character unless instructed otherwise.  keep your first response short."
        self.messages.append({"role": "system", "content": personality})

    # respond to messages
    def respond(self, message):
        try:
            #Generate response with gpt-3.5-turbo model
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message)
        except Exception as e:
            return e
        else:
            #Extract response text and add it to history
            response_text = response['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": response_text})
            if len(self.messages) > 14:
                del self.messages[1:3]
            return response_text.strip()
        
    def start(self):
        #clear screen
        def reset():
            os.system('clear') #clear 
            
            greet = "introduce yourself"
            personality = "assume the personality of " + self.personality + ".  roleplay and always stay in character unless instructed otherwise.  keep your first response short."
            try:
                response = openai.ChatCompletion.create(model='gpt-3.5-turbo', messages=[{"role": "system", "content": personality},
                                                                                            {"role": "user", "content": greet}])
                response_text = response['choices'][0]['message']['content']
                console.print(response_text + "  Type help for more information.\n", style='gold3')
            except:
                console.print("Hello, I am InfiniGPT, an AI that can assume any personality.  Type help for more information.\n", style='gold3')

        # text wrap and color
        console = Console()
        console.width=100
        console.wrap_text = True
        soft_wrap=True
        
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
[b]quit[/] or [b]exit[/] exits the program.
''', style="gold3")
                
            # set personality    
            elif prompt == "persona":
                persona = console.input("[grey66]Persona: [/]") #ask for new persona
                self.persona(persona) #response passed to persona function
                console.print(self.respond(self.messages) + "\n", style="gold3", justify="full") #print response

            # reset history   
            elif prompt == "reset":
                reset()
                
            # stock gpt    
            elif prompt == "default" or prompt == "stock":
                self.messages.clear()
                console.print("Stock GPT settings applied\n", style="red")

            # normal response
            elif prompt != None:
                self.messages.append({"role": "user", "content": prompt})
                console.print(self.respond(self.messages) + "\n", style="gold3", justify="full") #print response
            
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
