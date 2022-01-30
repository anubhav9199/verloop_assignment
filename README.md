# verloop_assignment
this is the an api example created using django rest framework to show the basic functionality of the given Map API. 

### Requirements:
- Python3
- Django Framework
- Django Rest Framework

### How to run on local machine?
> Add a MasterConfig.ini file in the same directiory which contains the config key for the Map API in the iven below format
```
[config]
maps_key = your_key_here
```

> Go to the folder where you clone the repository.
> Run the following commands
>>- ```pip install -r requirements.txt```
>>- ```python manage.py runserver 8080```
<br/>

> Go to the terminal and write the curl code to see the demonstration live working.

> for Fetching the Data in JSON
>>- ```curl -X POST -H "Content-Type: application/json" -d '{"address":"3582, 13th G Main Rd, Channakesahava Nagar, HAL 2nd Stage, Doopanahalli, Indiranagar, Bengaluru, Karnataka 560008, India", "output_format":"json"}' http://127.0.0.1:8000/getAddressDetails```

> for Fetching the Data in XML
>>- ```curl -X POST -H "Content-Type: application/json" -d '{"address":"3582, 13th G Main Rd, Channakesahava Nagar, HAL 2nd Stage, Doopanahalli, Indiranagar, Bengaluru, Karnataka 560008, India", "output_format":"xml"}' http://127.0.0.1:8000/getAddressDetails```

