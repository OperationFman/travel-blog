from flask import Flask, render_template, url_for

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template('home.html', page_title='Franklins Travel Blog')

@app.route('/Map')
def map():
    return render_template('map.html', page_title="Where I've Been")

@app.route('/Japan')
def japan():
    return render_template('japan.html', page_title='Frankly Japan')

@app.route('/NewZealand')
def newzealand():
    return render_template('newzealand.html', page_title='Frankly NZ')

@app.route('/Singapore')
def singapore():
    return render_template('singapore.html', page_title='Frankly Singapore')

@app.route('/Malaysia')
def malaysia():
    return render_template('malaysia.html', page_title='Frankly Malaysia')

@app.route('/Bali')
def bali():
    return render_template('bali.html', page_title='Frankly Bali')

@app.route('/Nepal')
def nepal():
    return render_template('nepal.html', page_title='Frankly Nepal')

@app.route('/China')
def china():
    return render_template('china.html', page_title='Frankly China')

if __name__ == '__main__':
    app.run(debug=True)
"""if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)"""
