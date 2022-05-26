# -*- coding: utf-8 -*-
"""
Created on Thu May 26 09:53:57 2022

@author: siddhardhan.s
"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/aadhaar_details_retrieval')
def retrieve_aadhaar(aadhaar_num : str):
    
    aadhaar_details = {
            
            'first_name' : 'Wilbur',
            'last_name' : 'Damron', 
            'dob': '15/09/1967',
            'age': '54',
            'aadhaar_number': aadhaar_num,
            'gender': 'Male', 
            'father_name': 'Vasant Surve' ,
            'father_no' : '-' ,
            'mother_name': '-' ,
            'mother_no': '-' ,
            'mobile_no': '6364194446',
            'email_addr': '-' ,
            'city': 'Mumbai' ,
            'state': 'Maharashtra' ,
            'country': 'India' ,
            'pin_code': '400010' ,
            'addr': '3e/10, 2nd Floor, Majithia Nagar, S.v.road,Mumbai,Maharashtra-400010'
        }

    
    return aadhaar_details
