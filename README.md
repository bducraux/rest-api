# Rest API

## Executando o Servidor

1. Abra um terminal e navegue até a pasta root do projeto

2. Construindo o container:

```
docker-compose build
```

3. Migrando o banco de dados:
```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
```

4. Criando super usuário:

```
docker-compose run web python manage.py createsuperuser

sugestão de usuario para funcionar sem alterações no Postman:
email:admin@admin
password: admin
confirma a senha
y para aceitar senha
```

5. Execute o container:

```
docker-compose up
```
