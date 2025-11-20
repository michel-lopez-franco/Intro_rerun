import rerun as rr
import numpy as np

def main():
    rr.init("manipulator_tutorial_04", spawn=True)

    # Definimos dimensiones de los eslabones
    # Link 1: Largo 1.0
    l1 = 1.0
    # Link 2: Largo 1.0
    l2 = 1.0
    
    # Geometría de las cajas (centradas en su sistema local)
    # Para que un eslabón gire desde su extremo, debemos desplazar la geometría
    # de modo que el eje de rotación esté en un extremo, no en el centro.
    # Estrategia: El sistema de coordenadas del Link está en la articulación (base del link).
    # La geometría del link se desplaza +L/2 en X para que "nazca" del origen.
    
    box_half_size_1 = [l1/2, 0.1, 0.1]
    box_center_1    = [l1/2, 0, 0] # Desplazamiento del centro de la caja
    
    box_half_size_2 = [l2/2, 0.08, 0.08]
    box_center_2    = [l2/2, 0, 0]


    # 0. Origen del sistema de coordenadas
    rr.log("world/origin", rr.Arrows3D(vectors=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], colors=[[255,0,0], [0,255,0], [0,0,255]]))

    # --- Eslabón 1 (Base) ---
    # Supongamos que está rotado 30 grados
    q1 = np.deg2rad(30)
    
    rr.log("world/link1", rr.Transform3D(rotation=rr.RotationAxisAngle(axis=[0,0,1], angle=q1)))
    
    # Dibujamos la geometría del Link 1. 
    # Nota: Usamos un transform intermedio para posicionar la caja relativa al frame del joint
    rr.log("world/link1/geom", rr.Transform3D(translation=box_center_1))
    rr.log("world/link1/geom", rr.Boxes3D(half_sizes=box_half_size_1, colors=[[255, 100, 0]]))
    
    # --- Eslabón 2 (Hijo de Link 1) ---
    # El frame del Link 2 está al final del Link 1.
    # Traslación: [l1, 0, 0] (en el sistema de Link 1)
    # Rotación: q2 (digamos -45 grados)
    q2 = np.deg2rad(-45)
    
    rr.log("world/link1/link2", rr.Transform3D(
        translation=[l1, 0, 0],
        rotation=rr.RotationAxisAngle(axis=[0,0,1], angle=q2)
    ))
    
    # Dibujamos geometría Link 2
    rr.log("world/link1/link2/geom", rr.Transform3D(translation=box_center_2))
    rr.log("world/link1/link2/geom", rr.Boxes3D(half_sizes=box_half_size_2, colors=[[0, 200, 255]]))

    # Marker en el efector final
    rr.log("world/link1/link2/end_effector", rr.Transform3D(translation=[l2, 0, 0]))
    rr.log("world/link1/link2/end_effector", rr.Points3D(positions=[[0,0,0]], colors=[[255,255,255]], radii=0.1))

    print("Paso 4 completado: Cadena cinemática padre-hijo.")

if __name__ == "__main__":
    main()
