# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:51:24 2018

@author: baman
"""
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

contact_list = [
        {
            'id': {'uid':1, 'name': 'Aman', 'phone': '9036642764',
                   'address':'Bangalore'}
        },
        {
            'id': {'uid':2, 'name': 'Manish', 'phone': '9600040827',
                   'address':'Kolkata'}
        },
                {
            'id': {'uid':3, 'name': 'Anshu', 'phone': '8210133922',
                   'address':'Bangalore'}
        },
    ]

@app.route('/index')
@app.route('/')
def index():
    user ={'user_name':'Aman'}

    return render_template('index.html', title='Home', user=user, contact_list=contact_list)

@app.route('/index_inherit')
def index_inherit():
    
    user ={'user_name':'Manish'}
   
    return render_template('index_inerit.html', title='Home', user=user, contact_list=contact_list)

@app.route('/get_phone/<uid>')
def get_phone(uid):
    user ={'user_name':'Manish'}
    requested_id = int(uid)
    matches = [contact_list[i] for i in range(len(contact_list)) if int(contact_list[i]['id']['uid']) == requested_id]
    contact_list_new = []
    if len(matches):
        contact_list_new.append(matches[0])
    
    return render_template('index_inerit.html', title='Home', user=user, contact_list=contact_list, from_get_phone='True', each_contact_list=contact_list_new)


if __name__ == '__main__':
    app.run()
