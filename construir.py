"""Actualiza el HTML autónomo a partir de app.js y styles.css, sin dependencias."""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
target = root / 'index.html'
html = target.read_text(encoding='utf-8')
html = re.sub(r'<style>.*?</style>', lambda _: '<style>\n' + (root / 'styles.css').read_text(encoding='utf-8') + '\n</style>', html, count=1, flags=re.S)
html = re.sub(r'<script>.*?</script>', lambda _: '<script>\n' + (root / 'app.js').read_text(encoding='utf-8') + '\n</script>', html, count=1, flags=re.S)
if 'id="session-label"' not in html:
    html = html.replace('<button id="logout"', '<span id="session-label" class="session-badge"></span>\n    <button id="logout"')
if 'id="theme-init"' not in html:
    bootstrap = """<script id="theme-init">
(function(){var theme;try{theme=localStorage.getItem('capaz-tema');}catch(e){}document.documentElement.dataset.theme=theme==='dark'||theme==='light'?theme:window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';})();
</script>"""
    html = html.replace('</head>', bootstrap + '\n</head>')
if 'id="theme-toggle"' not in html:
    toolbar = '<div class="appearance-toolbar"><button type="button" id="theme-toggle" class="theme-toggle" aria-label="Activar modo oscuro"><span id="theme-icon" aria-hidden="true">☾</span><span id="theme-label">Modo oscuro</span></button></div>'
    html = html.replace('<body>', '<body>\n' + toolbar)
target.write_text(html, encoding='utf-8')
print('index.html actualizado con el JavaScript y CSS actuales.')
