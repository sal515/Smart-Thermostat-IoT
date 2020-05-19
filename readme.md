# Project: Smart Thermostat (IoT) using MQTT Protocol 

## Description of the Entities 
   The project has three different MQTT client entities and one MQTT server entity.
   The following section will provide an overview of entities. 

   * ##### The MQTT Server Implementation using Python sockets
        * Driver file name (file in project root directory):
                
                * app_server.py
            
            * Other required files of the entity are in the directory
                
                * control_packets
                * databaseHelper/sql_helpers
            
        * Brief Description:
        
            * The Server was implemented using python's built-in SocketServer framework. The TCP SocketServer.TCPServer class used to implement the server workflow and every new request is handled in a separate thread. Details of the python server framework can be found in https://docs.python.org/2/library/socketserver.html. 
            

   * ##### All three MQTT client entities were implemented using the paho-mqtt library.
       
       1. User Application
            
            * Driver file name (file in project root directory):
                
                    * app_client.py  
            
            * Other required files of the entity are in the directory
                * app_client
                * databaseHelper/json_helpers
            
            * Publish Topics: 
                * "smart_home/smart_thermostat"
            
            * Brief description
                * Allows the user to provide their name and their preferred temperature room. And publishes the user information to two different topics mentioned above.
                    
       2. Door locker Application 
                   
            * Driver file name (file in project root directory):
                
                    * app_door_locker.py 
            
            * Other required files of the entity are in the directory
                * app_door_locker
                * databaseHelper/json_helpers
            
            * Subscribed Topics: 
                * "smart_home/smart_thermostat"
                            
            * Published Topics
                * "smart_home/smart_thermostat"
             
            * Brief description
                * Emulates a smart monitoring system, that identifies if a person either entered or left the house. For the purpose of the simulation, the application asks the user to change the presence of a user, who have already registered using the User Application mentioned above.
        
       3. Thermostat Application 
                    
            * Driver file name (file in project root directory):
                
                    * app_thermostat.py  
            
            * Other required files of the entity are in the directory
                * app_thermostat
                * databaseHelper/json_helpers
            
            * Subscribed Topics: 
               * "smart_home/smart_thermostat"
            
            * Brief description
                * A smart thermostat simulator, it sets the preferred temperature of person who entered the house the earliest. The temperature is set to the preference of the person first in the queue. 
        



### Libraries required for the project:
* The libraries are listed in the **requirements.txt** file of the project
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
            
    * Virtual environment (Recommended)
        * virtualenv
            * python -m pip install --user virtualenv
            * Download link: https://virtualenv.pypa.io/en/latest/installation.html#via-pip
            * Installation guide on Windows: https://programwithus.com/learn-to-code/Pip-and-virtualenv-on-Windows/
                
    * All other imports found in the project are built-in python libraries for standard python installation.


###Python Version - Tested:
* Python interpreter
    * **3.7.2**
  
### Operating system - Tested:
* Windows 10 Home

### Installation steps on Windows:
* Pre-requisites 
    1. Ensure the following are installed
       * Python 3.7.2+ should be available
       * Virtualenv application should be installed
        
            * To install virtualenv (Windows 10)
            
                a. Open command prompt and verify python and pip is installed 
                
                    * pip --version
                    * python --version 
            
                b. Enter the pip command in the terminal: 
                
                    * pip install virtualenv
                
    2. Create a new Virtual Environment using the installed virtualenv
        
        a. Move to the project directory, one can use the following command: 
             
             cd C:\<...>\Smart-Thermostat-IoT
        
        b. A virtual environment should be created at the project root directory from the command prompt:
            
            virtualenv venv

        c. Activate the virtual environment by issuing the following command from the **project root directory**. This runs the venv activation batch script: 
            
            venv\Scripts\activate.bat
        
        d. If the virtual environment was successfully activated, the command prompt will show (venv) on the left of each new line
   
    3. **Install** all the **required python libraries** in the virtual environment using the **requirements.txt** file 
        
            * pip install -r requirements.txt
        
        * Following the command all the required libraries will be installed in the virtual environment
        
   
   * All the libraries should be installed and setup to run the applications.  
    
     
    
### Run instructions:

i. Please open 4 separate command prompts in windows 10
    
ii. Activate the virtual environment in each command prompt

   * To activate the virtual environments, in each command prompt do the following steps:
        
        * cd <root_directory_of_the_project>
        
   * Activate the virtual environment by running: 
        
        * venv\Scripts\activate.bat

   * Once all the command prompt window has the virtual environment activated, proceed to the next step     
iii. Please **run the applications** **in sequence** from the **root directory** of the project:
    
     1.  python app_server.py
     
     2.  python app_client.py
     
     3.  python app_door_locker.py
     
     4.  python app_thermostat.py


iv. Follow the prompts in each of the user application. 


### UI inputs of each application 

* python app_server.py
    
    * No inputs, socket and packet detail print outs for publish and subscribe packets

* python app_client.py

    * Username
    * Preferred Temperature
    
* python app_door_locker.py

    * Select from available options of which user is should enter or exit based on current status
    
* python app_thermostat.py

    * No input, only current temperature reading
    
    
