# from app import app
import urllib.request,json
from .models import Sources
from .models import Articles


# Source = Sources
# Article = Articles

#Getting api_key
# api_key = app.config ['SOURCE_API_KEY']

#Getting the news base url
# news_sources_url = app.config["NEWS_SOURCES_API_BASE_URL"]
# article_url = app.config ["ARTICLE_API_BASE_URL"]

# Getting api key
api_key = None
# Getting the news base url
base_url = None
article_url = None

def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config["NEWS_SOURCES_API_BASE_URL"]
    article_url = app.config ["ARTICLE_API_BASE_URL"]

def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        source_results = None
        
        if get_sources_response['sources']:
            source_results_list = get_sources_response['sources']
            source_results = process_source_results(source_results_list)
            
    return source_results   

def process_source_results(source_list):
    '''
    function that processes the source result and transform them to a list of objects
    args:
    source_list: A list of dictionaries that contain source details
    Returns: source_results: A list of Source objects

    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        if id:
         source_object = Sources(id,name, author, title, description)
         source_results.append(source_object)
        
    return source_results    
        
def get_source(id):
    get_sources_details_url = base_url.format(id, api_key) 
    
    with urllib.request.urlopen(get_source_details_url)as url:
        source_details_data = url.read()
        source_details_response = json.loads(source_details_data)
        
        sources_object = None
        if source_details_response:
             name = source_details_response.get('name')  
             author= source_details_response.get('author')
             title = source_details_response.get('title')  
             description = source_details_response.get('description')
             
             sources_object = Sources(name,author,title, description)
        
    return source_object
  
def get_article(id):
    article_source_url = article_url.format(id,api_key)
    with urllib.request.urlopen(article_source_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)
        
        article_results = None
        if article_response ["articles"]:
            article_list = article_response['articles']
            article_results = article_details(article_list)
            
    return article_results

def article_details(news):
    article_results = []
    for article_details_response in news:
        name = article_details_response.get('name')  
        author= article_details_response.get('author')
        title = article_details_response.get('title')  
        description = article_details_response.get('description')
        image = article_details_response.get('urlToImage')
        url = article_details_response.get('url')
        date = article_details_response.get('publishedAt')
        content = article_details_response.get('content')
        
        if url:
            article_object = Articles(name, author, title, description, url, image, date, content)
            article_results.append(article_object)
    return article_results        
        
    
         
        
        









