class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLE_API_BASE_URL='https://newsapi.org/v2/everything?q={}&apiKey={}'
    pass

class ProdConfig(Config):
    '''
    production configuration child class
    Args:
    Config:
    the parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    Args:
    Config : the parent configuration class with general configuration settings
    '''
    DEBUG = True
    
