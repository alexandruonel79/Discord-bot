from neuralintents import GenericAssistant

def generateAnswer(input)->str:
    print(input)
    chatbot=GenericAssistant('intents.json', model_name="test_model")
    print("pana aici")
    chatbot.train_model()
    print("pana aici2")
    chatbot.save_model()
    print("pana aici3")
    return chatbot.request(input)
