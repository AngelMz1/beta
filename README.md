# 🐍 Python Learning Repository

¡Bienvenido a mi repositorio de aprendizaje de Python! Este espacio está dedicado a documentar mi viaje aprendiendo uno de los lenguajes de programación más populares del mundo.

---

## 📚 Historia de Python

Python fue creado por **Guido van Rossum** y lanzado por primera vez en **1991**. El nombre del lenguaje proviene del grupo de comedia británico "Monty Python". 

### Características principales:
- 🎯 **Filosofía**: Enfatiza la legibilidad del código
- 🔧 **Sintaxis**: Limpia y fácil de entender
- 📐 **Estructura**: Uso de sangría significativa
- 🌍 **Comunidad**: Una de las más grandes y activas

---

## 🚀 Instalación

### Windows
1. Visita [python.org](https://www.python.org/downloads/)
2. Descarga la última versión estable
3. Ejecuta el instalador
4. ✅ **IMPORTANTE**: Marca la casilla "Add Python to PATH"
5. Verifica la instalación:
```bash
python --version
```

### macOS
```bash
# Usando Homebrew
brew install python
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

---

## 📊 Tabla de Variables y Nomenclatura

| Tipo de Variable | Nomenclatura | Ejemplo | Descripción |
| :--- | :--- | :--- | :--- |
| **Entero** | `snake_case` | `edad_usuario = 25` | Números enteros |
| **Flotante** | `snake_case` | `precio_producto = 19.99` | Números decimales |
| **Cadena** | `snake_case` | `nombre_completo = "Juan"` | Texto |
| **Booleano** | `snake_case` | `es_activo = True` | Verdadero/Falso |
| **Lista** | `snake_case` | `numeros_lista = [1, 2, 3]` | Colección ordenada |
| **Diccionario** | `snake_case` | `datos_usuario = {}` | Pares clave-valor |
| **Constante** | `UPPER_CASE` | `PI = 3.14159` | Valores inmutables |
| **Clase** | `PascalCase` | `class UsuarioSistema:` | Definición de clase |
| **Función** | `snake_case` | `def calcular_promedio():` | Definición de función |

### 📝 Reglas de Nomenclatura
- ✅ Usar nombres descriptivos
- ✅ Evitar abreviaciones confusas
- ✅ No usar palabras reservadas de Python
- ✅ Comenzar con letra o guión bajo, nunca con número

---

## 🔧 Entornos Virtuales

### ¿Qué es un entorno virtual?
Un entorno virtual es un espacio aislado donde puedes instalar paquetes de Python sin afectar la instalación global del sistema.

### 📋 Creación y Uso

#### 1️⃣ Crear un entorno virtual
```bash
# Crear entorno virtual
python -m venv nombre_del_entorno

# Ejemplo práctico
python -m venv mi_proyecto_env
```

#### 2️⃣ Activar el entorno virtual

**Windows:**
```bash
# Command Prompt
nombre_del_entorno\Scripts\activate

# PowerShell
nombre_del_entorno\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source nombre_del_entorno/bin/activate
```

#### 3️⃣ Verificar activación
Cuando esté activo, verás el nombre del entorno en tu terminal:
```bash
(mi_proyecto_env) usuario@computadora:~/proyecto$
```

#### 4️⃣ Instalar paquetes
```bash
# Instalar un paquete específico
pip install requests

# Instalar desde requirements.txt
pip install -r requirements.txt

# Ver paquetes instalados
pip list
```

#### 5️⃣ Crear archivo requirements.txt
```bash
# Generar lista de dependencias
pip freeze > requirements.txt
```

#### 6️⃣ Desactivar el entorno
```bash
deactivate
```

### 🎯 Mejores Prácticas
- 📁 Crear un entorno virtual por proyecto
- 📝 Mantener actualizado el archivo `requirements.txt`
- 🗑️ No incluir la carpeta del entorno virtual en el control de versiones
- 🔄 Usar nombres descriptivos para los entornos

---

## 📁 Estructura del Repositorio

```
mi-repo-python/
│
├── 📂 proyectos/          # Proyectos de práctica
├── 📂 ejercicios/         # Ejercicios resueltos
├── 📂 notas/             # Apuntes y documentación
├── 📄 requirements.txt    # Dependencias del proyecto
├── 📄 .gitignore         # Archivos a ignorar en Git
└── 📄 README.md          # Este archivo
```

---

## 🎯 Próximos Pasos

- [ ] Completar ejercicios básicos
- [ ] Explorar librerías populares
- [ ] Crear proyectos prácticos
- [ ] Contribuir a proyectos open source

---

## 📞 Contacto

¿Tienes preguntas o sugerencias? ¡No dudes en contactarme!

---

⭐ **¡No olvides dar una estrella a este repositorio si te resulta útil!** ⭐
