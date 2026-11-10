# Prime Boxing — versión mejorada

Abre index.html o sirve esta carpeta con `python3 -m http.server 8000`.
No requiere instalación ni compilación para publicarse: sube los HTML y assets al hosting.

## Cambios
- Logo original de El Penthouse del Boxeo en Inicio y Penthouse.
- Entradas escalonadas y animación de bloques al entrar en pantalla, una sola vez.
- Interacciones suaves en botones, tarjetas, fotografías, menú móvil y diálogos.
- Navegación con transición entre páginas cuando el navegador la admite.
- Preferencia de movimiento reducido respetada, incluso si cambia con la página abierta.
- Menú que se cierra al elegir un enlace y mejoras de ajuste a pantallas de 320 px.
- Sin nuevas dependencias; animaciones con CSS y APIs nativas.

El contenido permanece visible sin animaciones ni JavaScript. Las transiciones de documentos tienen una navegación convencional como alternativa.

Los datos comerciales siguen en assets/js/config.js. Se conservaron los enlaces de boletos y redes existentes. Los videos y el registro requieren sus URLs/endpoints reales para activarse.

build.py es el generador original y ahora incluye el logo. Regenera los HTML completos, por lo que puede reemplazar otros ajustes manuales anteriores del sitio; no es necesario ejecutarlo para publicar esta versión.

## Comprobación de navegador
Con Playwright disponible en Node y Chromium instalado en /usr/bin/chromium, inicia el servidor en la raíz del sitio y ejecuta `node tests/browser.cjs`. Comprueba seis páginas a cuatro tamaños, imágenes locales, menú, diálogo de video y movimiento reducido.
