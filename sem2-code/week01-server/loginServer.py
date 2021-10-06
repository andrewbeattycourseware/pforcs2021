from flask import Flask, session, url_for,redirect, abort
app = Flask(__name__)
app.secret_key = 'someSecrtetasdrgsadfgsdfg3ko'
#eyJ1c2VybmFtZSI6IkkgZHVubm8ifQ.YV09VA.z7L9xazWvadqhxXSxzhdXddmen8
#eyJ1c2VybmFtZSI6IkkgZHVubm8ifQ.YV0-Rw.hXfFeej-Xkg-FdRnWyyRKRs9Z_c

@app.route('/')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    
    return 'welcome ' + session['username'] +\
        '<br><a href="'+url_for('logout')+'">logout</a>'

@app.route('/login')
def login():
    return '<h1> login</h1> '+\
        '<button>'+\
            '<a href="'+url_for('proccess_login')+'">' +\
                'login' +\
            '</a>' +\
        '</button>'

@app.route('/processlogin')
def proccess_login():
    #check credentials
    #if bad redirect to login page again

    #else
    print("logging in")
    session['username']="I dunno2"
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    print(session['username'])
    session.pop('username',None)
    if 'username' in session:
        print('o no')
        print(session['username'])
    else:
        print("nowt here")
    #session['username'] ='3434'
    #print(session['username'])

    #return 'done'
    return redirect(url_for('home'))


@app.route('/data/<int:id>')
def getData(id):
    if not 'username' in session:
        abort(401)

    print (session['username'])
    return '{"data":"all here"}'

if __name__ == '__main__' :
    app.run(debug= True)

