from flask import Flask,render_template
from flask_wtf import Form
from wtforms import PasswordField,StringField
from wtforms.validators import input_required,Email,AnyOf,Length
from flask_bootstrap import Bootstrap

app=Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY']='DontTellAnyone'

class LoginForm(Form):
       username=StringField('username',validators=[input_required(),Email(message='i dont like your mail')])
       password=PasswordField('password',validators=[input_required(),Length(min=5,max=10),AnyOf(['secret','password'])])

@app.route('/',methods=['GET','POST'])
def index():
    form=LoginForm()
    if form.validate_on_submit():
        return 'Form succesfully submitted'
    return render_template('index.html',form=form)

if __name__=='__main__':
    app.run(debug=True)