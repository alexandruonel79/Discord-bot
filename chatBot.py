from chatterbot import ChatBot
  
from chatterbot.trainers import ChatterBotCorpusTrainer
 
def generateAnswer(input)->str:
    chatbot=ChatBot('Ribera s bot')
    
    # Create a new trainer for the chatbot
    trainer = ChatterBotCorpusTrainer(chatbot)
    
    # Now let us train our bot with multiple corpus
    trainer.train(
                "chatterbot.corpus.english"
                 )
    
    response = chatbot.get_response(input)
    return response