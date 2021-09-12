from flask import render_template
from app import app
from .request import get_sources
#views
@app.route('/')
def index():
    ''' view root page function that returns the index page and its data'''
    
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    technology_sources = get_sources('technology')
    health_sources = get_sources('health')
    science_sources = get_sources('science')
    title = 'Welcome to News Centre'
    
    
    return render_template('index.html', title= title, general= general_sources,business= business_sources,technology =technology_sources,health=health_sources, science = science_sources )

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    view source page function that returns the source details page and its data
    '''
    
    return render_template('index.html', id = source_id)




