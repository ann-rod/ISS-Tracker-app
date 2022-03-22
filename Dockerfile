FROM centos:7.9.2009

RUN yum update -y && \
    yum install -y python3

RUN pip3 install pytest==7.0.0 && \
    pip3 install --user flask && \
    pip3 install --user xmltodict
    

COPY ISS.OEM_J2K_EPH.xml /code/ISS.OEM_J2K_EPH.xml

COPY XMLsightingData_citiesUSA03.xml /code/XMLsightingData_citiesUSA03.xml

COPY app.py /code/app.py

RUN chmod +rx /code/app.py

#RUN chmod +rx /code/ISS.OEM_J2K_EPH.xm

#RUN chmod +rx /code/XMLsightingData_citiesUSA03.xml

ENV PATH "/code:$PATH" 
