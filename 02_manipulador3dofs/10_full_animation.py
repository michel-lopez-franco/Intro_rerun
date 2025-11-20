import rerun as rr
import numpy as np

# --- Configuración ---
L1, L2, L3 = 0.5, 1.0, 1.0

def log_robot(q1, q2, q3):
    # Misma función de visualización
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
    # Inicializamos Rerun
    rr.init("manipulator_tutorial_10_final", spawn=True)
    
    print("Generando animación completa (Círculo en el espacio)...")
    
    # Definir una trayectoria circular en el plano YZ (x constante)
    center = [1.0, 0.0, 1.0]
    radius = 0.5
    
    num_steps = 200
    
    for t_idx in range(num_steps):
        theta = 2 * np.pi * t_idx / num_steps
        
        # Círculo en plano YZ desplazado en X
        x = center[0]
        y = center[1] + radius * np.cos(theta)
        z = center[2] + radius * np.sin(theta)
        
        ik_sol = inverse_kinematics(x, y, z)
        
        if ik_sol:
            q1, q2, q3 = ik_sol
            
            rr.set_time_sequence("frame", t_idx)
            rr.set_time_seconds("sim_time", t_idx * 0.05)
            
            log_robot(q1, q2, q3)
            
            # Dibujar la trayectoria deseada completa (estática)
            # Para ver por dónde va a pasar
            if t_idx == 0:
                 path_points = []
                 for k in range(num_steps):
                     th = 2 * np.pi * k / num_steps
                     path_points.append([center[0], center[1] + radius * np.cos(th), center[2] + radius * np.sin(th)])
                 rr.log("world/path", rr.LineStrips3D(strips=[path_points], colors=[[255, 255, 0]]))

            # Dibujar el punto actual
            rr.log("world/target", rr.Points3D(positions=[[x, y, z]], colors=[[255, 0, 0]], radii=0.05))

    print("Paso 10 completado: Animación final generada. Revisa el visor de Rerun.")

if __name__ == "__main__":
    main()
