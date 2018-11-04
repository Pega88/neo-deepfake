# neo-deepfake
Deepfake Neo Hackathon submission


**PrivateNet**

* $ docker pull cityofzion/neo-privatenet

* $ docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet

* $ docker cp neo-privatenet:/opt/node1/neo-cli/wallet1.json .

**Flask**

* pip install Flask

* export FLASK_APP=main.py

* flask run --host=0.0.0.0 -p 8080
