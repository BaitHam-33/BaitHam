# BaitHam


#### Authors: 

* Afik Danan - afikda@ac.sce.ac.il
* Topaz Aakal – topazaa@ac.sce.ac.il
* Avigail Shekasta - avigash@ac.sce.ac.il
* Daniel Diei - Danieha6@ac.sce.ac.il

#### Description:

The project is part of "Fundamentals in Software Engineering" course. 
We are group #33.
This is a website for an animal shelter. 
The website have three users: 
* Adopters - the regular user, annonymos user, this user can read articles and success stories, donate to the shelter, view the animals available for adoption, adopt an animal,
reoprt for an abuse or missing animal, view reports (like how many animals in the shelter and more), get info about upcoming event and ask question in the forum.
* Volunteer - the staff at shelter, have more permissions compare to the adopters. The staff can see all the pages like the adopter but can do more things for example: 
to add/edit/delete an animal to/from the database, also the volunteers have a Task board in it they can see all the "to do task" and assign themself for a task. The Volunteers 
can log in to their account and report thier attandence, Moreover they can download all kind of useful reports to their computers. Beside that they can respond in forum and respond
to a report made by adopter.
* Manager- the manager of the shelter is the person with all the permissions, he create users in the database (the volunteer users), he can download all the reports, view evrything
and control the database, edit objects, create objects and delete them. The manger creates the tasks for the volunteers to see.   

#### Environment:
  the code was devloped on pycharm, the framework is django 4.0.0, most of the code is python, but we have some html and css code

#### How to run:

```
git clone https://github.com/BaitHam-33/BaitHam.git
 ```
#### Requirements:
```
pip install asgiref==3.4.1  
pip install Django==4.0    
pip install django-filter==21.1   
pip install Pillow==8.4.0  
pip install pip==21.3.1 
pip install reportlab==3.6.3  
pip install sqlparse==0.4.2
pip install tzdata==2021.5
pip install xlwt==1.3.0
```

#### Create tables
```
 python manage.py makemigrations
 python manage.py migrate
```

#### Start the application (development)
 ```
 python manage.py runserver
```

 #### Access the web app in browser: http://127.0.0.1:8000/
 
#Unit Test
```
python manage.py test                # all tests
python manage.py test Animal         # Animal test
python manage.py test Article        # Article test
python manage.py test Donations      # Donations test
python manage.py test Event          # Event test
python manage.py test forum          # forum test
python manage.py test Report         # Report test
python manage.py test success_story  # success_story test
python manage.py test Taskboard      # Taskboard test
python manage.py test volunteer      # volunteer test
      
```
