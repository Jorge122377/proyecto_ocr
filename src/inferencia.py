import argparse
import os
from ocr_pipeline import ejecutar_ocr

def procesar_entrada():
    # Configuración de argumentos de consola 
    parser = argparse.ArgumentParser(description="Sistema de Inferencia OCR - Maestría TIC")
    parser.add_argument("--imagen", required=True, help="Ruta de la imagen o carpeta de imágenes")
    args = parser.parse_args()

    ruta = args.imagen

    # Lógica para manejar carpetas o imágenes individuales [cite: 43]
    if os.path.isfile(ruta):
        realizar_ocr_y_mostrar(ruta)
    elif os.path.isdir(ruta):
        print(f"--- Procesando carpeta: {ruta} ---")
        for archivo in os.listdir(ruta):
            if archivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                ruta_completa = os.path.join(ruta, archivo)
                realizar_ocr_y_mostrar(ruta_completa)
    else:
        print(f"Error: La ruta '{ruta}' no es válida.")

def realizar_ocr_y_mostrar(ruta_archivo):
    """Ejecuta el OCR y muestra el resultado [cite: 44, 45]"""
    print(f"\n[Archivo]: {os.path.basename(ruta_archivo)}")
    resultado = ejecutar_ocr(ruta_archivo)
    
    print("-" * 30)
    print(resultado if resultado else "No se detectó texto.")
    print("-" * 30)

if __name__ == "__main__":
    procesar_entrada()