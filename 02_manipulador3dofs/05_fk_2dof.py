import rerun as rr
import numpy as np
import time

def main():
    rr.init("manipulator_tutorial_05", spawn=True)

    l1 = 1.0
    l2 = 1.0
    
    # Geometría (reutilizada del paso anterior)
    box_half_size_1 = [l1/2, 0.1, 0.1]
    box_center_1    = [l1/2, 0, 0]
    box_half_size_2 = [l2/2, 0.08, 0.08]
    box_center_2    = [l2/2, 0, 0]

    # Bucle de simulación
    print("Iniciando animación de Cinemática Directa (2DOF)...")
    
# 0. Origen del sistema de coordenadas
    rr.log("world/origin", rr.Arrows3D(vectors=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], colors=[[255,0,0], [0,255,0], [0,0,255]]))

    for t in range(100):
        # Generamos ángulos que cambian con el tiempo
        # q1 oscila entre -45 y 45 grados
        q1 = np.deg2rad(45 * np.sin(t * 0.1))
        # q2 oscila más rápido
        q2 = np.deg2rad(90 * np.cos(t * 0.1))
        
        # --- Actualizar Rerun ---
        # Rerun permite actualizar los datos en el mismo path.
        # Al usar rr.set_time_sequence, podemos grabar la historia.
        rr.set_time_sequence("step", sequence=t)

        # Link 1
        rr.log("world/link1", rr.Transform3D(rotation=rr.RotationAxisAngle(axis=[0,0,1], angle=q1)))
        rr.log("world/link1/geom", rr.Transform3D(translation=box_center_1))
        rr.log("world/link1/geom", rr.Boxes3D(half_sizes=box_half_size_1, colors=[[255, 100, 0]]))
        
        # Link 2
        rr.log("world/link1/link2", rr.Transform3D(
            translation=[l1, 0, 0],
            rotation=rr.RotationAxisAngle(axis=[0,0,1], angle=q2)
        ))
        rr.log("world/link1/link2/geom", rr.Transform3D(translation=box_center_2))
        rr.log("world/link1/link2/geom", rr.Boxes3D(half_sizes=box_half_size_2, colors=[[0, 200, 255]]))
        
        # Efector final (visualización)
        rr.log("world/link1/link2/end_effector", rr.Transform3D(translation=[l2, 0, 0]))
        rr.log("world/link1/link2/end_effector", rr.Points3D(positions=[[0,0,0]], colors=[[255,255,255]], radii=0.05))

        # Cálculo manual de la posición del efector (solo para imprimir o verificar)
        # x = l1*cos(q1) + l2*cos(q1+q2)
        # y = l1*sin(q1) + l2*sin(q1+q2)
        x_ee = l1 * np.cos(q1) + l2 * np.cos(q1 + q2)
        y_ee = l1 * np.sin(q1) + l2 * np.sin(q1 + q2)
        
        # Podemos loguear la posición calculada como un punto en el mundo para verificar la traza
        rr.log("world/trace", rr.Points3D(positions=[[x_ee, y_ee, 0]], colors=[[255, 255, 0]], radii=0.02))

        time.sleep(0.05)

    print("Paso 5 completado: Animación FK 2DOF.")

if __name__ == "__main__":
    main()
