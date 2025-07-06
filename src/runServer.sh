

if [ ! -f .env/bin/activate ];
then
    ./create_python_env.sh
fi

#setting the envirment
source .env/bin/activate
export FLASK_APP=webServer
export FLASK_ENV=development

port=$1

if [ "$port" == "" ];
then
    port="5000"
fi

echo "running the server on port : $port"
cd backEnd/webServer

flask run -p $port
