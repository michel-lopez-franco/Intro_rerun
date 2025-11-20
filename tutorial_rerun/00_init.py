import rerun as rr

def main():
    # 0. Inicialización básica
    # spawn=True abre el visor inmediatamente.
    rr.init("00_init", spawn=True)
    
    print("Rerun inicializado. Revisa la ventana emergente.")

if __name__ == "__main__":
    main()
