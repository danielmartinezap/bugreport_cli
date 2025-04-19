# VisualGuard QA 🛡️🔍  
**AI-Powered Visual Testing Tool · Catch UI bugs before your users do**

## 🚀 Overview  
VisualGuard QA is a CLI tool that combines Computer Vision + AI to detect and classify visual bugs in web interfaces. It compares screenshots against a reference baseline and generates detailed reports with:

- Visual differences (pixels, layout, colors)  
- Semantic bug classification using AI (e.g., “Button is invisible due to poor contrast”)  
- HTML/PDF reports  
- Ideal for QA automation, developers, and designers who need automated, human-readable visual testing.

# 🌟 Features  
- ✅ **Accurate Detection**: Uses OpenCV + SSIM to compare images  
- 🤖 **AI-Powered Classification**: GPT-4 Vision analyzes bug context  
- 📊 **Automated Reports**: Generates HTML reports with severity-based bug sorting  
- 🔧 **100% Local**: Keeps your images private—no cloud upload  
- 🐍 **Python-Based**: Easy to integrate into CI/CD pipelines

# 📦 Installation  
Clone the repository:

```bash
git clone https://github.com/danielmartinezap/VisualGuard-QA.git
cd VisualGuard-QA
```

Install dependencies:

```bash
pip install -r requirements.txt
# (Optional) Set your OpenAI API key for AI classification
export OPENAI_API_KEY="your-key-here"
```

# 🛠 Usage

### 1. Set Baseline  
Save a reference image:

```bash
python -m visualguard set-baseline baseline.png home_page
```

### 2. Run Tests  
Compare a new screenshot against the baseline:

```bash
python -m visualguard test new_page.png home_page
```

### 3. Generate Report  
Create an HTML report with detected bugs:

```bash
python -m visualguard generate-report
```

# 📄 Sample Output

🐞 **Bug Report** - Apr 15, 2025  
```markdown
--------------------------------  
🟠 **Bug #1**: Contrast Error  
   - Element: "Login Button"  
   - Severity: High (WCAG Fail)  
   - Diff: [screenshot_diff.png]  

🔵 **Bug #2**: Layout Shift  
   - Element: Navigation Bar  
   - Severity: Medium  
   - Expected: 150px padding (Actual: 90px)  
```

# 🤖 How the AI Works  

The AI module:  
- Detects visual differences using OpenCV  
- Sends affected regions to GPT-4 Vision for semantic classification  
- Suggests fixes (e.g., “Increase text contrast to 4.5:1”)

# 🛡️ Why Choose VisualGuard QA?

| Feature           | VisualGuard QA | Percy   | Applitools |
|------------------|----------------|---------|------------|
| Privacy          | ✅ Local       | ❌ Cloud| ❌ Cloud   |
| Cost             | Free           | $$$     | $$$$       |
| Customization    | Full           | Limited | Limited    |
| Contextual AI    | ✅ GPT-4       | ❌      | 🟡 Basic   |

## 📈 Roadmap  
- GitHub Actions integration  
- PDF/Excel report support

# 🤝 Contributing  
PRs are welcome!  
Follow these steps:

1. Fork the repo  
2. Create a new branch: `git checkout -b feature/new-algorithm`  
3. Commit your changes: `git commit -m "Add magic"`  
4. Push your branch: `git push origin feature/new-algorithm`

# 📜 License  
MIT © Daniel Martínez

## 🛡️ Questions? Open an issue  

✨ *Catch visual bugs before they catch your users!* ✨

## 🔗 Useful Links  
Built with Python 🐍, OpenCV 👁️, and GPT-4 🧠.  

Want a custom logo or live demo? Open an issue! 🎨  

_(This README was crafted with ❤️ by the VisualGuard QA team a.k.a. Daniel Martínez.)_

# Thanks for using VisualGuard QA! 🎉

---------------------------------------------------------------------------------------------

# VisualGuard QA 🛡️🔍
AI-Powered Visual Testing Tool · Catch UI bugs before your users do

## 🚀 Overview
VisualGuard QA es una herramienta CLI que combina Computer Vision + IA para detectar y clasificar bugs visuales en interfaces web. Compara screenshots contra una base de referencia (baseline) y genera reportes detallados con:

- Diferencias visuales (píxeles, layout, colores).

- Clasificación semántica de bugs usando IA (ej: "Botón invisible por contraste").

- Reportes en HTML/PDF.

- Ideal para QA Automation, desarrolladores y diseñadores que necesitan testing visual automatizado y comprensible.

# 🌟 Features
- ✅ Detección precisa: Usa OpenCV + SSIM para comparar imágenes.
- 🤖 Clasificación con IA: GPT-4 Vision analiza el contexto de los bugs.
- 📊 Reportes automáticos: Genera HTML con bugs clasificados por severidad.
- 🔧 100% local: No sube tus imágenes a la nube (ideal para proyectos privados).
- 🐍 Python-based: Fácil de integrar en pipelines CI/CD.

# 📦 Installation
- Clona el repositorio:

```bash
git clone https://github.com/danielmartinezap/VisualGuard-QA.git
cd VisualGuard-QA
```
- Instala dependencias:

```bash
pip install -r requirements.txt
Configura tu API key de OpenAI (opcional, para IA):
export OPENAI_API_KEY="tu-key-aqui"
```


# 🛠 Usage
### 1. Set Baseline
Guarda una imagen de referencia:

```bash
python -m visualguard set-baseline baseline.png home_page
```

### 2. Run Tests
Compara una nueva imagen contra el baseline:


```bash
python -m visualguard test new_page.png home_page
```
### 3. Generate Report
Crea un reporte HTML con los bugs detectados:


```bash
python -m visualguard generate-report
```

# 📄 Sample Output

🐞 **Bug Report** - 15/Abr/2025  
```markdown
--------------------------------  
🟠 **Bug #1**: Contrast Error  
   - Element: "Login Button"  
   - Severity: High (WCAG Fail)  
   - Diff: [screenshot_diff.png]  

🔵 **Bug #2**: Layout Shift  
   - Element: Navigation Bar  
   - Severity: Medium  
   - Expected: 150px padding (Actual: 90px)  
```


# 🤖 How the AI Works

El módulo de IA:

- Detecta diferencias con OpenCV.

- Envía regiones con bugs a GPT-4 Vision para clasificación semántica.

- Sugiere fixes (ej: "Aumentar contraste del texto a 4.5:1").

# 🛡️ Why Choose VisualGuard QA?

- Feature	VisualGuard QA	Percy	Applitools
- Privacidad	✅ Local	❌ Cloud	❌ Cloud
- Costo	Gratis	$$$	$$$$
- Custom	Total	Limitado	Limitado
- IA Contextual	✅ GPT-4	❌	🟡 Básico
- 📈 Roadmap
- Integración con GitHub Actions.
- Soporte para PDF/Excel reports.

# 🤝 Contributing
¡PRs son bienvenidos! Sigue estos pasos:

Haz fork del repo.

Crea una rama: git checkout -b feature/new-algorithm.

Haz commit: git commit -m "Add magic".

Push: git push origin feature/new-algorithm.

# 📜 License

MIT © Daniel Martínez

## 🛡️ ¿Preguntas? Abre un issue

✨ "Catch visual bugs before they catch your users!" ✨

## 🔗 Links Útiles

Hecho con Python 🐍, OpenCV 👁️ y GPT-4 🧠.

¿Quieres un logo personalizado o una demo en vivo? ¡Abre un issue! 🎨

(Este README fue generado con ❤️ por el equipo de VisualGuard QA aka Daniel Martinez).


# ¡Gracias por usar VisualGuard QA! 🎉

