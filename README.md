## Demo
This project is actually created for doing some testing like, How a django project actually created?What is the folder structure?How to manage version control tools like github?What info should a developer need to add to his project and how to make clear documentation in 'README.md' file so that whoever wants to clone this project will have a total guideline for it? How to use DRF in Django project?And many other things.

Now let's see some of this project features along with explanations.

### Make endpoint
In a normal django project we can create a superuser and using that credentials we can login into the admin  site.And there if we add content, content got added into the frontend.When we are using normal django we are using MVT(Model, View, Template) architecture.But when we are using DRF(Django Rest Framework) we create routers, seralizers to make endpoints.

Routers:
![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/9d33d5ce-d015-4349-b9e6-846b4cef6226)
Here movies, actions, Thriller are 3 endpoints

Seralizers:
![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/f6e06d6f-c8d6-4c55-8259-395c5bd23b59)
Here name, duration, rating, genres, images can be added from a particular endpoints

Views:
![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/7cd61709-8525-43cb-b1a5-3eaf159808ad)

Inside views there are viewsets and these viewsets actually filtering data based on genres.But we can set the filtering as per our need.

Now let's take look into the frontend

Movies:
![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/772fc9ad-e980-4a6c-af32-24e0ec45754f)
Inside movies endpoint all of the movies are listed.

Action:
![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/20afc782-0e29-41ba-9bae-6354b3a0a9a5)
In this endpoint movies which got action genres are listed in this page.And action is also set as default genres.

Thriller:
![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/d62bf3ee-29a0-42f3-a1ca-a701701ff9dd)
In this endpoint movies which got Thriller genres are listed in this page.

In every page there are form so that user can add a new movie.Also user can write json data and then post it.
![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/b3cf0f05-d341-471a-845b-dd8a26a493d0)

![image](https://github.com/Emon-Khan/MovieRatingRestApi/assets/42010220/53e81f3d-1c27-4003-8f92-c61bf3234532)


