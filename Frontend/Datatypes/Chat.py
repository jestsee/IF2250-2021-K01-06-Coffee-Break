from Message import Message 

class Chat : 
    def __init__(self, chatId, firstUserId, secondUserId) : 
        if(type(id) != int or type(firstUserId) != int or type(secondUserId) != int ) :
            raise ValueError("Invalid input for initiating object of type chat")
        # Values 
        self.__chatId = chatId
        self.__firstUserId = firstUserId
        self.__secondUserId = secondUserId

    def __init__(self, chatId, firstUserId, secondUserId, messages) : 
        if(type(chatId) != int or type(firstUserId) != int or type(secondUserId) != int) :
            raise ValueError("Invalid input for initiating object of type chat")
        # Values 
        if(type(messages) != list) : 
            if(len(messages) > 0 and type(messages[0]) != Message) : 
                raise ValueError("Invalid input for initiating object of type chat; messages parameter must be a list of object Messages")
        self.__chatId = chatId
        self.__firstUserId = firstUserId
        self.__secondUserId = secondUserId
        self.__messages = messages
    
    def printMessages(self) : 
        for message in self.__messages : 
            print(message);


# Testing 
message = Message(1, "Hey", "12 Nov 2020")
chat = Chat(12, 12, 12, [message])
chat.printMessages();


    