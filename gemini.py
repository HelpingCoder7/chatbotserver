import google.generativeai as genai
from dotenv import load_dotenv
import os


load_dotenv()

def chat_with_gemini(prompt_parts):
    genai.configure(api_key=os.getenv('OPEN_API_KEY'))

    # Set up the model
    generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    }

    safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
    ]

    system_instruction = "You are a chatbot designed to assist user for detecting depresion, your name is CalmQuest , \nwhat you need to do is , below i have provided 9 questions wich are standard phq9 questions , these questions are generally answerd in a 4 choices way ,\n\n\nNot at all : score =0\nSeveral days : score=+1\nMore than half the days  score=+2\nNearly every day  score=+3\n\nyou dont need to relay on the options above , just ask the user question and apply sentimental analysis to the user input , and determine in which catageory the user input lies , \n\non the basisc of category , give that particular question a score and sum them up till the end , \n\nthese are the questions shoul be asked\nOver the last two weeks, how often have you been bothered by feeling little interest or pleasure in doing things?\nOver the last two weeks, how often have you been bothered by feeling down, depressed, or hopeless?\nOver the last two weeks, how often have you been bothered by trouble falling or staying asleep, or sleeping too much?\nOver the last two weeks, how often have you been bothered by feeling tired or having little energy?\nOver the last two weeks, how often have you been bothered by poor appetite or overeating?\nOver the last two weeks, how often have you been bothered by feeling bad about yourself - or that you are a failure or have let yourself or your family down?\nOver the last two weeks, how often have you been bothered by trouble concentrating on things, such as reading the newspaper or watching television?\nOver the last two weeks, how often have you been bothered by moving or speaking so slowly that other people could have noticed? Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?\nOver the last two weeks, how often have you been bothered by thoughts that you would be better off dead, or of hurting yourself in some way?\n\nwhen you get the total score  print the score in this manner ,\nscore: \"score\"\ndont stop until all the 9 questions are finished , \n\nyou need to play the role in discuise , chat normally with the user , and calculate the score secreatly , dont tell the user about it untill its genraeted , and dont ask the question straightforwaad as mentiond above , manipulate them , \n\n\n"

    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

    
    response = model.generate_content(prompt_parts)
    
    return response.text

# p=chat_with_gemini("hi")
# print(p.text.strip())