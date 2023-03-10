# Django-Car-API

<h1 align="center">
  <br>
  <a href=""><img src="https://www.iti.gov.eg/assets/images/iti-logo.png" alt="ITI" width="200"></a>
  <br>
  ITI
  <br>
</h1>

<h4 align="center">This is a simple Django application that provides a RESTful API for managing cars. The API allows you to view, create, update and delete cars.
.</h4>


![screenshot](https://www.educative.io/cdn-cgi/image/f=auto,fit=contain,w=1200/api/page/4851104629129216/image/download/5817722754564096)
---------------------------------------------------------------
## How to run
---------------------------------------------------------------
pip install virtualenv
----------------------------------------------------------------
virtualenv my_env_name
----------------------------------------------------------------
virtualenv my_env_name to create a new environment
----------------------------------------------------------------
source my_env_name/bin/activate to activate the new environment
----------------------------------------------------------------
python manage.py migrate
----------------------------------------------------------------
python manage.py runserver
----------------------------------------------------------------

---------------------------------------------------------------
 Use a REST client (e.g. Postman) to make API requests to the following endpoints:
<table><thead><tr><th>Endpoint</th><th>Method</th><th>Description</th></tr></thead><tbody><tr><td><code>/car/</code></td><td>GET</td><td>View all cars</td></tr><tr><td><code>/car/&lt;str:car_name&gt;</code></td><td>GET</td><td>View a specific car by name</td></tr><tr><td><code>/car/</code></td><td>POST</td><td>Create a new car</td></tr><tr><td><code>/car/&lt;str:car_name&gt;</code></td><td>PUT</td><td>Update a specific car by name</td></tr><tr><td><code>/car/&lt;str:car_name&gt;</code></td><td>DELETE</td><td>Delete a specific car by name</td></tr></tbody></table>
---------------------------------------------------------------

To use this Django project with Postman, follow these steps:
---------------------------------------------------------------
    Download and install the latest version of Postman on your computer.
---------------------------------------------------------------
    Launch Postman.
---------------------------------------------------------------
    Click on the "Import" button in the top left corner of the Postman window.
---------------------------------------------------------------
    In the Import dialog box, select "Import From Link" and paste the following
## [Link](https://github.com/bedaba/Django-Car-API/blob/main/simple-api.postman_collection.json)

    After importing the collection, you will see a list of all available API endpoints for your Django project in the Postman Collections tab.
## Created BY

[![Bedaba Edward](https://avatars.githubusercontent.com/u/21156712?v=4)](https://github.com/bedaba)

[Bedaba Edward ](https://github.com/bedaba) 

## [License](https://github.com/bedaba/Django-Car-API/blob/main/LICENSE)

MIT

