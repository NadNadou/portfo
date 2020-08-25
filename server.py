from flask import Flask, render_template,request,redirect #render_template : allows to send html file
import csv

app = Flask(__name__) #correspond à la classe Flask, permet d'instancier notre app

@app.route('/') # decorator : takes a function, adds some functionality and returns it.
def my_home():
    return render_template('index.html')

#comprendre comment ça se fait que cette fonction soit 100 % dynamique
@app.route('/<string:page_name>') # decorator : takes a function, adds some functionality and returns it.
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:   #mode 'a' car on ajoutera des données aux données déjà existantes
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        file=database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:   #mode 'a' car on ajoutera des données aux données déjà existantes
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

#gestion du formulaire, on appelera jamais cette route dans le front
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #request.method = importation de flask
    if request.method == 'POST':
        try:
            #l'ensemble des données seront sous forme de dictionnaire
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'
