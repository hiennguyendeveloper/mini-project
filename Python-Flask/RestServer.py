from flask import Blueprint, jsonify, request
from Model import companies_db
import sqlite3

RestServer = Blueprint("RestServer", __name__)
RestServer = Blueprint("RestServer", __name__, url_prefix='/companies')

#blueprint to route to index page
@RestServer.route('/')
def index():
    return jsonify("Welcome back end, use PostMan for testing API")

#blueprint to route to add_a page
@RestServer.route('/add_company')
def add_company():
    data = request.get_json()
    name = data['name']
    address = data['address']
    city = data['city']
    state = data['state']
    zipcode = data['zip_code']
    
    #f make pull the value {varible} into string, """ help write sqlite execute into multiple line
    conn.execute(f""" INSERT INTO Companies 
                (name, addr, city, state, zipcode) 
                VALUES ({name}, {address}, {city}, {state}, {zipcode}) """)
    conn.commit()
    return jsonify({'success': True})



@RestServer.route('/edit_company/<int:id>')
def edit_company(id):
    data = request.get_json()
    name = data['name']
    address = data['address']
    city = data['city']
    state = data['state']
    zip_code = data['zip_code']
    
    success = companies_db.edit_company(id, name, address, city, state, zip_code)
    return jsonify({'success': success})

#blueprint for route to delete company
@RestServer.route('/delete_compan/<int:id>')
def delete_company(id):
    success = companies_db.delete_company(id)
    return jsonify({'success': success})


cursor.execute(
        """DELETE FROM Tasks WHERE taskId=:taskId""", 
        {"taskId": taskId})

#blueprint for route get a company by their id
@RestServer.route('/get_company_by_id/<int:id>')

def get_company_by_id(id):
    company = companies_db.get_company_by_id(id)
    if company is not None:
        return jsonify(company.to_dict())
    else:
        return jsonify({'message': 'Company not found'})


#blueprint for route get all companies
@RestServer.route('/get_all_companies')
def get_all_companies():
    companies = companies_db.get_all_companies()
    return jsonify(companies)