from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:8529454669@localhost:5432/dummy"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
class SavingModel(db.Model):
    __tablename__ = 'savings_data'

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String())
    savings  = db.Column(db.Integer())
    salary   = db.Column(db.String())
    isPrimary= db.Column(db.Boolean())

    def __init__(self, userName, savings,salary,isPrimary):
        self.userName = userName
        self.savings = savings
        self.salary = salary
        self.isPrimary=isPrimary
    def __repr__(self):
        return f"<user: {self.userName} savings:{self.savings} salary:{self.salary} isPrimary:{self.isPrimary}>"
  
@app.route('/total',methods=['GET'])
def toal_users():
     userSavings = SavingModel.query.all()
     return {"totalUsers":len(userSavings)}

@app.route('/savings', methods=['POST'])
def handle_submission():
     data =  request.get_json(force=True)
     dataSavings=int(data['How much percent of salary do you save?'])
     dataSalary=data['What is your yearly income?']
     dataName=data['userName']

     currentUsersData=SavingModel.query.filter_by(userName = dataName).count()
     dataIsPrimary = False

     percentile=0
     total=1
     smaller=0 
     average=dataSavings

     if (currentUsersData==0):
      dataIsPrimary=True
      total=0
      average=0
     

     userSavings = SavingModel(userName=dataName, savings=dataSavings, salary=dataSalary,isPrimary=dataIsPrimary)
     db.session.add(userSavings)
     db.session.commit()

     userSavings = SavingModel.query.filter_by(salary = dataSalary,isPrimary=True).order_by('savings').all()


     for userSaving in userSavings:
         total+=1
         average+=userSaving.savings
         if (userSaving.savings < dataSavings):
          smaller=smaller+1         

     
     def round_to_two_digits(num):
       return float(int(num*100)/100)

     average=average/total
     percentile=(smaller/total*100)

     percentile=round_to_two_digits(percentile)
     average=round_to_two_digits(average)

     totUsers=len(userSavings)
     print(totUsers)
     totUsers=int(totUsers*9/10)
     totUsers-=1
     top10=userSavings[totUsers].savings
   

     return {"Percentile":percentile,"Average":average,"Top10":top10}
    

if __name__ == '__main__':
    app.run(debug=True)