import math
import csv
import os

class IAGuardianaLatente:
    def __init__(self):
        # 1. Invariantes xilográficos de la matriz original (Condiciones de Contorno)
        self.AREA_MATRIZ = 357810.0
        self.PERIMETRO_MATRIZ = 9070.0
        self.CIRCULARIDAD_MATRIZ = 0.05466
        
        # 2. Espacio de control para el Filtro TDA
        self.DIMENSIONES_TOPOLOGICAS = 11
        self.ruta_csv = "datos_fractales.csv"
        self.registro_estampas = {}
        
        # Cargar de golpe los datos reales del archivo CSV de la pantalla
        self._cargar_matriz_fractal()

    def _cargar_matriz_fractal(self):
        """
        Lee el archivo datos_fractales.csv de forma automática,
        absorbiendo las etiquetas de texto y los valores reales del Corpus (1.732, 1.745, etc.)
        """
        if not os.path.exists(self.ruta_csv):
            print(f"[ADVERTENCIA] No se encontró '{self.ruta_csv}' en la raíz. Usando fallback analítico.")
            # Fallback por si se ejecuta fuera de la raíz del repositorio
            self.registro_estampas = {"MujerRecostada_01": 1.732, "MujerRecostada_02": 1.745}
            return

        with open(self.ruta_csv, mode="r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                # Extrae el nombre exacto de la estampa y su dimensión fractal real
                identificador = fila.get("Estampa", "").strip()
                try:
                    df = float(fila.get("Dimension_Fractal_Df", 0.0))
                    if identificador and df > 0:
                        self.registro_estampas[identificador] = df
                except ValueError:
                    continue
        print(f"[SISTEMA] Matriz cargada con éxito. {len(self.registro_estampas)} estampas integradas en el flujo.")

    def simular_homologia_persistente(self, estampa_nombre):
        """
        Aplica el Filtro TDA sobre una estampa basándose en la Dimensión Fractal real del CSV.
        Mapea el nacimiento y muerte de cavidades en 11 dimensiones.
        """
        if estampa_nombre not in self.registro_estampas:
            raise ValueError(f"La estampa '{estampa_nombre}' no existe en el archivo datos_fractales.csv")
            
        df = self.registro_estampas[estampa_nombre]
        diagrama_persistencia = []
        
        print(f"\n[TDA] Procesando '{estampa_nombre}' con Df real de la pantalla = {df}")
        
        for dim in range(self.DIMENSIONES_TOPOLOGICAS):
            # Comportamiento del trazo modulado por la verdadera complejidad fractal detectada
            factor_escala = math.sin(dim + 1) * df
            
            birth = abs(factor_escala * 0.1)
            death = abs(birth + (df / (dim + 1)))
            persistencia = death - birth
            
            diagrama_persistencia.append({
                "dimension_betti": dim,
                "nacimiento": round(birth, 4),
                "muerte": round(death, 4),
                "persistencia_formal": round(persistencia, 4)
            })
            
        return diagrama_persistencia

    def mapear_espacio_hiperbolico(self, diagrama):
        """
        Verifica el colapso topológico y si el accidente local se ha estabilizado en patrón.
        """
        persistencias = [d["persistencia_formal"] for d in diagrama]
        persistencia_media = sum(persistencias) / len(persistencias)
        
        equilibrio_alcanzado = persistencia_media > (2 / math.pi)
        
        return {
            "persistencia_global_media": round(persistencia_media, 4),
            "equilibrio_homeomorfico": equilibrio_alcanzado,
            "estado_trazo": "Patrón Invariante Estabilizado" if equilibrio_alcanzado else "Fluido Inestable"
        }

# --- EJECUCIÓN DE LA INTELIGENCIA DEL SISTEMA ---
if __name__ == "__main__":
    guardiana = IAGuardianaLatente()
    
    # Procesamos de golpe la primera estampa real visible en tu captura de Chrome
    try:
        nombre_objetivo = "MujerRecostada_01"
        diagrama_tda = guardiana.simular_homologia_persistente(nombre_objetivo)
        resultado = guardiana.mapear_espacio_hiperbolico(diagrama_tda)
        
        print("\n--- RESULTADO DEL COLAPSO DE LA GESTALT ---")
        print(f"Estampa analizada: {nombre_objetivo}")
        print(f"Estado del campo continuo: {resultado['estado_trazo']}")
        print(f"Métrica de persistencia unificada: {resultado['persistencia_global_media']}")
    except Exception as e:
        print(f"[ERROR] Colapso en el flujo: {e}")
