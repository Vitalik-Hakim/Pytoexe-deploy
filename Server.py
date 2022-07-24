# importing the required libraries
import os
from flask import Flask, render_template, request, send_file, flash,redirect
from scipy import rand
from werkzeug.utils import secure_filename
import datetime
#import hashids
import random




## Implementing Ticket naming system
#hashids = hashids.Hashids(salt="this is my exe and salt", )


# initialising the flask app
app = Flask(__name__)

app_data = {
    "name":         "Python to  EXE CONVERTER",
    "description":  "A web application to convert python .py files to .exe",
    "author":       "Vitalik Hakim",
    "html_title":   "Python to EXE CONVERTER",
    "project_name": "Python To Exe Converter",
    "keywords":     "PYTHON, .PY, exe, convert"
}


# Creating the upload folder
upload_folder1 = "uploads-server-1"
if not os.path.exists(upload_folder1):
   os.mkdir(upload_folder1)

upload_folder2 = "uploads-server-2"
if not os.path.exists(upload_folder2):
   os.mkdir(upload_folder2)

# Configuring the upload folder
app.config['UPLOAD_FOLDER1'] = upload_folder1
app.config['UPLOAD_FOLDER2'] = upload_folder2
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
# configuring the allowed extensions
allowed_extensions = ['py',]

def check_file_extension(filename):
    return filename.split('.')[-1] in allowed_extensions
def check_limit(filename):
    pass
# The path for uploading the file
@app.route('/')
def index():
   return render_template('index.html', app_data=app_data)

@app.route('/upload-page')
def uploadpage():
   return render_template('upload.html')
indexed = 1
@app.route('/upload', methods = ['GET', 'POST'])
def uploadfile():
   addr = request.environ['REMOTE_ADDR']
        # Counting hits
   with open('indexed.txt', 'r') as s:
        hit_list = s.readlines()
   hits = len(hit_list)
   if request.method == 'POST': # check if the method is post
      files = request.files.getlist('files') # get the file from the files object
      print(files)
      time = 0
      basename = "my_exe_ticket"
      randInt = str(random.randint(0,5000))
      #rands = hashids.encode(randInt)
      suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
      filenamed = "_".join([basename,randInt,suffix]) # e.g. 'my_exe_ticket_XDJSs3N_120508_171442'
      
      for f in files:
        #  f.filename.replace(" ","")
        #  if f== '':
        #     print("Please Upload A file")
        #     redirect('/')

         
        #  print(f.filename)
         clickbait = f.filename
         clickbait = clickbait.replace(".py",".exe")
         print(filenamed)
         # Saving the file in the required destination
         if check_file_extension(f.filename):
            if hits % 2 == 0: 
                f.save(os.path.join(app.config['UPLOAD_FOLDER1'] ,secure_filename(filenamed+".py"))) # this will secure the file
                res = os.listdir('uploads-server-1')
                print(res)
                position = res.index(filenamed+'.py')
                        # Counting hits
                with open('indexed.txt', 'a') as f:
                    f.write((filenamed) + " IP:"+ addr + '\n')
                with open('indexed.txt', 'r') as f:
                    hit_list = f.readlines()
                hits = len(hit_list)
                # each File takes about one minute to process so
                time = 60*position+1 # for 0 indexing of lists/ possible for first person
                if time == 1:
                    time = 60
            else:
                f.save(os.path.join(app.config['UPLOAD_FOLDER2'] ,secure_filename(filenamed+".py"))) # this will secure the file
                res = os.listdir('uploads-server-2')
                print(res)
                position = res.index(filenamed+'.py')
                        # Counting hits
                with open('indexed.txt', 'a') as f:
                    f.write((filenamed) + " IP:"+ addr + '\n')
                with open('indexed.txt', 'r') as f:
                    hit_list = f.readlines()
                hits = len(hit_list)
                # each File takes about one minute to process so
                time = 60*position+1 # for 0 indexing of lists/ possible for first person
                if time == 1:
                    time = 60
            

      if time == 0:
            filenamed = "Invalid Ticket Name: (Upload A the required file)"
      return render_template('modal.html',app_data=app_data,filenamed=filenamed,time=time, hits=hits, clickbait=clickbait)
   else:
        return render_template('404.html'), 404


# Download


# @app.route('/download-page')
# def downloadPage():
#    return render_template('download.html')

# Sending the file to the user
# @app.route('/download')
# def download():

#    return send_file('server-web.py', as_attachment=True)

@app.route('/ticket', methods =["GET", "POST"])
def ticket():
    if request.method == "POST":
       # getting input with ticket in HTML form
       ticket_id = request.form.get("download-ticket")
       res = os.listdir('downloads')
       print(res)
       if ticket_id+".exe" in res:

            return send_file('downloads/{}.exe'.format(ticket_id), as_attachment=True)
            
            
       else:
        pass
    return render_template('ticket.html',app_data=app_data)
@app.route('/service')
def service():
    return render_template('service.html', app_data=app_data)


@app.route('/contact')
def contact():
    return render_template('contact.html', app_data=app_data)

@app.route('/about')
def about():
    return render_template('about.html', app_data=app_data)

@app.route('/modal')
def modal():
    return render_template('modal.html', app_data=app_data)


# ERROR ROUTES
@app.errorhandler(404)
def not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(413)
def too_large(e):
   return render_template('413.html'), 413

@app.errorhandler(500)
def too_large(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.secret_key = 'xxxxxxxx'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run() # running the flask app
