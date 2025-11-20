import rerun as rr
import numpy as np
import time

def main():
    rr.init("04_time_sequence", spawn=True)

    # Simular 50 pasos de tiempo
    for t in range(50):
        # set_time_sequence asocia los datos siguientes con un instante de tiempo
        # Esto crea la barra de tiempo en la parte inferior del visor
        rr.set_time_sequence("step", t)
        
        # Posición que se mueve en círculo
        x = np.cos(t * 0.1) * 5
        y = np.sin(t * 0.1) * 5
        
        rr.log("objeto_movil", rr.Points3D([[x, y, 0]], radii=0.2, colors=[255, 255, 0]))
        
        # Pequeña pausa para simular tiempo real (opcional, Rerun guarda todo)
        # time.sleep(0.05)

if __name__ == "__main__":
    main()
