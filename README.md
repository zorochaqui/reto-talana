Este repositorio contiene una aplicación que se puede ejecutar en un contenedor Docker. Siga las instrucciones a continuación para construir y ejecutar la aplicación en su entorno local.

## Requisitos previos

Asegúrese de tener instalado Docker en su sistema. Puede descargar Docker desde [el sitio web oficial de Docker](https://www.docker.com/get-started).

## Instrucciones

### 1. Clonar el Repositorio

Clone este repositorio en su máquina local utilizando el siguiente comando:

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
```

### 2. Navegar al Directorio del Proyecto

Acceda al directorio del proyecto:

```bash
cd tu-repositorio
```

### 3. Construir la Imagen Docker

Ejecute el siguiente comando para construir la imagen Docker:

```bash
docker-compose build
```

### 4. Ejecutar el Contenedor

Una vez que la imagen Docker se haya construido con éxito, puede ejecutar el contenedor utilizando el siguiente comando:

```bash
docker-compose up
```

## Preguntas

1. **Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste. De ser posible, que quede solo un commit con los cambios.**

**Si ya hiciste "push"**:

1. Crea el archivo olvidado o realiza las modificaciones necesarias en tu repositorio local.

2. Realiza un nuevo commit para agregar estos cambios al historial de Git.

3. Utiliza el comando `git commit --amend`. Esto combinará tus cambios con el commit anterior y los incluirá en ese commit en lugar de crear un nuevo commit. Puedes editar el mensaje de commit si es necesario.

4. Realiza un "push" nuevamente con el comando `git push origin nombre-rama`, donde "nombre-rama" es el nombre de la rama en la que estás trabajando.

**Si aún no has hecho "push"**:

1. Crea el archivo olvidado o realiza las modificaciones necesarias en tu repositorio local.

2. Realiza un nuevo commit para agregar estos cambios al historial de Git.

3. Usa el comando `git stash` para guardar temporalmente los cambios que no se han registrado.

4. Luego, utiliza el comando `git pull` para actualizar tu repositorio local con los cambios más recientes del repositorio remoto.

5. Finalmente, utiliza el comando `git stash pop` para aplicar tus cambios guardados nuevamente. Esto creará un nuevo commit con los cambios que habías realizado anteriormente y los combinará con los cambios más recientes del repositorio remoto.

En ambos casos, puedes lograr que quede solo un commit con los cambios, lo que ayuda a mantener un historial limpio y ordenado en Git.

2. **Si has trabajado con control de versiones, ¿cuáles han sido los flujos con los que has trabajado?**

   los flujos trabajados han sido crear ramas, y usarlas para poder modificar estos, esos si se trabaja con un repositorio para Dev, Test y prod

3. **¿Cuál ha sido la situación más compleja que has tenido con esto?**

   El que me pidan de la rama actual dividir en 3 versiones, y modificación de cada una, y cada uno salia en una fecha determinada

4. **¿Qué experiencia has tenido con los microservicios?**

   He trabajado con rest, tambien con aws lambdas, django y flask

5. **¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?**

   Aws, no he podido probar servicios de GCP, sol he trabajado con AWS y ahondar bastante con cloudformation

