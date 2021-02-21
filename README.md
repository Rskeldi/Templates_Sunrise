# Templates_Sunrise

1. Создайте виртуальное окружение venv 

2. Активируйте его и скачайте всё из requirments.txt

pip install -r requirments.txt

3. Файл 'secret_example.py' переименуйте в 'secret.py', и заполните все поля.
   (В поле "EMAIL_HOST_PASSWORD" нужно указывать специальный пароль для приложений, а не пароль от почтового ящика)
   
4. Проведите все миграции

python manage.py migrate

5. Запустите сервер