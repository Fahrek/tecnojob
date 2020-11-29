from django.shortcuts import render, HttpResponse
import psycopg2
import psycopg2.extras
import os, cgi
import cgitb; cgitb.enable()


# Create your views here.
def index(request):
    # return HttpResponse('Hola bienvenid@ a TecnoJob')
    return render(request, "searcher.html")


def offer_insert(request):
    conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
    cursor = conn.cursor()
    cursor.execute("insert into offer (title, salary, remote, publi_date, company_id, cat_id) values (%s, %s, %s, %s, %s, %s);", ('DBA', 10000, True, '2020-11-28', 4, 1))
    conn.commit()
    cursor.close()
    conn.close()
    return HttpResponse('Registro Insertado')
    # return render(request, "offer_create.html")


def offer_select(request):
    conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
    cursor = conn.cursor()
    cursor.execute("select * from offer;")
    return HttpResponse(cursor.fetchall())
    # return render(request, "offer_read.html")


def offer_update(request):
    conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
    return render(request, "offer_update.html")


def offer_delete(request):
    conn = psycopg2.connect(dbname="tecnojob00", user="postgres", password="47601469W", host="localhost", port=5432)
    return render(request, "offer_delete.html")


def offer_save_file():
    form = cgi.FieldStorage()
    # Obtener el nombre del archivo.
    fileitem = form['filename']
    # Comprobar si el archivo ha sido subido correctamente
    if fileitem.filename:
        # strip leading path from file name to avoid
        # directory traversal attacks
        fn = os.path.basename(fileitem.filename)
        open('/tmp/' + fn, 'wb').write(fileitem.file.read())
        message = 'The file "' + fn + '" was uploaded successfully'
    else:
        message = 'No file was uploaded'

    # print
    # """\
    # Content-Type: text/html\n
    # <html>
    # <body>
    #    <p>%s</p>
    # </body>
    # </html>
    # """ % (message,)



