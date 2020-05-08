from flask import Flask
from flask import url_for, redirect, render_template
app = Flask(__name__)


@app.route('/cool')
def home(): 
    return render_template('letter_counter_app.html')



if __name__ == '__main__': 
    app.run(debug=True)
