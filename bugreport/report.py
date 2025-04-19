import json
import os
from datetime import datetime

class BugReport:
    def __init__(self, store_path="bugs.json"):
        self.store_path = store_path
        self.bugs = self._load_bugs()

    def _load_bugs(self):
        if os.path.exists(self.store_path):
            with open(self.store_path, "r") as f:
                return json.load(f)
        return []

    def _save_bugs(self):
        with open(self.store_path, "w") as f:
            json.dump(self.bugs, f, indent=4)

    def add_bug(self, image_path, classification, affected_area, diff_image_path):
        bug_entry = {
            "timestamp": datetime.now().isoformat(),
            "image_tested": image_path,
            "classification": classification,
            "affected_area": affected_area,
            "diff_image": diff_image_path
        }
        self.bugs.append(bug_entry)
        self._save_bugs()

    def export_html(self, output_path="bugreport_output.html"):
        if not self.bugs:
            raise ValueError("No hay bugs registrados para generar reporte")

        html = """
        <html><head><title>Reporte de Bugs</title></head><body>
        <h1>Reporte de Bugs Visuales</h1>
        <ul>
        """
        for bug in self.bugs:
            html += f"""
            <li>
                <strong>Fecha:</strong> {bug['timestamp']}<br/>
                <strong>Imagen evaluada:</strong> {bug['image_tested']}<br/>
                <strong>Tipo:</strong> {bug['classification']}<br/>
                <strong>Área afectada:</strong> {bug['affected_area']}<br/>
                <strong>Diferencia visual:</strong><br/>
                <img src="{bug['diff_image']}" width="400"/>
            </li><br/>
            """

        html += "</ul></body></html>"

        with open(output_path, "w") as f:
            f.write(html)

        return output_path
