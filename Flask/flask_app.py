from flask import Flask, render_template
#import price_tracker

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()