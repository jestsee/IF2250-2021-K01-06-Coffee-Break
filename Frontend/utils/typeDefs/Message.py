class Message : 
    def __init__(self, id, content, timestamp) : 
        if(type(id) != int or type(content) != str or type(timestamp) != str ) :
            raise ValueError("Invalid input for initiating object of type Message") 
        self.__messageId = id
        self.content = content
        self.timestamp = timestamp
    def __str__(self): 
        return "id : " + str(self.__messageId) + ", content : " + self.content + ", timestamp : " + self.timestamp

# # Testing 
# message = Message(1, "Hey", "There")
# print(type(message) == Message)