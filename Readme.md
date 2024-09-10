
v1.0 - Alfredo Romero - deploys en docker 

Usualmente el despliegue se encuentra en el archivo readme dentro de cada modulo

# Comandos útiles

# administración de docker files desplegados
docker ps -a 
docker rm docker_name


# Administración de networks
docker network create --subnet=172.18.0.0/29 api_test_net
docker network inspect api_test_net
docker rm net_name
docker network ls 

