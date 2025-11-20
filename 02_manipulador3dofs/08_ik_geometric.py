import rerun as rr
import numpy as np
import time

# --- Parámetros ---
L1 = 0.5 # Altura base
L2 = 1.0 # Brazo
L3 = 1.0 # Antebrazo

def log_robot(q1, q2, q3):
    # (Mismo código de visualización, simplificado para brevedad en este archivo si fuera necesario, 
    # pero lo repetiremos para que sea ejecutable standalone)
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
    """
    Calcula q1, q2, q3 para alcanzar la posición (x, y, z).
    Retorna (q1, q2, q3) o None si no es alcanzable.
    """
    # 1. q1: Rotación de la cintura (plano XY)
    q1 = np.arctan2(y, x)
    
    # 2. Problema planar (r, z_local)
    # r es la distancia horizontal desde el eje Z hasta el punto
    r = np.sqrt(x**2 + y**2)
    # z_local es la altura respecto al hombro
    z_local = z - L1
    
    # Distancia desde el hombro al efector final en el plano
    d = np.sqrt(r**2 + z_local**2)
    
    # Verificamos alcance
    if d > (L2 + L3) or d < abs(L2 - L3):
        print(f"Objetivo fuera de alcance: {d}")
        return None
    
    # 3. Ley de cosenos para el codo (q3)
    # d^2 = L2^2 + L3^2 - 2*L2*L3*cos(pi - q3)
    # cos(q3_angle_inside) = (L2^2 + L3^2 - d^2) / (2*L2*L3)
    # q3 es el ángulo relativo.
    # Usaremos la convención geométrica:
    # alpha = angulo opuesto a d (no nos sirve directo)
    # beta = angulo opuesto a L3 (parte de q2)
    # gamma = angulo opuesto a L2 (parte de q3)
    
    # cos_q3 = (r^2 + z_local^2 - L2^2 - L3^2) / (2 * L2 * L3)
    cos_q3 = (d**2 - L2**2 - L3**2) / (2 * L2 * L3)
    
    # Clamp por errores numéricos
    cos_q3 = np.clip(cos_q3, -1.0, 1.0)
    
    # q3 geométrico (ángulo interno del triángulo? No, q3 es la desviación de la línea recta)
    # Si q3=0, el brazo está estirado.
    # En nuestra definición, si q3=0, el link3 sigue al link2.
    # Entonces la distancia sería L2+L3.
    # La fórmula de ley de cosenos da el ángulo interno opuesto al lado d.
    # Espera, ley de cosenos c^2 = a^2 + b^2 - 2ab cos(C).
    # Aquí d^2 = L2^2 + L3^2 - 2*L2*L3*cos(180 - q3)
    # d^2 = L2^2 + L3^2 + 2*L2*L3*cos(q3)
    # cos(q3) = (d^2 - L2^2 - L3^2) / (2*L2*L3)
    
    q3 = -np.arccos(cos_q3) # Codo abajo/arriba. Probemos negativo para configuración típica "codo arriba" si z es positivo?
    # Depende de la configuración deseada (codo arriba o codo abajo).
    
    # 4. q2 (Hombro)
    # q2 = atan2(z_local, r) - atan2(L3*sin(q3), L2 + L3*cos(q3))
    # Ángulo de elevación del vector destino
    alpha = np.arctan2(z_local, r)
    # Ángulo interno debido a la flexión del codo
    # beta = atan2(L3 sin(q3), L2 + L3 cos(q3))
    # Nota: q3 es negativo en nuestra elección anterior, verifiquemos signos.
    beta = np.arctan2(L3 * np.sin(q3), L2 + L3 * np.cos(q3))
    
    q2 = - (alpha - beta) # Ajuste de signo según convención de rotación Y
    # En Rerun, rotación positiva en Y (regla mano derecha) baja el brazo si X es forward?
    # X forward, Y up (no, Y es eje rotación). Z up.
    # Si eje rotación es Y [0,1,0]. X es forward [1,0,0]. Z es up [0,0,1].
    # Rotar positivo en Y mueve X hacia Z negativo (regla mano derecha: pulgar en Y, dedos de X a Z... no, de Z a X).
    # X cross Y = Z.
    # Rotación +Y: Z -> X. X -> -Z.
    # Entonces rotación positiva baja el brazo.
    # alpha es positivo si z_local > 0 (hacia arriba).
    # Queremos rotar "hacia arriba", que es rotación negativa en Y.
    # Entonces q2 debería ser -(alpha - beta).
    
    return q1, q2, q3

def main():
    rr.init("manipulator_tutorial_08", spawn=True)
    
    # Objetivo a alcanzar
    target_point = [1.2, 0.5, 0.8]
    
    rr.log("world/target", rr.Points3D(positions=[target_point], colors=[[255, 0, 0]], radii=0.1, labels=["Target"]))
    
    result = inverse_kinematics(target_point[0], target_point[1], target_point[2])
    
    if result:
        q1, q2, q3 = result
        print(f"Solución IK encontrada: q1={np.rad2deg(q1):.2f}, q2={np.rad2deg(q2):.2f}, q3={np.rad2deg(q3):.2f}")
        log_robot(q1, q2, q3)
    else:
        print("No se encontró solución.")

    print("Paso 8 completado: Cinemática Inversa Geométrica.")

if __name__ == "__main__":
    main()
