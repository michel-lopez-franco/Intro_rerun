import rerun as rr

def main():
    rr.init("08_text_logs", spawn=True)

    # Rerun puede capturar logs de texto
    # Esto es muy útil para debuggear y ver eventos en la línea de tiempo
    rr.log("logs/info", rr.TextLog("Iniciando la aplicación...", level="INFO"))
    
    for i in range(5):
        rr.set_time_sequence("paso", i)
        if i % 2 == 0:
            rr.log("logs/proceso", rr.TextLog(f"Procesando paso par {i}", level="DEBUG"))
        else:
            rr.log("logs/proceso", rr.TextLog(f"Procesando paso impar {i}", level="WARN"))

    rr.log("logs/error", rr.TextLog("¡Simulación de un error fatal!", level="CRITICAL"))

if __name__ == "__main__":
    main()
