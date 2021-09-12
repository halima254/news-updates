from app import app
import urllib.request,json
from app.models.sources import Sources

Source = Sources

#Getting api_key
api_key = app.config ['SOURCE_API_KEY']

#Getting the news base url
news_sources_url = app.config["NEWS_SOURCES_API_BASE_URL"]

def get_sources(category):
    '''
    function that gets the json response to our url request
    '''
    get_sources_url = news_sources_url.format(category, api_key)
    
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
        name = source_item.get('name')
        author = source_item.get('author')
        title = source_item.get('title')
        description = source_item.get('description')
        
        source_object = Source(name, author, title, description)
        source_results.append(source_object)
        
    return source_results    
        
        
        
    
  
    
         
        
        









