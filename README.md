Flask-User is a user management app written  in python 3.4 with Flask, FLask-SQLAlchemy, marshmallow and PostgreSQL.

Its features include user roles, user session management with flask-login, password hashing and user status.

Please ensure PostgreSQL is installed with the development libraries. Steps are available [here](http://techarena51.com/index.php/flask-sqlalchemy-postgresql-tutorial/)


###Installation Steps
####Step 1:Clone the project to your application folder.

    git clone git@github.com:Leo-g/Flask-Skeleton.git YourAppFolderName

####Step 2: Activate the virtual environment.
 
    cd YourAppFolderName
    virtualenv -p /usr/bin/python3.4 venv-3.4
    source venv-3.4/bin/activate
    pip install -r requirements.txt 

#### Step 3 : Update the config file with your Database Username, Database Password, Database Name and Database Hostname

    vim config.py

#### Step 4 : Run migrations 
   
    python db.py db init
    python db.py db migrate
    python db.py db upgrade
    
####  Step 5 : Create an initial admin user: 
   Modify create_user.py with your email and password and then run
   
    python create_user.py  
   
####  Step 6 : Start the server
    python run.py

**You can then login with your email and password and create users at  http://localhost:5000/users/login**
