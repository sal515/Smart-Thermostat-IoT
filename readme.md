# Project: Smart Thermostat (IoT) using MQTT Protocol 

## Description of the Entities 
   The project has three different MQTT client entities and one MQTT server entity.
   The following section will provide an overview of the use

   * ##### The MQTT Server Implementation using Python sockets
        * Driver file name (file in project root directory):
                
                * app_server.py
            
            * Other application files in directory
                
                * control_packets
            
        * Brief Description:
        
            * The Server was implemented using python's built-in SocketServer framework. The TCP SocketServer.TCPServer class used to implement the server workflow and every new request is handled in a separate thread. Details of the python server framework can be found in https://docs.python.org/2/library/socketserver.html. 
            

   * ##### All three MQTT client entities were implemented using the paho-mqtt library.
       
       1. User Application
            
            * Driver file name (file in project root directory):
                
                    * app_client.py  
            
            * Other application files in directory
                * app_client
                * databaseHelper/json_helpers
            
            * Publish Topics: 
                * "smart_home/user_data"
                * "smart_home/presence_data"
            
            * Brief description
                * Allows the user to provide their name and their preferred temperature room. And publishes the user information to two different topics mentioned above.
                    
       2. Door locker Application 
                   
            * Driver file name (file in project root directory):
                
                    * app_door_locker.py 
            
            * Other application files in directory
                * app_door_locker
                * databaseHelper/json_helpers
            
            * Subscribed Topics: 
                * "smart_home/user_data"
                            
            * Published Topics
                * "smart_home/presence_data"
             
            * Brief description
                * Emulates a smart monitoring system, that identifies if a person either entered or left the house. For the purpose of the simulation, the application asks the user to change the presence of a user, who have already registered using the User Application mentioned above.
        
       3. Thermostat Application 
                    
            * Driver file name (file in project root directory):
                
                    * app_thermostat.py  
            
            * Other application files in directory
                * app_thermostat
                * databaseHelper/json_helpers
            
            * Subscribed Topics: 
               * "smart_home/presence_data"
            
            * Brief description
                * A smart thermostat simulator, it sets the preferred temperature of person who entered the house the earliest. The temperature is set to the preference of the person first in the queue. 
        



###Libraries required for the project:
* The libraries are listed in the requirements.txt file of the project
    * The **requirements.txt** file can be used to install all the required libraries
* A list of the libraries are provided below:
    
    * MQTT Python Client Library:
        * paho-mqtt==1.5.0
            * pip install paho-mqtt
            * Download link: https://pypi.org/project/paho-mqtt/
    * Local database libraries:
        * filelock==3.0.12
            * pip install filelock
            * Download link: https://pypi.org/project/filelock/
        * SQLAlchemy==1.3.16
            * pip install SQLAlchemy
            * Download link: https://pypi.org/project/SQLAlchemy/
            
    * All other imports found in the project are built-in python libraries for standard python installation.

###Python Version - Tested:
* Python interpreter
    * **3.7.2**
  
### Operating system - Tested:
* Windows 10 Home

### Installation steps on Windows:


