class Message : 
    def __init__(self, messageId, senderId, content, timestamp) : 
        if(type(messageId) != int or type(senderId) != int or type(content) != str or type(timestamp) != str ) :
            raise ValueError("Invalid input for initiating object of type Message") 
        self.__messageId = id
        self.content = content
        self.senderId = senderId
        self.timestamp = timestamp
    def __str__(self): 
        return "id : " + str(self.__messageId) + ", content : " + self.content + ", timestamp : " + self.timestamp

    def getId(self):
        return self.__messageId
    
    def setId(self, messageId):
        if(type(messageId) != int) : 
            raise ValueError("Invalid input for Message.setId")
        self.__messageId = messageId