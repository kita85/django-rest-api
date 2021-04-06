# Django Rest API Exercise
This application creates a single RESTful API endpoint which returns a filtered set of "batch job records" from the provided dataset. 

This sample demonstrates:

* ETL the provided CSV into a SQLite database
* Gracefully handles omissions within the example dataset
* Provide a functional API endpoint at /batch_jobs
* The API endpoint responds with a JSON-API document (string)
* The API endpoint correctly filters the dataset based upon any combination of filter keywords
* Provides basic test(s)

## Areas For Improvement

After taking a Saturday to quickly pickup Django for this exercise, I think the most obvious area of improvement is better domain knowledge. While I have experience 
with coding similar scenarios, Python and Django are both new to my repertoire. Aside from being new to the language, here are a few areas that I would like to see
fleshed out more.

* Error handling

  Currently there is no error handling being done for improper input. Both for type errors or for malicious input. 
  
* Ability to scale
  
  This application was built as an exercise in Python RESTful API's and did not have scalability as a priority.

* Authentication

  An auth token should be provided before results are received.

* URL Encoding

  A more robust method to handle URL Encoding when receiving the filters.
 
* String Output

  My biggest hurdle during this project was how to render an object instead of a string. This prevented me from formatting (parsing) the json easily in the view. 
  If in a real word situation, this would be a question I would ask someone more experienced in Django.


## Installation

#### Migrations
Run your migration to create the database schema

1. ```python3 manage.py makemigrations jobs```
2. ```python3 manage.py migrate```


#### Database
To import the database, run 

1. ```python3 manage.py shell```
2. ```exec(open('./jobs/import.py').read())```

To add a super user, run ```python3 manage.py createsuperuser```


#### Development Server

To start the Django development server, run ```python3 manage.py runserver```

To test the API, visit 
http://127.0.0.1:8000/batch_jobs?filter[submitted_after]='2018-02-28T15:00:00+00:00'&filter[submitted_before]='2018-03-01T15:00:00+00:00'&filter[min_nodes]=2&filter[max_nodes]=200


## Testing
Tests can be executed by running ```python3 manage.py test jobs```


## Built With

* [Python 3.9.2](https://www.python.org/)
* [Django 3.1.7](https://www.djangoproject.com/)


## Authors

* **Kita Cranfill** - *Development* - [GitHub](https://github.com/kita86)

