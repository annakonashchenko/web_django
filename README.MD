Инструкция: как подготовить и запустить проект
1. Клонируйте репозиторий и перейдите в папку проекта:
   git clone https://github.com/ваш-проект.git cd web_django
2. Создайте и активируйте виртуальное окружение. Убедитесь, что вы находитесь в корне проекта (проверьте с помощью команды `pwd`):
   python -m venv venv
   source venv/bin/activate  # для Linux/MacOS
   venv\Scripts\activate     # для Windows или
   venv\Scripts\activate.bat  
3. Установите все необходимые зависимости:
   pip install -r requirements.txt
4. Выполните миграции базы данных:
   python manage.py migrate
5. Запустите сервер и проверьте работоспособность:
   python manage.py runserver