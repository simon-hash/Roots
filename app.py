from flask import Flask, request, Response, render_template
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap

from database import db_init, db
from models import RootUsers


app = Flask(__name__)
Bootstrap(app)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:peterlustig@localhost/rootsrock'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kjlgqrfqnbicyn:c26d248de8e9f7ecb1556827592c49922c8c47631804f8a0ad1ccea8881ebb12@ec2-52-201-124-168.compute-1.amazonaws.com:5432/d3qhna99gf3vpe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()