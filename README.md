# learnDjango
Repository made to learn how Django works

Django denomina "aplicación" a un componente del proyecto. Creamos una app con el comando
    py manage.py startapp posts
Un componente tendrá una carpeta "migrations" y los archivos:
    __init__.py 
        Indica a la máquina que es un módulo Python
    admin.py
        Vincula la App con el módulo de administración interno de Django
    app.py
        Contiene configuración propia de la App
    models.py
        Guarda las clases del sistema que interactúan con la DB
    tests.py
        Clases utilizadas para automatizar Tests
    views.py
        Interfaz entre usuario y sistema

Django sólo conoce las Apps cuando están declaradas en el archivo settings.py

Admin
    Podremos gestionar componentes de cada App una vez que los agreguemos al admin.py. Para esto hay que importar el modelo correspondiente y agregar la línea "admin.site.register(Modelo)". https://docs.djangoproject.com/en/3.1/ref/contrib/admin/actions/

Modelos
    Los atributos deben definirse a partir de un tipo de dato. Los posibles tipos de datos están documentados en https://docs.djangoproject.com/en/3.1/ref/models/fields/#field-types

Vistas
    Hay distintos tipos de vistas: basadas en funciones y basadas en clases.
    Una vista involucra un pedido (request) y una respuesta (HttpResponse, render, etc).
    Podemos modularizar el archivo principal de urls para importar las urls correspondientes a cada app