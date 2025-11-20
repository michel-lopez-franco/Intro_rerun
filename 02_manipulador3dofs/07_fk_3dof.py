import rerun as rr
import numpy as np
import time

# --- Parámetros (mismos que paso 06) ---
LINK_1_HEIGHT = 0.5
LINK_2_LENGTH = 1.0
LINK_3_LENGTH = 1.0

def log_robot(q1, q2, q3):
    # Base
    rr.log("world/base", rr.Boxes3D(half_sizes=[0.2, 0.2, 0.05], colors=[[100, 100, 100]]))
    
    # Joint 1 (Cintura)
    rr.log("world/link1", rr.Transform3D(rotation=rr.RotationAxisAngle(axis=[0,0,1], angle=q1)))
    rr.log("world/link1/geom", rr.Transform3D(translation=[0, 0, LINK_1_HEIGHT/2]))
    rr.log("world/link1/geom", rr.Boxes3D(half_sizes=[0.1, 0.1, LINK_1_HEIGHT/2], colors=[[255, 100, 0]]))
    
    # Joint 2 (Hombro)
    rr.log("world/link1/link2", rr.Transform3D(
        translation=[0, 0, LINK_1_HEIGHT],
        rotation=rr.RotationAxisAngle(axis=[0,1,0], angle=q2)
    ))
    rr.log("world/link1/link2/geom", rr.Transform3D(translation=[LINK_2_LENGTH/2, 0, 0]))
    rr.log("world/link1/link2/geom", rr.Boxes3D(half_sizes=[LINK_2_LENGTH/2, 0.08, 0.08], colors=[[0, 200, 255]]))
    
    # Joint 3 (Codo)
    rr.log("world/link1/link2/link3", rr.Transform3D(
        translation=[LINK_2_LENGTH, 0, 0],
        rotation=rr.RotationAxisAngle(axis=[0,1,0], angle=q3)
    ))
    rr.log("world/link1/link2/link3/geom", rr.Transform3D(translation=[LINK_3_LENGTH/2, 0, 0]))
    rr.log("world/link1/link2/link3/geom", rr.Boxes3D(half_sizes=[LINK_3_LENGTH/2, 0.06, 0.06], colors=[[100, 255, 100]]))
    
    # Efector
    rr.log("world/link1/link2/link3/end_effector", rr.Transform3D(translation=[LINK_3_LENGTH, 0, 0]))
    rr.log("world/link1/link2/link3/end_effector", rr.Points3D(positions=[[0,0,0]], radii=0.05, colors=[[255, 255, 255]]))

def main():
    rr.init("manipulator_tutorial_07", spawn=True)
    
    print("Animando robot 3DOF...")
    
    for t in range(200):
        rr.set_time_sequence("step", t)
        
        # Movimiento complejo
        q1 = np.deg2rad(45 * np.sin(t * 0.05))       # Cintura: Izquierda/Derecha
        q2 = np.deg2rad(-45 + 30 * np.cos(t * 0.05)) # Hombro: Arriba/Abajo
        q3 = np.deg2rad(45 * np.sin(t * 0.1))        # Codo: Flexión
        
        log_robot(q1, q2, q3)
        time.sleep(0.02)

    print("Paso 7 completado: Animación FK 3DOF.")

if __name__ == "__main__":
    main()
