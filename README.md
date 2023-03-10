# Django-Stripe-Test-Task

## **Тестовое задание**
### **Описание**
[stripe.com/docs](stripe.com/docs) - платёжная система с подробным API и бесплатным тестовым режимом для имитации и тестирования платежей. С помощью python библиотеки stripe можно удобно создавать платежные формы разных видов, сохранять данные клиента, и реализовывать прочие платежные функции. 
Мы предлагаем вам познакомиться с этой прекрасной платежной системой, реализовав простой сервер с одной html страничкой, который общается со Stripe и создает платёжные формы для товаров. 
Для решения нужно использовать Django. Решение бонусных задач даст вам возможность прокачаться и показать свои умения, но это не обязательно. 
### **Задание**
Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
Django Модель Item с полями (name, description, price)

*API с двумя методами:*

**GET /buy/{id}**, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

**GET /item/{id}**, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на */buy/{id}*, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму **stripe.redirectToCheckout(sessionId=session_id)**.

- Пример реализации можно посмотреть в пунктах 1-3 [тут](https://stripe.com/docs/payments/accept-a-payment?integration=checkout)
- Залить решение на Github, описать запуск в Readme.md
- Опубликовать свое решение чтобы его можно было быстро и легко протестировать. 
- Решения доступные только в виде кода на Github получат низкий приоритет при проверке.

**Бонусные задачи:**

 &#9745; Запуск используя Docker

 &#9745; Использование environment variables

 &#9745; Просмотр Django Моделей в Django Admin панели

 &#9745; Запуск приложения на удаленном сервере, доступном для тестирования

 &#9744; Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

 &#9744; Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe  
 в таком случае они корректно отображаются в Stripe Checkout форме. 

 &#9744; Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте

 &#9744; Реализовать не Stripe Session, а Stripe Payment Intent.

Демонстрация доступна по адресу http://niksan3452.pythonanywhere.com/. Срок действия истекает 18 мая 2023 года.

## **Запуск**

Склонируйте репозиторий:

```https://github.com/NikSan3452/Django-Stripe-Test-Task.git```

Перейдите в папку Django-Stripe-Test-Task:

```cd Django-Stripe-Test-Task```

Создайте новое виртуальное окружение:

```python -m venv venv```

Установите зависимости:

```pip install -r requirements.txt```

Выполните миграции:

```python manage.py migrate```

Создайте суперпользователя для доступа к панели администратора:

```python manage.py createsuperuser```

Создайте файл `.env` в котором должны быть указаны следующие переменные окружения:

```SECRET_KEY = секретный ключ Django```

```DEBUG = True/False```

```STRIPE_PUBLISHABLE_KEY = Публичный ключ Stripe```

```STRIPE_SECRET_KEY = Секретный ключ Stripe```

Заупустите сервер:

```python manage.py runserver```

Откройте браузер и перейдите по адресу:

```http://127.0.0.1:8000```

Для добавления товаров перейдите в панель администратора и добавьте новые записи во вкладке "Товары":

```http://127.0.0.1:8000/admin```

### **Запуск в Docker**

В папке Django-Stripe-Test-Task выполните следующую команду:

```docker-compose up --build```

Откройте браузер и перейдите по адресу:

```http://127.0.0.1:8000```


