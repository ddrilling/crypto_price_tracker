from flask import Flask, render_template
from .. import price_tracker as pt

trendingList = []
trendingList = pt.getTrending()

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route('/home')
def index():
    return render_template('index.html', trendingList)

if __name__ == '__main__':
    app.run()