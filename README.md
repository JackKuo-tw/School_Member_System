# School_Member_System
![Python Version](https://img.shields.io/badge/Python-3.5-green.svg)
![Django Version](https://img.shields.io/badge/Django-2.0-green.svg)
* For my university - [NCNU](http://www.gazette.ncnu.edu.tw/)
* A database course final project, using [Django](https://www.djangoproject.com/)

## Fearute
* import/search/mail member system
* Online form with authenticated
* Explore events photos/videos and one click download as zip
* Sample questions/Note for past exams
* Interesting project discuss, collecting ideas
* Calendar for NCNU CSIE

## HOWTO

建立虛擬環境

```python3 -m venv Django_venv```

啓用虛擬環境

```source Django_venv/bin/activate```

安裝必要套件

```pip install -r requirements.txt```

建立資料表

```python manage.py migrate```

啓動網頁伺服器

```python manage.py runserver```

