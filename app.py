from flask import Flask
app = Flask(__name__)
app.config['SECRET KEY'] = 'zfgb6554vddfgsrg54351f'

# ----------------------- routes
# main page
@app.route('/')
def intro():
    return render_template('intro.html')

# history page
@app.route('/history')
def history():
    return render_template('history.html')


    
if __name__ == '__main__':
    app.run(debug=True)

