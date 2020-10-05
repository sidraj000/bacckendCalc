from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:8529454669@localhost:5432/dummy"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class SavingModel(db.Model):
    __tablename__ = 'savings_data'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String())
    savings  = db.Column(db.Integer())
    salary   = db.Column(db.String())

    def __init__(self, userName, savings,salary):
        self.userName = userName
        self.savings = savings
        self.salary = salary

    def __repr__(self):
        return f"<user {self.userName}>"
  

@app.route('/savings', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def handle_cars():
     data = request.get_json()
    #dataName=data['userName']
     dataSavings=(data['How much percent of salary do you save?'])
    # dataSalary=data['What is your yearly income?']
    #dataSalary=request.args.get('What is your yearly income?')
    #  userSavings = SavingModel(userName="unknown", savings=dataSavings, salary=dataSalary)
    #  db.session.add(userSavings)
    #  db.session.commit()
    #  userSavings = SavingModel.query.filter_by(salary = dataSalary).all()
    #  s1 = [0]*10
    #  results = [
    #         {
    #             "userName": userSaving.userName,
    #             "savings": userSaving.savings,
    #             "salary": userSaving.salary
    #         } for userSaving in userSavings]
    #  percentile=0
    #  total=len(userSavings)
    #  smaller=0
    #  for userSaving in userSavings:
    #      if (userSaving.savings < dataSavings):
    #          smaller=smaller+1
    #  percentile=(smaller/total*100)
     return ({'dataSavings': 'sid'})
    

if __name__ == '__main__':
    app.run(debug=True)