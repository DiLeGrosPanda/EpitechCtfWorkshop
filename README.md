# EpitechCtfWorkshop
Content for the CTF i organised for an Epitech Lyon workshop.
Using Flask as backend, NuxtJS (SSR+VueJS) as front end and mysql as DB (for sqli)
I learned on the fly so don't expect much :)

# Setup

+ you need to change your DB username/password in /back/server.py

## Back end setup
    # pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    pip install flask-restful flask-mysql
    python server.py # NOT for production

## Front end setup
    npm install
    npm run dev # NOT for production

## Mysql setup
    mysql -u DiLeGrosPanda -p # Replace with your credentials

    CREATE DATABASE workshop_secu;
    use workshop_secu;

    CREATE TABLE foods (
      id INT NOT NULL AUTO_INCREMENT,
      food_name VARCHAR(100) NOT NULL,
      food_desc VARCHAR(200) NOT NULL,
      food_link VARCHAR(200) NOT NULL,
      PRIMARY KEY ( id )
    );

    INSERT INTO foods VALUES (1, "Pizza", "Un gout delicieux", "/pizza.png");
    INSERT INTO foods VALUES (2, "Kebab", "Une viande exquise", "/kebab.png");
    INSERT INTO foods VALUES (3, "Raclette", "Une odeur exceptionnelle", "/raclette.jpeg");
    INSERT INTO foods VALUES (4, "Flag", "Flag{ThatWasAnEasyOne}", "/flag.jpeg");

    CREATE TABLE foods2 LIKE foods;
    INSERT INTO foods2 SELECT * from foods;
    update foods2 SET food_desc = "Flag{ThatIsCrazy}" where id = 4;

    CREATE TABLE fakeCreds (
        id INT NOT NULL AUTO_INCREMENT,
        pseudo VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        PRIMARY KEY (id)
    );

    INSERT INTO fakeCreds VALUES (1, "oops", "Flag{GgAdmin}");
