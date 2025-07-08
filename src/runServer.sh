

if [ ! -f .env/bin/activate ];
then
    ./create_python_env.sh
fi

#setting the envirment
source .env/bin/activate
#export FLASK_APP=webServer
export FLASK_APP=trivial_compute
export FLASK_ENV=development
export FLASK_DEBUG=1
port=$1

if [ "$port" == "" ];
then
    port="5000"
fi

#cd backEnd/SQL
#echo "creating the database"
#python -m init_db
#cd ../..

echo "running the server on port : $port"
#cd backEnd/
#cd frontEnd/

flask run -p $port
