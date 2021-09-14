class Articles:  
    ''' source class to define Source Objects
    '''
    def __init__(self,name, author, title, description, url, image, date, content):
        self.name = name
        self.author = author
        self.title = title
        self.url = url
        self.image = image
        self.description = description
        self.date = date
        self.content = content
        
        