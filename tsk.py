from flask import Flask,render_template,request
import mysql.connector
app=Flask(__name__)
@app.route('/')
def film():
    return render_template('index.html')

@app.route('/result',methods=['POST','GET'])
def result():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="my_task" )
        mycursor = mydb.cursor()
        if request.method=='POST':
         result=request.form.to_dict()
        id = int(result['Id'])
        name = str(result['Name'])
        img = str(result['Img'])
        summary = str(result['Summary'])


        mycursor.execte("insert into my_task (id,name,img,summary)values(%i,%s,%s,%s)",(id,name,img,summary))
        mydb.commit()
        mycursor.close()
        return "Success"
app.run(debug=True)
