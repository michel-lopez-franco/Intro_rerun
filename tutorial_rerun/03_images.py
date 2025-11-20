import rerun as rr
import numpy as np

def main():
    rr.init("03_images", spawn=True)

    # Crear una imagen de ruido aleatorio 200x200 con 3 canales (RGB)
    image_data = np.random.uniform(0, 255, size=(200, 200, 3)).astype(np.uint8)

    # Loguear la imagen
    # Rerun detecta automáticamente si es RGB, RGBA, o escala de grises según la forma
    rr.log("sensores/camara", rr.Image(image_data))

if __name__ == "__main__":
    main()
