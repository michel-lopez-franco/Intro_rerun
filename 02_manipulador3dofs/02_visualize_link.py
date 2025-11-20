import rerun as rr
import numpy as np

def main():
    rr.init("manipulator_tutorial_02", spawn=True)

    # Definimos un "eslabón" (link) como una caja (Box3D)
    # Dimensiones: Largo=1.0, Ancho=0.2, Alto=0.2
    link_dimensions = [1.0, 0.2, 0.2]
    
    # Visualizamos el eslabón en el origen
    # Nota: Por defecto, las cajas en Rerun se centran en su posición.
    # Si queremos que el eslabón "nazca" del origen y se extienda a lo largo de X,
    # tendríamos que desplazarlo, pero por ahora lo dibujaremos centrado para ver la primitiva.
    
    rr.log(
        "world/link1",
        rr.Boxes3D(half_sizes=[d/2 for d in link_dimensions], colors=[[200, 100, 0]])
    )

    # Agregamos un sistema de coordenadas de referencia para ver dónde está el centro
    rr.log("world/origin", rr.Arrows3D(vectors=[[0.5, 0, 0], [0, 0.5, 0], [0, 0, 0.5]], colors=[[255,0,0], [0,255,0], [0,0,255]]))

    print("Paso 2 completado: Visualización de un eslabón básico.")

if __name__ == "__main__":
    main()
