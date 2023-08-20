# infinigpt-terminal

Terminal version of InfiniGPT, the OpenAI chatbot capable of any personality.  Also available for [IRC](https://github.com/h1ddenpr0cess20/infinigpt-irc) and [Matrix](https://github.com/h1ddenpr0cess20/infinigpt-matrix) chat protocols.  Google PaLM version available at [infiniPaLM-terminal](https://github.com/h1ddenpr0cess20/infiniPaLM-terminal)

## Setup
```
pip3 install openai rich
```
Add your [OpenAI API](https://platform.openai.com/signup) key.  
Change the default personality to something else if you want.

## Use
```
python3 infinigpt.py
```


**help** shows the help menu

**reset**  resets to default personality

**stock** or **default**  sets bot to stock gpt settings

**persona**  activates personality changer, enter a new personality when prompted. This isn't where you would use one of those long custom prompts you find elsewhere.  If you want to do that, use **stock** then enter your custom prompt.

**quit** or **exit** exits the program
