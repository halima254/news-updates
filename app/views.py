from flask import render_template
from app import app
#views
@app.route('/')
def index():
    ''' view root page function that returns the index page and its data'''
    
    message = 'Welcome to News Centre'
    return render_template('index.html', message = message)

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    view source page function that returns the source details page and its data
    '''
    
    return render_template('source.html', id = source_id)

def index():
    '''
    view root page that returns the index page and its data
    '''
    
    title = 'Home - Welcome to News center'
    
    return render_template('index.html', title = title)
