#Class object for Tweet

class Tweet:
    """def __init__(self, content, topic, category):
        self.content = content #The tweet itself
        self.topic = topic #Topic of tweet
        self.category = category #Category of tweet: statement, question, answer
    """
    def __init__(self, content):
        self.content = content
        self.topic = ""
        self.category = ""
