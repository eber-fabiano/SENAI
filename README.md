# SENAI

# Banco de dados
- Instalar o banco de dados PostgreSQL
- Executar o scrit: CREATE DATABASE senai WITH OWNER = postgres ENCODING = 'UTF8' TABLESPACE = pg_default CONNECTION LIMIT = -1 IS_TEMPLATE = False;
- Criar a tabela monitoring: 
  create table monitoring (
    id integer generated always as identity not null,
    mac_address varchar(50) not null,
    date timestamp without time zone not null,
    classe varchar(100) not null,
    evidence text not null,
    constraint pk_monitoring primary key(id)	
  );

# Anaconda
- Criar ambiente django: conda create --name django python=3.10
- Ativar ambiente djando: conda activate django
- Instalar as dependêndias: 
  pip install djangorestframework
  pip install django-rest-swagger
  pip install djangorestframework-simplejwt
  pip install psycopg2 
  (MacBook) pip install psycopg2-binary
  pip install django-base64field
- Criar o usuário padrão, para isto no diretório ./api_senai executar os comandos abaixo:
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
     Username: admin   
     Email address: admin@apisenai.com.br
     Password: Senai@2023
- Provavelmente ocorrerá o erro arquivo index.html do swagger, para isto verifique a Known Issue do link abaixo:
  https://roytuts.com/how-to-use-swagger-with-python-based-django-rest-apis/
  O arquivo index.html corrigido está no Google Drive: https://drive.google.com/drive/folders/1n6Y12PgOJNQfadhs0iUxk0xCYzBsQ7gX?usp=sharing
- Executar o server: python manage.py runserver
- Em outro terminal criar ambiente yolov7: conda create --name yolov7 python=3.10
- Ativar ambiente yolov7: conda activate yolov7
- Instalar as depenências do yolov7:
  pip install -r ./yolov7/requirements.txt
  pip install requests 
  pip install getmac
- Baixar os pesos da rede neural YOLO diponível no Google Drive: https://drive.google.com/drive/folders/1n6Y12PgOJNQfadhs0iUxk0xCYzBsQ7gX?usp=sharing
- Adicionar os pesos da rede neural best.pt no seguinte caminho: ./yolov7/runs/train/mouse/weights
- Iniciar a detecção pela webcam: python detect.py --weights runs/train/mouse/weights/best.pt --conf 0.6 --img-size 640 --source 0

# Observação
- O treinamento da rede neural YOLO ocorreu por meio de 348 imagens de mouses, onde o dataset foi dividido em 279 imagens de treinamento, 34 imagens para teste e 35 imagens para validação. Todas as imagens foram anotadas utilizando a ferramenta labelme (https://github.com/wkentaro/labelme).

# Melhorias a serem realizadas
- Refatorar o código da detecção do objeto de interesse, separando a lógica de consumo da API da implementação do YOLO (arquivo ./yolov7/detect.py).
- Implementar a lógica para renovar automaticamente o refresh_token após 24 horas (arquivo ./yolov7/detect.py).
- Estudar como passar os parâmetros para a API utilizando PathParam (arquivo ./api_senai/rest_api/views.py).
- Adaptar o código para rodar API no Docker Compose.

