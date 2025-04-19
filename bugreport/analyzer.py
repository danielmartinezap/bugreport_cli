import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from openai import OpenAI
import base64
from pathlib import Path
from typing import Dict, Union
import json
from pathlib import Path

class ImageComparator:
    @staticmethod
    def compare_images(baseline_path: str, test_path: str) -> Dict[str, Union[float, str, bool]]:
        """
        Compara dos imágenes usando SSIM y detección de contornos.
        
        Args:
            baseline_path: Ruta de la imagen de referencia
            test_path: Ruta de la imagen a comparar
            
        Returns:
            Dict con:
            - similarity: Puntuación SSIM (0-1)
            - diff_path: Ruta de la imagen de diferencias
            - diff_found: True si se encontraron diferencias significativas
        """
        # Cargar imágenes
        baseline = cv2.imread(baseline_path)
        test = cv2.imread(test_path)
        
        if baseline is None or test is None:
            raise ValueError("No se pudieron cargar una o ambas imágenes")

        # Redimensionar si son diferentes tamaños
        if baseline.shape != test.shape:
            test = cv2.resize(test, (baseline.shape[1], baseline.shape[0]))

        # Convertir a escala de grises
        gray_a = cv2.cvtColor(baseline, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(test, cv2.COLOR_BGR2GRAY)

        # Calcular SSIM
        score, diff = ssim(gray_a, gray_b, full=True)
        diff = (diff * 255).astype("uint8")

        # Umbralización y detección de contornos
        _, thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Guardar diferencias
        diff_path = "diff_visual.png"
        output = np.hstack([baseline, test])
        cv2.drawContours(output, contours, -1, (0, 0, 255), 2)
        cv2.imwrite(diff_path, output)

        return {
            "similarity": float(score),
            "diff_path": diff_path,
            "diff_found": len(contours) > 5 or score < 0.90  # Ajustar umbrales
        }

class AIClassifier:
    def __init__(self):
        self.client = OpenAI()

    def classify_bug(self, baseline_path: str, test_path: str, diff_path: str) -> str:
        """
        Clasifica diferencias usando OpenAI GPT-4 Vision.
        
        Args:
            baseline_path: Ruta de la imagen base
            test_path: Ruta de la imagen de prueba
            diff_path: Ruta de la imagen de diferencias
            
        Returns:
            Descripción del bug clasificada por IA
        """
        def encode_image(image_path: str) -> Dict:
            with open(image_path, "rb") as img_file:
                return {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64.b64encode(img_file.read()).decode('utf-8')}"
                    }
                }

        messages = [
            {
                "role": "system",
                "content": "Eres un experto en QA. Analiza estas imágenes y clasifica los bugs visuales."
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "**Imagen de Referencia (Baseline):**"},
                    encode_image(baseline_path),
                    {"type": "text", "text": "**Imagen de Prueba:**"},
                    encode_image(test_path),
                    {"type": "text", "text": "**Diferencias Detectadas:**"},
                    encode_image(diff_path),
                    {"type": "text", "text": "Clasifica los bugs encontrados usando este formato:"},
                    {"type": "text", "text": "1. Tipo de Bug (Layout/Color/Contenido)"},
                    {"type": "text", "text": "2. Elementos afectados"},
                    {"type": "text", "text": "3. Severidad (1-5)"}
                ]
            }
        ]

        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            max_tokens=1000
        )
        return response.choices[0].message.content

def compare_with_baseline(baseline_path: str, test_path: str) -> Dict:
    """
    Función principal que coordina la comparación y clasificación.
    
    Args:
        baseline_path: Ruta de la imagen base
        test_path: Ruta de la imagen a testear
        
    Returns:
        Dict con resultados de la comparación
    """
    comparator = ImageComparator()
    classifier = AIClassifier()
    
    # 1. Comparación técnica
    diff_data = comparator.compare_images(baseline_path, test_path)
    
    # 2. Clasificación con IA si hay diferencias
    if diff_data["diff_found"]:
        try:
            diff_data["classification"] = classifier.classify_bug(
                baseline_path, 
                test_path,
                diff_data["diff_path"]
            )
        except Exception as e:
            diff_data["classification"] = f"Error en clasificación: {str(e)}"
    
    return diff_data

def save_result(result, path="results.json"):
    with open(path, "w") as f:
        json.dump(result, f, indent=4)