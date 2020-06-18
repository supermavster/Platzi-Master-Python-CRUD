# Click

Click es un pequeño framework que nos permite crear aplicaciones de Línea de comandos. Tiene cuatro decoradores básicos:

```
@click_group: Agrupa una serie de comandos
```

```
@click_command: Aca definiremos todos los comandos de nuestra apliacion
```

```
@click_argument: Son parámetros necesarios
```

```
@click_option: Son parámetros opcionales
```

Los subdirecotrios son modulos (tal como clients)

Ambientes virtuales:

Para inicializar tu virtual enviroment en Windows:

1. Para instalar virtualenv:
   `pip install virtualenv`
2. Para verificar que está instalado:
   `where virtualenv`
3. Lleva tu proyecto a una cartera cuya ruta no contenga ningún espacio.
4. Inicializar el ambiente virtual estándo en la carpeta de tu proyecto:
   `virtualenv --python=python3 venv`
5. Activar el ambiente virtual:
   `call venv/Scripts/activate`
6. Listar paquetes instalados en el ambiente virtual:
   `pip freeze`
7. Instalar Click en el ambiente virtual (verificar después con paso 6.):
   `pip install click`
8. Crea en el directorio de tu proyecto el archivo requeriments.txt.
    ```
    Usa
    cualquiera de los métodos para esto en windows (bloc de notas -> Archivo
    -> Guardar, clic derecho -> Nuevo -> Documento de texto).
    ```
9. Para verificar desde consola la creación de requeriments.txt:
   `dir`
10. Vuelve al paso 6, copia y pega los resultados en requeriments.txt, guarda y sal.
11. Para instalar en otra ocasión o en otro equipo el mismo ambiente, virtual en el que trabajas:
    `pip install -r requeriments.txt`

```
virtualenv --python=python3 venv
python -m venv venv
source venv/Scripts/activate

# Exit
deactivate
```
