#!/usr/bin/env python3
import xmltodict
import json

import logging
logging.basicConfig()

from flask import Flask
app = Flask(__name__)

# The two variables below are global
iss_epoch_data = {}
iss_sighting_data = {}

@app.route('/', methods=['GET'])
def print_informatics() -> str:
    '''
    This function prints out information on the commands available for use 
    in this app and how to use them.
    
    Args: 
        None

    Returns: 
        string (str): A string of informational text on how to run this app.

    '''
    title = '    ISS Tracker\n\n'
    subtitle1 = '    Informational and management routes:\n\n'
    info1 = '    /' + '                              (GET) print this information\n'
    info2 = '    /read_data' + '                     (POST) reset data, load\
             from file\n\n\n'   
    subtitle2 = '    Routes for querying positional and velocity data:\n\n'
    info3 = '    /epochs' + '                        (GET) list all epochs\n'
    info4 = '    /epochs/<epoch>' + '                (GET) info on a specific\
             epoch\n\n\n'
    subtitle3 = '    Routes for querying sighting data:\n\n'
    info5 = '    /countries' + '                     (GET) List of all countries\n'
    info6 = '    /countries/<country>' + '           (GET) All data associated\
             with <country>\n'
    info7 = '    /countries/<country>/regions' + '   (GET) List of all regions\
             in a given country\n'
    info8 = '    /countries/<country>/regions/<region> (GET) All data associated\
             with <region>\n'
    info9 = '    /countries/<country>/regions/<region>/cities   (GET) List of\
             all cities in a given region\n'
    info10 = '    /countries/<country>/regions/<region>/cities/<city>   (GET)\
              All data associated with <city>\n\n' 
    return title + subtitle1 + info1 + info2 + subtitle2 + info3 + info4 +\
           subtitle3 + info5 + info6 + info7 + info8 + info9 + info10


@app.route('/read-data', methods=['GET','POST'])
def read_data_from_file_into_dict() -> str:
    '''
    This function reads in the data and assigns it to the proper variables. 
    It can be used to initialize or reset the data variables. Shows a help
    message if the command is typed incorrectly.

    Args:
        None

    Returns:
        string (str): Returns a message confirming that the data has been
                      uploaded if it works correctly. OR returns a helpful message
                      if user types command incorrectly.
    '''
    if(methods=='POST'):    
        global iss_epoch_data
        global iss_sighting_data


        with open('ISS.OEM_J2K_EPH.xml', 'r') as f:
            iss_epoch_data = xmltodict.parse(f.read())
        #iss_epoch_data = iss_epoch_data['ndm']['oem']['body']['segment']['data']['stateVector']
        iss_epoch_data = iss_epoch_data['ndm']['oem']['body']['segment']['data']
    

        with open('XMLsightingData_citiesUSA03.xml', 'r') as f:
            iss_sighting_data = xmltodict.parse(f.read())

        return str('Data has been uploaded')
    else:
        return '    This is a route for initializing or resetting data. You\
                must perform a POST request to this route to get it to\
                work, e.g.:\n\n' + '    curl -X POST localhost:5024/read-data'


@app.route('/epochs', methods=['GET'])
def return_list_of_epochs():############################################### This one needs type hints
    '''
    Once the data variables are initialized, this function returns a list
    of all epochs related to the positional data of the ISS that has been
    stored in the data.
    
    Args:
   
    Returns:

    '''
    epochs_list = ''
    #iss_epoch_data = iss_epoch_data['ndm']['oem']['body']['segment']['data']
    #return str(type(iss_epoch_data['stateVector']))  
    for i in range(len(iss_epoch_data)):
        epochs_list += str(iss_epoch_data[0]['EPOCH']) + '\n'

    return epochs_list


@app.route('/epochs/<epoch>', methods=['GET'])
def return_epoch_info(epoch: str) -> : #########################################33
    '''
    When given a specific epoch within the dataset, this function returns
    all the information known about it.

    Args:
        epoch (str): The name of the specific instance the user wants
                     information about.
    
    Returns:
        ##################################################################################
    '''
    pass


@app.route('/countries', methods=['GET'])
def return_list_of_countries() -> list:
    '''
    When prompted, returns a list of all countries the ISS has been sighted from.
    
    Args:
        None

    Returns:
        countries (list): A list of countries that have spotted the ISS at some
                          in time.
    '''
    pass


@app.route('/countries/<country>', methods=['GET'])
def return_country_specifics(country: str) -> dict:
    '''
    This function returns all information associated with the given country
    when prompted.

    Args: 
        country (str): The name of the country the user is searching for
                       information about.

    Returns:
        country_info (dict): a dictionary containing all relevant information
                             about the queried country.
    '''
    pass


@app.route('/countries/<country>/regions', methods=['GET'])
def return_list_of_regions(country: str) -> list:
    '''
    When given a country from the database, this function returns a list of
    all the regions in that country.

    Args:
        country (str): The name of the country in query.
 
    Returns:
        regions_in_country (list): A list of all the regions within the
                                   given country.

    '''
    pass


@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def return_region_specifics(country: str, region: str) -> dict:
    '''
    When asked for a specific region in a country, this function returns all
    data associated with the given region.

    Args:
        country (str): The name of the country within which the queried
                       region resides.
        region (ste):

    Returns:
        region_info (dict): A dictionary containing all relevant information
                            about the queried region.

    '''
    pass


@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def return_list_of_cities(country: str, region: str) -> list:
    '''
    Returns a list of all cities within a given region when prompted.

    Args: 
        country (str): The name of the country in which the queried region
                       resides.
        region (str):  The name of the region in which the program should
                       look for cities.

    Returns:
        cities_in_region (list): A list of all the cities within the given region.
   '''
    pass


@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GET'])
def return_city_specifics(country: str, region: str, city: str) -> dict:
    '''
    Returns all data associated with the given city when prompted.
    
    Args:
        country (str): The name of the country in which the queried region
                       resides.
        region (str): The name of the region in which the query pertains.

    Returns:
        city_info (dict): A dictionary containing the relevant information
                          on the queried city.
    '''
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
