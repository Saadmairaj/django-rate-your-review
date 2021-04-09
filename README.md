# django-rate-your-review

[![CodeFactor](https://www.codefactor.io/repository/github/saadmairaj/django-rate-your-review/badge/master)](https://www.codefactor.io/repository/github/saadmairaj/django-rate-your-review/overview/master)


An online application that will give a rating to your reviews.

<p align="center">
  <img width="700" alt="Screenshot 2021-04-09 at 13 31 57" src="https://user-images.githubusercontent.com/46227224/114148942-f6ee5e80-9937-11eb-8fa3-4d5ccda6e393.png">
  <img width="700" alt="Screenshot 2021-04-09 at 13 30 36" src="https://user-images.githubusercontent.com/46227224/114148894-ea6a0600-9937-11eb-91c3-c4769bf8d4c4.png"> 
<p>

## Requirement

Install all the requirements with [requirements.txt](https://github.com/Saadmairaj/django-rate-your-review/blob/master/requirements.txt) with the command

```bash
pip install -r requirements.txt
```

Main packages used in the application are:
 
 - Django
 - django-crispy-forms
 - tensorflow
 
 ## Installation
 
 Install and run the server in 5 simple steps.
 
 - *Step 1:* Clone the repository.
 
 - *Step 2:* Create a virtual environment in the cloned directory with the following command:
   ```bash
   python3 -m venv env
   ```
  
   Note: If you get an error saying venv doesn't exist then install venv first with command [`pip install virtualenv`](https://pypi.org/project/virtualenv/).
 
 - *Step 3:* After creating the virtual environment, activate it with command:
   ```bash
   source ./env/bin/activate
   ```
  
 - *Step 4:* Now install the requirements into the virtual environement `evn` with command:
    ```bash
    pip install -r requirements.txt
    ```
  
 - *Step 5:* After installing all the requirements we are set to go! Just go run the server with the following command:
    ```bash
    python manage.py runserver
    ```
   
   
