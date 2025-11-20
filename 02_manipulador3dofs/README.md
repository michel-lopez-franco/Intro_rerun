# Tutorial: Manipulador 3 Grados de Libertad (3DOF) con Rerun

Este tutorial te guiará paso a paso en la construcción, simulación y visualización de un robot manipulador de 3 grados de libertad utilizando Python y Rerun.

## Requisitos
- Python 3.8+
- `rerun-sdk`
- `numpy`
- `scipy` (opcional, para rotaciones avanzadas, pero usaremos numpy principalmente)

Instalación:
```bash
pip install rerun-sdk numpy
```

## Contenido

1. **01_setup_rerun.py**: Configuración básica de Rerun y visualización del sistema de coordenadas mundial.
2. **02_visualize_link.py**: Cómo visualizar un objeto 3D (un eslabón del robot) usando primitivas.
3. **03_transforms.py**: Entendiendo las transformaciones (traslación y rotación) en 3D.
4. **04_chain_links.py**: Conectando dos eslabones (padre e hijo).
5. **05_fk_2dof.py**: Cinemática Directa (Forward Kinematics) para un brazo plano de 2 grados de libertad.
6. **06_robot_3dof.py**: Construcción de la geometría completa del robot de 3 grados de libertad.
7. **07_fk_3dof.py**: Cinemática Directa para el robot 3DOF.
8. **08_ik_geometric.py**: Cinemática Inversa (Inverse Kinematics) enfoque geométrico.
9. **09_trajectory.py**: Generación de trayectorias simples (punto a punto).
10. **10_full_animation.py**: Animación completa de una trayectoria usando la línea de tiempo de Rerun.

## Ejecución
Para correr cada paso, simplemente ejecuta:
```bash
python 01_setup_rerun.py
```
(y así sucesivamente para cada archivo)
