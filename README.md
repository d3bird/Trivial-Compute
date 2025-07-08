# Trivial-Compute game

this is the game

# requirments

bash
docker

# how to build

to build the server container run this script
`./buildServerContainer.sh`

# how to run the apllications

to boot up a instance of the server run this script 
`./bootServer.sh`  
if container has not been built when this script is ran, it will call the buildServerContainer.sh script

#the database was generated with teh following commands

flask db upgrade
flask db migrate -m "users table"
flask db upgrade