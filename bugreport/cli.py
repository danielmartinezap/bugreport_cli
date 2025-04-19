import typer
from bugreport.analyzer import compare_with_baseline
from bugreport.report import BugReport
from bugreport.db import BaselineDB

app = typer.Typer()

# Asegúrate de que estos objetos mantengan estado entre comandos
report = BugReport()
db = BaselineDB()

@app.command()
def set_baseline(
    image_path: str = typer.Argument(..., help="Ruta a la imagen de referencia"),
    name: str = typer.Argument(..., help="Nombre identificador del baseline")
):
    """Registra una imagen como referencia"""
    db.add_baseline(name, image_path)
    typer.echo(f"✅ Baseline '{name}' guardado")

@app.command()
def test(image_path: str, baseline_name: str):
    """Compara una imagen con su baseline"""
    baseline_path = db.get_baseline(baseline_name)
    
    if not baseline_path:
        typer.echo(f"❌ Baseline '{baseline_name}' no encontrado")
        raise typer.Exit(1)
    
    result = compare_with_baseline(baseline_path, image_path)
    
    if result["diff_found"]:
        report.add_bug(
            image_path,
            result["classification"],
            result.get("diff_area", "Área no especificada"),
            result["diff_path"]
        )
        typer.echo(f"🐞 Bug detectado: {result['classification']}")
    else:
        typer.echo("✅ No se encontraron diferencias")

@app.command()
def generate_report(output_path: str = "bugreport_output.html"):
    """Exporta reporte con bugs clasificados"""
    try:
        report_path = report.export_html(output_path)
        typer.echo(f"📊 Reporte generado en: {report_path}")
    except Exception as e:
        typer.echo(f"❌ Error al generar reporte: {str(e)}", err=True)
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
