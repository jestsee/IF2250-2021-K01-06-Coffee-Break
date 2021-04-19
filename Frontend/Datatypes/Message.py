class Message : 
    def __init__(self, id, text, timestamp) : 
        if(type(id) != int or type(text) != str or type(timestamp) != str ) :
            raise ValueError("Invalid input for initiating object of type Message") 
        self.id = id
        self.text = text
        self.timestamp = timestamp
    def __str__(self): 
        return "id : " + str(self.id) + ", content : " + self.text + ", timestamp : " + self.timestamp

# # Testing 
# message = Message(1, "Hey", "There")
# print(type(message) == Message)