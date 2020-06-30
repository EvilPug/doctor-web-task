# Тестовое задание для собеседования в компанию Doctor Web

<br>

#### Техническое задание

Реализовать HTTP API для загрузки, скачивания и удаления файлов с использованием хеширования.

Алгоритм - на выбор (был выбран md5).

Загрузка:
- получив файл от клиента, сервер сохраняет его на диск в следующую структуру каталогов: store/ab/abcdef12345... где "abcdef12345..." - имя файла, совпадающее с его хэшем, "ab" - подкаталог, состоящий из первых двух символов хэша файла, затем сервер возвращает в отдельном поле http response хэш загруженного файла


Скачивание:
- клиент передаёт параметр - хэш файла, затем сервер ищет файл в локальном хранилище и передает его на скачивание, если находит

Удаление:
- клиент передаёт параметр - хэш файла, затем сервер ищет файл в локальном хранилище и удаляет файл и прилежащий каталог если таковые существуют

<br>

#### Как развернуть проект локально?

    pip install -r requirements/base.txt
    cd ./src/
    python3 manage.py runserver

<br>
<i> Запущенный сервер доступен по адресу 127.0.0.1:8000 </i>
<br>

<h3> Загрузка файла с любым расширением </h3>

![upload](https://github.com/EvilPug/doctor-web-task/blob/master/screenshots/2_upload.png?raw=true)


<h3> Скачивание файла по хэшу </h3>

![download](https://github.com/EvilPug/doctor-web-task/blob/master/screenshots/3_download.png?raw=true)


<h3> Удаление файла по хэшу </h3>

![delete](https://github.com/EvilPug/doctor-web-task/blob/master/screenshots/4_delete.png?raw=true)

<h3> При вводе несуществующего хэша или не связанных с ним символов </h3>

![error](https://github.com/EvilPug/doctor-web-task/blob/master/screenshots/5_error.png?raw=true)
