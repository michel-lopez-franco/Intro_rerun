import rerun as rr
import numpy as np

# Definición de parámetros del robot 3DOF
# Configuración: Antropomórfica (Cintura, Hombro, Codo)
# Joint 1: Rotación Z (Cintura)
# Joint 2: Rotación Y (Hombro)
# Joint 3: Rotación Y (Codo)

LINK_1_HEIGHT = 0.5 # Base a Hombro
LINK_2_LENGTH = 1.0 # Hombro a Codo
LINK_3_LENGTH = 1.0 # Codo a Muñeca

def log_robot(q1, q2, q3):
    """
    Función helper para dibujar el robot dado los ángulos de las articulaciones.
    q1: Cintura (Z)
    q2: Hombro (Y)
    q3: Codo (Y)
    """
    
    # --- Base (Estática) ---
    rr.log("world/base", rr.Boxes3D(half_sizes=[0.2, 0.2, 0.05], colors=[[100, 100, 100]]))
    
    # --- Joint 1 (Cintura) ---
    # Rota en Z.
    rr.log("world/link1", rr.Transform3D(rotation=rr.RotationAxisAngle(axis=[0,0,1], angle=q1)))
    
    # Geometría Link 1 (Cilindro vertical o caja)
    # Va desde z=0 hasta z=LINK_1_HEIGHT
    rr.log("world/link1/geom", rr.Transform3D(translation=[0, 0, LINK_1_HEIGHT/2]))
    rr.log("world/link1/geom", rr.Boxes3D(half_sizes=[0.1, 0.1, LINK_1_HEIGHT/2], colors=[[255, 100, 0]]))
    
    # --- Joint 2 (Hombro) ---
    # Ubicado en [0, 0, LINK_1_HEIGHT] respecto al frame anterior
    # Rota en Y.
    rr.log("world/link1/link2", rr.Transform3D(
        translation=[0, 0, LINK_1_HEIGHT],
        rotation=rr.RotationAxisAngle(axis=[0,1,0], angle=q2)
    ))
    
    # Geometría Link 2 (Brazo superior)
    # Se extiende en Z (o X, depende de convención). Usaremos X local para el brazo.
    # Si rota en Y, el brazo se mueve en el plano XZ local.
    # Vamos a definir que el brazo en reposo (q2=0) apunta hacia arriba (Z) o hacia el frente (X)?
    # Convención común: En reposo apunta hacia arriba (Z) o X.
    # Vamos a hacer que apunte hacia Z local para simplificar la visualización vertical,
    # PERO para manipuladores seriales suele ser X el eje del link.
    # Usemos X: El link se extiende a lo largo del eje X local.
    
    rr.log("world/link1/link2/geom", rr.Transform3D(translation=[LINK_2_LENGTH/2, 0, 0]))
    rr.log("world/link1/link2/geom", rr.Boxes3D(half_sizes=[LINK_2_LENGTH/2, 0.08, 0.08], colors=[[0, 200, 255]]))
    
    # --- Joint 3 (Codo) ---
    # Ubicado en [LINK_2_LENGTH, 0, 0]
    # Rota en Y.
    rr.log("world/link1/link2/link3", rr.Transform3D(
        translation=[LINK_2_LENGTH, 0, 0],
        rotation=rr.RotationAxisAngle(axis=[0,1,0], angle=q3)
    ))
    
    # Geometría Link 3 (Antebrazo)
    rr.log("world/link1/link2/link3/geom", rr.Transform3D(translation=[LINK_3_LENGTH/2, 0, 0]))
    rr.log("world/link1/link2/link3/geom", rr.Boxes3D(half_sizes=[LINK_3_LENGTH/2, 0.06, 0.06], colors=[[100, 255, 100]]))
    
    # Efector final
    rr.log("world/link1/link2/link3/end_effector", rr.Transform3D(translation=[LINK_3_LENGTH, 0, 0]))
    rr.log("world/link1/link2/link3/end_effector", rr.Points3D(positions=[[0,0,0]], radii=0.05, colors=[[255, 255, 255]]))

def main():
    rr.init("manipulator_tutorial_06", spawn=True)
    
    # Estado inicial (Home)
    log_robot(0, 0, 0)
    
    print("Paso 6 completado: Definición del robot 3DOF.")

if __name__ == "__main__":
    main()
