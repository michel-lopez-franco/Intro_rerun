import rerun as rr
import numpy as np
import time

# Importamos funciones de los pasos anteriores para no repetir código
# Nota: En un tutorial real, es mejor tener un archivo utils.py, pero aquí copiaremos
# las constantes y funciones necesarias para que cada archivo sea independiente.

L1 = 0.5
L2 = 1.0
L3 = 1.0

def log_robot(q1, q2, q3):
    rr.log("world/base", rr.Boxes3D(half_sizes=[0.2, 0.2, 0.05], colors=[[100, 100, 100]]))
    rr.log("world/link1", rr.Transform3D(rotation=rr.RotationAxisAngle(axis=[0,0,1], angle=q1)))
    rr.log("world/link1/geom", rr.Transform3D(translation=[0, 0, L1/2]))
    rr.log("world/link1/geom", rr.Boxes3D(half_sizes=[0.1, 0.1, L1/2], colors=[[255, 100, 0]]))
    rr.log("world/link1/link2", rr.Transform3D(translation=[0, 0, L1], rotation=rr.RotationAxisAngle(axis=[0,1,0], angle=q2)))
    rr.log("world/link1/link2/geom", rr.Transform3D(translation=[L2/2, 0, 0]))
    rr.log("world/link1/link2/geom", rr.Boxes3D(half_sizes=[L2/2, 0.08, 0.08], colors=[[0, 200, 255]]))
    rr.log("world/link1/link2/link3", rr.Transform3D(translation=[L2, 0, 0], rotation=rr.RotationAxisAngle(axis=[0,1,0], angle=q3)))
    rr.log("world/link1/link2/link3/geom", rr.Transform3D(translation=[L3/2, 0, 0]))
    rr.log("world/link1/link2/link3/geom", rr.Boxes3D(half_sizes=[L3/2, 0.06, 0.06], colors=[[100, 255, 100]]))
    rr.log("world/link1/link2/link3/end_effector", rr.Transform3D(translation=[L3, 0, 0]))
    rr.log("world/link1/link2/link3/end_effector", rr.Points3D(positions=[[0,0,0]], radii=0.05, colors=[[255, 255, 255]]))

def inverse_kinematics(x, y, z):
    q1 = np.arctan2(y, x)
    r = np.sqrt(x**2 + y**2)
    z_local = z - L1
    d = np.sqrt(r**2 + z_local**2)
    if d > (L2 + L3) or d < abs(L2 - L3): return None
    cos_q3 = (d**2 - L2**2 - L3**2) / (2 * L2 * L3)
    cos_q3 = np.clip(cos_q3, -1.0, 1.0)
    q3 = -np.arccos(cos_q3)
    alpha = np.arctan2(z_local, r)
    beta = np.arctan2(L3 * np.sin(q3), L2 + L3 * np.cos(q3))
    q2 = - (alpha - beta)
    return q1, q2, q3

def main():
    rr.init("manipulator_tutorial_09", spawn=True)
    
    # Definir puntos de paso (waypoints)
    points = [
        [1.5, 0.0, 0.5],
        [1.0, 1.0, 1.0],
        [0.0, 1.5, 0.5],
        [-1.0, 1.0, 1.0],
        [-1.5, 0.0, 0.5]
    ]
    
    # Visualizar waypoints
    rr.log("world/waypoints", rr.Points3D(positions=points, colors=[[255, 255, 0]], radii=0.05))
    
    print("Generando trayectoria...")
    
    # Interpolación simple
    steps_per_segment = 50
    
    for i in range(len(points) - 1):
        start = np.array(points[i])
        end = np.array(points[i+1])
        
        for step in range(steps_per_segment):
            t = step / steps_per_segment
            # Interpolación lineal (LERP) en espacio cartesiano
            current_pos = start + (end - start) * t
            
            # Calcular IK
            ik_sol = inverse_kinematics(current_pos[0], current_pos[1], current_pos[2])
            
            if ik_sol:
                q1, q2, q3 = ik_sol
                
                # Loguear en el tiempo global
                global_step = i * steps_per_segment + step
                rr.set_time_sequence("step", global_step)
                
                log_robot(q1, q2, q3)
                
                # Dibujar rastro
                rr.log("world/trace", rr.Points3D(positions=[current_pos], colors=[[0, 255, 0]], radii=0.02))
            
            time.sleep(0.01)

    print("Paso 9 completado: Trayectoria cartesiana.")

if __name__ == "__main__":
    main()
