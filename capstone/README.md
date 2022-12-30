# CS50W: Web Programming with Python and JavaScript

## Capstone
Designing and implementing a web application of your own with Python and JavaScript.

## Introduction
My final project is Simple Blog with Django. In this website,
- Users are able to register this site
- Make your own profile with profile picture, bio and add other platforms links to profile
- Add blog articles, images with category  
- Edit, Delete articles
- Users can add categories
- Users can like others articles
- Write comments on articles

The project was built using Django as a backend framework and HTML, Bootstrap, and JavaScript for the frontend. All generated information is saved in a database (SQLite by default).

All webpages of the project are mobile-responsive.

## Distinctiveness and Complexity
This web application is sufficiently distinct from the other projects in this course because in the views, earlier projects used basic views we created by own. passing our request and rendering our request to html template file we want to show. That's usually how we do things with django. But in this project, I used generic class-based views like ListView, DetailView etc. Also more complex than the last project, I use a user authentication system in a separate app to handle all that stuff. And use statis files to add the user's default profile picture.

## Installation

- Install project dependencies by running
```shell script
git clone https://github.com/me50/JaninduChanuka.git
cd JaninduChanuka
pip install -r requirements.txt
```
Dependencies include Django, django-ckeditor a rich text editor that allows writing content directly inside of web page and Pillow module that allows Django to work with images.

- Make and apply migrations by running
```shell script
python manage.py makemigrations
python manage.py migrate
```

- Create superuser with
```shell script
python manage.py createsuperuser
```
This step is optional

- Run your server
```shell script
python manage.py runserver
```

- Go to website address and register with new account.

## Contains in Files
 - `capstone` - main application directory.
    - `media/images` - contains all the images that uploads with article
      - `profile` - contains all the profile pictures of users.
    - `members` - app for users.
      - `forms.py` - contains forms of user application such as ProfilePage, SignUp, EditProfile, Password
      - `urls.py` - contains all URLs of members application. 
      - `views.py`- contains all views of members application.
      - `templates/registration` - contains all members application templates.
        - `change_password.html` - template contains password change fields.
        - `create_user_profile_page.html` - template to create user profile with profile picture, bio and social media urls.
        - `edit_profile_page.html` - template to edit user profile picture, bio and social media urls.
        - `edit_settings.html` - template to change username, first name, last name, email.
        - `login.html` - login template with username, passowrd.
        - `password_success.html` - template that shows when password changed successfully.
        - `register.html` - template to enter details to register with blog.
        - `user_profile.html` - template contains all user details.
    - `myblog` - app for blog content.
      - `admin.py` - registered Post,Category,Profile,Comment models.
      - `forms.py` - contains forms of blog application such as PostForm, EditForm, CommentForm, AddCategoryForm.
      - `models.py` - contains four models I used in the project. `Profile` model extends the standard User model, `Post` model is for posts, `Comment` represents users comments and `Category` models is for blog categories.
      - `urls.py` - contains all URLs of blog application. 
      - `views.py`- contains all views of blog application.
      - `templates` - contains all blog application templates.
        - `add_category.html` - template for add blog categories.
        - `add_comment.html` - template for add comments in articles.
        - `add_post.html` - template create new blog article.
        - `article.html` - template that shows a single post.
        - `base.html` - base template. All other tempalates extend from this.
        - `categories.html` - template that shows all articles wich belongs to category we choose.
        - `category_list.html` - template that shows all the categories as a list.
        - `delete_post.html` - template that display delete confirm.
        - `home.html` - template that shows all the blog articles. 
        - `update_post.html` - template to edit blog article.
     - `static/myblog/images` - contains all the default images(`default-profile-pic.png`)
