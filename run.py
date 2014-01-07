import flask, os

app = flask.Flask(__name__)


@app.route('/')
@app.route('/<page>')
def main(page="index"):
    page += '.html'
    if os.path.isfile('templates/' + page):
        return flask.render_template(page)
    return flask.abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return flask.render_template('404.html'), 404


@app.after_request
def add_header(response):
    """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

# Debug should normally be false, so we don't display hazardous information!
app.debug = False # Set it to true, to show awesome debugging information!
app.run(host='0.0.0.0', port=5000)
