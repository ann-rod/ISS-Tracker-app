# ISS Tracker App

## This app uses data provided by NASA to track the progress of the International Space Station in its voyage above the Earth.
With this app, you can access information on where the ISS was passing over at specific moments, as well as information on sightings of the ISS from Earth.


* To download the data used in this app, [NASA's website](https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq) for the Public Distribution File
and the Sighting Data File. For this specific project I used 'XMLsightingData_citiesUSA03' as my Sighting Data File, but any should work. *


## Dockerfile
  
  **Build Your own Dockerfile**:
  -Download the code in this directory.
  -Open up *Dockerfile* using your text editor of choice and make the necessary changes (whether you need to use different    versions of the software I used or would prefer to come up with your own commands)
  -Build a new image by typing 'docker build -t username/app.py:1.0 .' in the command line.
  -Run the application by typing 'docker run --rm -it username/app:1.0 /bin/bash'.
~~~~
docker build -t username/app.py:1.0 .
docker run --rm -it username/ml_data_analysis:hw04 /bin/bash
docker run --rm -it username/app:1.0 /bin/bash
~~~~

  **Using the Complete Dockerfile Provided (and Makefile)**:
  -If you wish to use the Dockerfile provided, and downloaded everything in the repo, change into the directory where the      code is, and simply type 'make build' followed by 'make run' into the command line. 
~~~~
 cd codeLocation
 make build
 make run
~~~~

 **Using an existing image on Docker Hub**:
 -Download the application by typing into the command line 'docker pull annrod/app:1.0'
 -Run the application using the command 'docker run --rm -it annrod/annrod/app:1.0 /bin/bash' to open the application.
~~~~
docker pull annrod/app:1.0
docker run --rm -it annrod/annrod/app:1.0 /bin/bash
~~~~


## Using the App
# The app contains several commands that can be used to find information on the navigation of the ISS:

To use any of the commands available, simply type: curl localhost:5024/command

  ** 1. URL: / **
        (GET) print information on the application commands
  
  ** 2. URL: /read-data **
        (POST) initialize or reset data (load from file)
  
  ** 3. URL: /epochs **
        (GET) list all epochs (instances of flight recorded)
        Interpretation: will show you a list of several instances that the ISS has traveled above the Earth
  
  ** 4. URL: /epochs/<epoch> **
        (GET) info on a specific epoch (type the ame of the one you want to look at where the <epoch> is)
        Interpretation: Look into a specific moment and see exactly what coordinates the ISS was overheard of
  
  ** 5. URL: /countries ** 
        (GET) List of all countries with ISS sightings
        Interpretation: See a list of places where the ISS has recently been spotted from
  
  ** 6. URL: /countries/<country> **
        (GET) All data of specific country you choose (similar directions as #4)
        Interpretation: See the sightings and epochs that happened at the country you chose
  
  ** 7. URL: /countries/<country>/regions ** 
        (GET) List of all regions in a given conutry
        Interpretation: See all the regions within a chosen country that have had sightings
  
  ** 8. URL: /countries/<country>/regions/<region> **
        (GET) All data associated with the region of your choosing (similar to #4,6)
        Interpretation: See all sighting data that is related to the country you cohose
  
  ** 9. URL: /countries/<country>/regions/<region>/cities ** 
        (GET) List of all cities in a given region (similar to #4,6,8)
        Interpretation: Find all the cities in a region that have seen the ISS from ground
  
  ** 10. URL: /countries/<country>/regions/<region>/cities/<city> **
        (GET) All data associated with a city of your choosing (similar to #4,6,8,9)
        Interpretation: see all sighting data at the city of your choosing
  
  
  examples:
  ~~~
  1. curl localhost:5024/
  2. curl localhost:5024/read-data -X POST. <-- important to type this one exactly
  3. curl localhost:5024/epochs                                            
  4. curl localhost:5024/epochs/<epoch>
  5. curl localhost:5024/countries
  6. curl localhost:5024/countries/<country>
  7. curl localhost:5024/countries/<country>/regions/<region>
  8. curl localhost:5024/countries/<country>/regions/<region>
  9. curl localhost:5024/countries/<country>/regions/<region>/cities
  10.  curl localhost:5024/countries/<country>/regions/<region>/cities/<city>
  ~~~
  
  
  
  # Citation:
  
    Both the Public Distribution File as well as the Sighting Data came from the official NASA website.
  
    “ISS_COORDS_2022-02-13 | NASA Open Data Portal.” NASA, NASA, 13 Feb. 2022, data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq.
    
                                                
