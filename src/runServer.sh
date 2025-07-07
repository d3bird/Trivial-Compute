

if [ ! -f .env/bin/activate ];
then
    ./create_python_env.sh
fi

#setting the envirment
source .env/bin/activate
export FLASK_APP=webServer
export FLASK_ENV=development

hostIP=$1
port=$2

if [ "$port" == "" ];
then
    port="5000"
fi

#listening on quad 0s currently
if [ "$hostIP" == "" ];
then
    hostIP="0.0.0.0"
fi

cd backEnd/SQL
echo "creating the database"
python -m init_db
cd ../..

echo "running the server on port : $port"
cd backEnd/

flask run -p $port -h $hostIP
