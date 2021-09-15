from flask import render_template, request
from . import main
from ..request import get_sources,get_source,article_details, get_article

#views
@main.route('/')
def index():
    ''' view root page function that returns the index page and its data'''

    general_sources = get_sources('general')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    title = 'Welcome to News Centre'
    
    
    return render_template('index.html', title= title, general= general_sources,business= business_sources,technology =technology_sources,health=health_sources, science=science_sources)

@main.route('/source/<int:id>')
def source(id):
    '''
    view source page function that returns the source details page and its data
    '''
    source = get_source(id)
    title= f'{source.title}'
    return render_template('source.html', title = title, source = source)




@main.route('/articles/<id>')
def article(id):
    
    article = get_article(id)
    title = f'{id}'
    
    return render_template('article.html', title = title, article = article)
