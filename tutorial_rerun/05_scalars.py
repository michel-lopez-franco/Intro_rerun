import rerun as rr
import math

def main():
    rr.init("05_scalars", spawn=True)

    for t in range(100):
        rr.set_time_sequence("step", t)
        
        # Valor sinusoidal
        value = math.sin(t * 0.1)
        
        # Loguear un escalar. Esto crea un gráfico de líneas en el visor.
        # Útil para métricas de error, velocidad, temperatura, etc.
        rr.log("sensores/sinusoide", rr.Scalars(value))

if __name__ == "__main__":
    main()
