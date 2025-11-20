# Guía de Inicio Rápido para Rerun SDK

**Rerun** es un SDK y visualizador para registrar datos multimodales (imágenes, tensores, texto, nubes de puntos, etc.) en aplicaciones de visión por computadora y robótica. Te permite visualizar el estado interno de tu código a lo largo del tiempo.

## 1. Instalación

Asegúrate de tener Python 3.8+ instalado.

```bash
pip install rerun-sdk
```

## 2. Conceptos Básicos

*   **Logging (Registro):** En lugar de usar `print()`, usas `rr.log()` para enviar datos al visualizador.
*   **Entities (Entidades):** Los datos se organizan en una jerarquía de rutas, similar a un sistema de archivos (ej. `/camera/image`, `/world/points`).
*   **Timelines (Líneas de tiempo):** Puedes asociar datos a diferentes ejes temporales (ej. `frame_idx`, `log_time`, `sim_time`).
*   **Viewer:** La interfaz gráfica donde exploras los datos.

## 3. Tu Primer Script con Rerun

Crea un archivo llamado `rerun_demo.py` con el siguiente contenido:

```python
import rerun as rr
import numpy as np

# 1. Inicializar Rerun
rr.init("mi_primera_demo_rerun", spawn=True)

# 2. Crear algunos datos dummy (puntos en 3D)
# Generamos 100 puntos aleatorios
positions = np.random.normal(size=(100, 3))
colors = np.random.uniform(0, 255, size=(100, 3)).astype(np.uint8)

# 3. Registrar los datos
# Usamos set_time_sequence para definir un "momento" en el tiempo
for i in range(30):
    rr.set_time_sequence("frame_idx", i)
    
    # Movemos los puntos un poco en cada frame para animarlos
    positions += np.random.normal(scale=0.1, size=positions.shape)
    
    # Logueamos los puntos en la entidad "world/points"
    rr.log(
        "world/points", 
        rr.Points3D(positions, colors=colors, radii=0.1)
    )
    
    print(f"Registrando frame {i}...")

print("¡Listo! Revisa la ventana de Rerun.")
```

## 4. Ejecutar

Corre el script desde tu terminal:

```bash
python rerun_demo.py
```

Esto abrirá automáticamente el visualizador de Rerun en tu navegador o en una ventana nativa, mostrando los puntos moviéndose en 3D.

## 5. Siguientes Pasos

*   **Imágenes:** Prueba loguear imágenes con `rr.Image`.
*   **Tensores:** Visualiza matrices y tensores con `rr.Tensor`.
*   **Documentación:** Visita [rerun.io/docs](https://www.rerun.io/docs) para más ejemplos.
