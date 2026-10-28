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
target.write_text(html, encoding='utf-8')
print('index.html actualizado con el JavaScript y CSS actuales.')
