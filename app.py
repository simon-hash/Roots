from flask import Flask, request, Response, render_template
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap

from database import db_init, db
from models import RootUsers


app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:peterlustig@localhost/rootsrock'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()