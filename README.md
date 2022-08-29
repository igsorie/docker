# Docker

![Docker](índice.png)
1. [Introducción](#id1)
2. [Red](#id2)
3. [Almacenamiento](#id3)
4. [Imagenes](#id4)
5. [Instalación](#id5)
6. [Docker Compose](#id6)
7. [Dockerfile](#id7)

## Introducción<a name="id1"></a> 

Docker es un proyecto de código abierto que automatiza el despliegue de aplicaciones dentro de contenedores de software, proporciona una capa de abstraccción y automatización de virtualización de aplicaciones en múltiples sistemas operativos.

**Contenedores:** 
* Def1. Unidad de software que empaqueta el código y todas las dependencias necesarias de una aplicación
* Def2. Es otra capa adicional de donde van a ejecutar las capas de imagenes, es decir, donde van a correr nuestras imagenes.

Los contenedores tiempre tienen estados asignados y los estados disponibles son:
 * Created
 * restarting
 * running
 * removing
 * paused
 * exited
 * dead 

El ciclo de vida es temportal, de lectura y escritura. Cuando se elimina un contenedor se elimina toda la información almacenada en el contenedor.

**Imágenes:** Paquete ligero y ejecutable de software con todo lo necesario para la aplicación

**Docker Engine:** Motor de ejecución de contenedores.

**Docker Hub:** Repositorio por defecto para las imágenes de docker

**Docker Compose:** Orquestador ligero de contenedores.

**Docker Swarm:** Orquestador de contenedores que permite manejar un cluster.

**Kubernetes:** Sistema para la administración de clusters y Orquestador Empresarial de contenedores.

## Red<a name="id2"></a> 

Tipo de conexión entre contenedores y el resto del mundo. Hay 5 tipos de drivers.

* **Bridge:** Es el driver por defecto, se utiliza para comunicar contenedores en el mismo docker host. La puerta de enlace de esta red es la interfaz docker que se crea en la instalación de docker.

* **Overlay:** Es el driver que se utiliza para conectarme con otros contenedores en otro docker hub.








## Almacenamiento<a name="id3"></a> 


## Imagenes<a name="id4"></a> 

Una imagen es una plantilla creada a partir de una serie de instrucciones para luego crear contenedores en base a esta. Para crear imagenes vamos a crear un archivo llamado Dockerfile


## Instalación<a name="id5"></a> 
~~~

#sudo apt-get update

#sudo apt-get install 
    ca-certificates \
    curl \
    gnupg \
    lsb-release

#sudo mkdir -p /etc/apt/keyrings

#curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

#echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

#sudo apt-get update

# apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

#docker version
~~~

Luego de instalado agregamos al los usuarios que querramos al grupo Docker con el comando: **usermod -aG docker ${USER}**

## Docker Compose<a name="id6"></a> 

* Instalación
apt-get install docker-compose-plugin

## Dockerfile<a name="id7"></a>

Es un documento de texto que contiene todos los comandos que vamos a ejecutar a la hora de crear nuestra imagen. Se podría decir que nuestro dockerfile va a ser la receta que docker va a seguir para poder crear nuestra imagen.

* El comando **FROM** nos va a servir para basar nuestra imagen en una imagen ya existenete. Este comando siempbre tienen que ser el primero en nuestro dockerfile.

        Ej: FROM node:11


* El comando **RUN** nos va a servir para correr comandos en una terminal dentro de nuestro container. Esto es util para cambiar configuración a nivel de sistema operarivo o bien instalar paquetes de forma global.

        RUN npm install -g pm2 --silent

* El mando **CMD** nos va a servir para indicarle a nuestra imagen que comando tiene que correr por defecto para crear nuestro contenedor. En caso de que nuestro comando contenga parámetros hay que escribir el comando en formato de array[]

        CMD ["node". "server.js"]

* El comando **EXPOSE** nos va a servir para indicarle a nuestro container que puerto escuchar muentras esté corriendo. Esto es especialmente útil para cuando estamos corriendo un servidor

        EXPOSE 3000

* El comando **WORKDIR** nos va a serviro para indicarle a nuestra imagen que directorio tiene que usar como base para los comandos que modifiquen el sistema de archivos. En caso de que no exista el directorio indicado, docker lo va a crear.

        WORKDIR /usr/src/app

* El comando **COPY** nos va a servir para copiar archivos desde nuestra computadora a nuestra imagen de Docker. Con el mando COPY podemos copiar archivos o directorios completos.

        COPY test.txt .

        COPY ..

El comando ENV nos va a servir para crear variables de ambiente dentro de nuestra imagen. Por ejemplo para indicarle si estamos en el ambiente de testing o producción

    ENV NODE_ENV production

Ejemplo de Dockerfile

FROM node:10.15-alpine
WORKDIR /usr/src/app
COPY ..
RUN npm run build
EXPOSE 3001
CMD ["nmp", "start"]