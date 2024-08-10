# Guía para Configurar un Ambiente Local en Python

Esta guía te ayudará a configurar un ambiente de desarrollo local en Python, utilizando herramientas como PyCharm, Miniconda y Poetry. Además, se incluye una breve explicación sobre `if __name__ == "__main__":`.

## 1. Instalar PyCharm

**PyCharm** es un entorno de desarrollo integrado (IDE) específicamente diseñado para el desarrollo en Python. Proporciona características como depuración, análisis de código y un potente editor que facilita el desarrollo.

### Pasos para instalar PyCharm:
1. Visita [el sitio web oficial de PyCharm](https://www.jetbrains.com/pycharm/download/).
2. Descarga la versión de tu sistema operativo (Windows, macOS, Linux).
3. Sigue las instrucciones del instalador.

> **Nota:** Existen dos versiones: la **Community Edition** que es gratuita y de código abierto, y la **Professional Edition** que es de pago pero incluye más características avanzadas.

## 2. Instalar Miniconda

**Miniconda** es una versión ligera de Anaconda que incluye solo `conda`, Python, y las bibliotecas necesarias para crear entornos virtuales y gestionar dependencias. Es ideal si prefieres tener más control sobre las bibliotecas que instalas.

Un entorno virtual en Python es una herramienta que permite crear un espacio aislado para instalar dependencias y paquetes específicos para un proyecto, sin afectar el sistema global de Python o otros proyectos. Esto asegura que las versiones de las bibliotecas utilizadas en un proyecto no entren en conflicto con las de otros proyectos, proporcionando un control más preciso sobre el entorno de desarrollo.

Lectura Sugerida
Para una comprensión más profunda sobre los entornos virtuales en Python, te recomiendo leer https://docs.python.org/es/3/tutorial/venv.html. No es necesario seguir el tutorial completo, pero es útil tener una idea general de cómo funcionan los entornos virtuales.
### Pasos para instalar Miniconda:
1. Visita [el sitio web oficial de Miniconda](https://docs.conda.io/en/latest/miniconda.html).
2. Descarga el instalador adecuado para tu sistema operativo. Ojo 64 o 32 bits, para mac tener en cuenta el chip M1
3. si te pregunta si deseas agregar conda al PATH, selecciona "yes". dice algo como: Add miniconda to my PATH environment variable, seleccionan el check. El resto de opciones las dejan por defecto. OJO EN EL VIDEO NO LO MARCAN, USTEDES SI LO DEBEN MARCAR.
4. Sigue las instrucciones de instalación.
5. Para verificar la instalación, abre una terminal y ejecuta:

   ```bash
   conda --version
    ```

Deberías ver la versión de conda instalada.

Video sugerido: https://www.youtube.com/watch?v=oHHbsMfyNR4, OJO AQUI NO SELECCIONEN LA OPCION DE AGREGAR AL PATH, USTEDES SI LO DEBEN HACER!!!!!!
## 3. Instalar Poetry con pip

Poetry es una herramienta de gestión de dependencias y empaquetado para Python. Facilita la instalación y gestión de bibliotecas, además de automatizar tareas comunes en el desarrollo.

### Pasos para instalar Poetry:
1. Abre una terminal.
2. Ejecuta el siguiente comando para instalar Poetry usando pip:

  ```bash
  pip install poetry 
  ```
  
3. Para verificar la instalación, ejecuta:

  ```bash
poetry --version
  ```


## 4. Comandos Básicos de Poetry

### 4.1. Agregar una Librería

Para agregar una nueva librería a tu proyecto:
 
```bash
poetry add <nombre-de-la-libreria>
  ``` 


### 4.2. Instalar Dependencias

Para instalar todas las dependencias especificadas en el archivo `pyproject.toml`:

```bash
poetry install
  ``` 



### 4.3. Remover una Librería

Para remover una librería de tu proyecto:
    
```bash
    poetry remove <nombre-de-la-libreria>
``` 



## 5. Explicación de `if __name__ == "__main__":`

En Python, `if __name__ == "__main__":` es un constructo utilizado para comprobar si un script está siendo ejecutado directamente o si está siendo importado como un módulo en otro script.

### ¿Qué significa esto?
- `__name__`: Es una variable especial que Python asigna al nombre del módulo que se está ejecutando. Si el módulo es el programa principal que se está ejecutando, entonces `__name__` se establece como `"__main__"`.
- `if __name__ == "__main__":`: Esta condición se evalúa como `True` si el archivo es el script principal que se está ejecutando. Permite que un script ejecute un bloque de código solo si se está ejecutando directamente, no cuando se importa.

### Ejemplo:
Supongamos que tenemos dos scripts: `script1.py` y `script2.py`. El contenido de `script1.py` es el siguiente:

```python
def saludar():
    print("¡Hola desde script1!")

print("El valor de __name__ en script1 es:", __name__)

if __name__ == "__main__":
    saludar()
```
en este ejemplo, `__name__` se establece como `"__main__"` porque `script1.py` es el script principal que se está ejecutando. Por lo tanto, el bloque de código dentro del `if __name__ == "__main__":` se ejecutará y se llamará a la función `saludar()`.