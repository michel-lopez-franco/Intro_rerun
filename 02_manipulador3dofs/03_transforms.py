import rerun as rr
import numpy as np

def main():
    rr.init("manipulator_tutorial_03", spawn=True)

    # Dimensiones del eslabón
    half_sizes = [0.5, 0.1, 0.1] # Largo total 1.0 en X

    # 0. Origen del sistema de coordenadas
    rr.log("world/origin", rr.Arrows3D(vectors=[[1, 0, 0], [0, 1, 0], [0, 0, 1]], colors=[[255,0,0], [0,255,0], [0,0,255]]))

    # 1. Dibujar el eslabón original en el origen (transparente para referencia)
    rr.log(
        "world/link_origin",
        rr.Boxes3D(half_sizes=half_sizes, colors=[[200, 200, 200, 100]])
    )

    # 2. Aplicar una Transformación (Traslación + Rotación)
    # Queremos mover otro eslabón a una posición (x=0, y=1, z=0) y rotarlo 45 grados en Z.
    
    translation = [0, 1.5, 0]
    
    # Rotación de 45 grados alrededor del eje Z
    # Rerun usa cuaterniones (x, y, z, w) o axis-angle.
    # Usaremos axis-angle para claridad: Eje Z [0,0,1], Ángulo 45 deg (pi/4)
    rotation_axis = [0, 0, 1]
    rotation_angle = np.pi / 4 # 45 grados
    
    # Rerun Transform3D
    rr.log(
        "world/transformed_frame",
        rr.Transform3D(
            translation=translation,
            rotation=rr.RotationAxisAngle(axis=rotation_axis, angle=rotation_angle)
        )
    )

    # Ahora dibujamos el eslabón "dentro" de este nuevo sistema de coordenadas "transformed_frame"
    # Nota la ruta: world/transformed_frame/link_moved
    rr.log(
        "world/transformed_frame/link_moved",
        rr.Boxes3D(half_sizes=half_sizes, colors=[[255, 100, 0]])
    )
    
    # Dibujamos ejes locales para ver la rotación
    rr.log("world/transformed_frame/axis", rr.Arrows3D(vectors=[[0.5,0,0], [0,0.5,0], [0,0,0.5]], colors=[[255,0,0],[0,255,0],[0,0,255]]))

    print("Paso 3 completado: Transformaciones espaciales.")

if __name__ == "__main__":
    main()
