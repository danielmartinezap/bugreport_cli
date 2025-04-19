# bugreport/db.py
import sqlite3
from pathlib import Path

class BaselineDB:
    def __init__(self):
        self.db_path = "baselines.db"
        self._init_db()
    
    def _init_db(self):
        Path("baselines").mkdir(exist_ok=True)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS baselines (
                    name TEXT PRIMARY KEY,
                    path TEXT NOT NULL
                )
            """)
    
    def add_baseline(self, name: str, image_path: str):
        """Guarda una nueva imagen de referencia"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO baselines VALUES (?, ?)",
                (name, str(Path(image_path).absolute()))
            )
    
    def get_baseline(self, name: str) -> str:
        """Obtiene la ruta de un baseline por nombre"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "SELECT path FROM baselines WHERE name = ?", 
                (name,)
            )
            result = cursor.fetchone()
            return result[0] if result else None