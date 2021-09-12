class Config:
    '''
    General configuration parent class
    '''
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
    
