import rerun as rr
import numpy as np

def main():
    # 1. Inicializar Rerun
    # 'spawn=True' hace que se abra la ventana del visualizador automáticamente
    rr.init("mi_primera_demo_rerun", spawn=True)

    print("Generando datos y enviándolos a Rerun...")

    # 2. Configuración inicial
    num_points = 100
    # Puntos iniciales aleatorios centrados en 0
    positions = np.random.normal(size=(num_points, 3))
    # Colores aleatorios RGB
    colors = np.random.uniform(0, 255, size=(num_points, 3)).astype(np.uint8)

    # 3. Bucle de simulación
    # Simulamos 60 frames de movimiento
    for i in range(60):
        # Establecemos el tiempo actual. Esto es CRÍTICO para la animación.
        # 'frame_idx' es el nombre de nuestra línea de tiempo.
        rr.set_time_sequence("frame_idx", i)
        
        # Actualizamos las posiciones (movimiento browniano simple)
        positions += np.random.normal(scale=0.05, size=positions.shape)
        
        # Logueamos los puntos 3D
        # La ruta "world/points" organiza estos datos en el visualizador
        rr.log(
            "world/points", 
            rr.Points3D(positions, colors=colors, radii=0.1)
        )
        
        # También podemos loguear un escalar para ver gráficos 2D
        avg_distance = np.mean(np.linalg.norm(positions, axis=1))
        rr.log("metrics/avg_distance", rr.Scalar(avg_distance))

    print("¡Terminado! El visualizador debería estar abierto.")

if __name__ == "__main__":
    main()
