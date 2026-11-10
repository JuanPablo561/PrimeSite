#!/usr/bin/env python3
"""
Genera las páginas estáticas de Prime Boxing Promotions.
Uso:  python3 build.py
Edita aquí el contenido/estructura compartida (cabecera, pie, textos) y vuelve a ejecutar.
Los datos reales (fecha, boletos, redes) van en assets/js/config.js, no aquí.
"""
from pathlib import Path

ROOT = Path(__file__).parent
IMG = "https://images.unsplash.com"
RING = "photo-1549719386-74dfcbf7dbed"      # ring / hero
GYM = "photo-1517438322307-e67111335449"    # entrenamiento


def unsplash(photo, widths, q=80):
    return ", ".join(
        f"{IMG}/{photo}?auto=format&fit=crop&q={q}&w={w} {w}w" for w in widths
    )


def ico(name, extra=""):
    return f'<svg class="i{extra}" aria-hidden="true"><use href="#i-{name}"/></svg>'


SPRITE = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false">
  <defs>
    <symbol id="i-arrow-right" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
    <symbol id="i-arrow-down" viewBox="0 0 24 24"><path d="M12 5v14M6 13l6 6 6-6"/></symbol>
    <symbol id="i-arrow-ur" viewBox="0 0 24 24"><path d="M7 17 17 7M8 7h9v9"/></symbol>
    <symbol id="i-calendar" viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="1"/><path d="M3 10h18M8 3v4M16 3v4"/></symbol>
    <symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 21s7-6.2 7-11a7 7 0 1 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></symbol>
    <symbol id="i-play" viewBox="0 0 24 24"><path class="i-fill" d="M8 5v14l11-7z"/></symbol>
    <symbol id="i-bars" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>
    <symbol id="i-x" viewBox="0 0 24 24"><path d="m6 6 12 12M18 6 6 18"/></symbol>
    <symbol id="i-instagram" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle class="i-fill" cx="17.5" cy="6.5" r="1"/></symbol>
    <symbol id="i-facebook" viewBox="0 0 24 24"><path d="M17 3h-3a4 4 0 0 0-4 4v3H7v4h3v7h4v-7h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></symbol>
    <symbol id="i-youtube" viewBox="0 0 24 24"><rect x="2.5" y="5.5" width="19" height="13" rx="3.5"/><path class="i-fill" d="M10 9.5v5l4.5-2.5z"/></symbol>
    <symbol id="fighter" viewBox="0 0 360 340">
      <circle cx="180" cy="94" r="43"/>
      <path d="M135 133Q180 158 225 133L248 169 275 237 250 260 218 218 231 340H129L142 218 110 260 85 237 112 169Z"/>
      <ellipse cx="112" cy="182" rx="30" ry="37" transform="rotate(-25 112 182)"/>
      <ellipse cx="248" cy="182" rx="30" ry="37" transform="rotate(25 248 182)"/>
    </symbol>
  </defs>
</svg>
"""

NAV = [
    ("index.html", "Inicio"),
    ("eventos.html", "Eventos"),
    ("peleadores.html", "Peleadores"),
    ("penthouse.html", "The Penthouse"),
    ("media.html", "Media"),
    ("contacto.html", "Contacto"),
]


def header(active):
    current = ' aria-current="page"'
    links = "\n".join(
        f'        <a href="{href}"{current if href == active else ""}>{label}</a>'
        for href, label in NAV
    )
    return f"""
  <a class="skip btn" href="#main">Saltar al contenido</a>

  <header class="nav">
    <div class="wrap nav-inner">
      <a href="index.html" class="brand" aria-label="Prime Boxing Promotions, inicio">
        <img src="assets/img/logo-white.svg" width="258" height="228" alt="Prime Boxing Promotions">
      </a>

      <nav id="navigation" class="nav-links" aria-label="Navegación principal">
{links}
      </nav>

      <div class="nav-end">
        <button class="btn" type="button" data-tickets>Buy Tickets {ico("arrow-ur")}</button>
        <button id="menuButton" class="icon-btn" type="button" aria-label="Abrir menú"
                aria-expanded="false" aria-controls="navigation">{ico("bars")}</button>
      </div>
    </div>
  </header>
"""


def social_buttons():
    return "".join(
        f'<button class="icon-btn" type="button" data-social="{n}" aria-label="{n}">{ico(i)}</button>'
        for n, i in (("Instagram", "instagram"), ("Facebook", "facebook"), ("YouTube", "youtube"))
    )


def footer():
    return f"""
  <footer class="footer">
    <div class="wrap">
      <div class="footer-grid">
        <div>
          <a class="brand" href="index.html" aria-label="Prime Boxing Promotions, inicio">
            <img src="assets/img/logo-white.svg" width="258" height="228" alt="" loading="lazy">
          </a>
          <p>El Penthouse del Boxeo.<br>Monterrey, Nuevo León, México.</p>
          <div class="socials mt-3" role="group" aria-label="Redes sociales">{social_buttons()}</div>
        </div>

        <div>
          <h2>EXPLORA PRIME</h2>
          <nav class="footer-nav" aria-label="Navegación del pie">
            <a href="eventos.html">Próximos eventos</a>
            <a href="peleadores.html">Nuestros peleadores</a>
            <a href="penthouse.html">Experiencia VIP</a>
            <a href="media.html">Detrás del ring</a>
            <a href="contacto.html#club">Club Prime</a>
          </nav>
        </div>

        <div>
          <h2>PRENSA &amp; ACREDITACIONES</h2>
          <p>Monterrey, Nuevo León, México.<br>Canal oficial de contacto por anunciar.</p>
          <button class="text-link gold mt-2" type="button" data-contact>
            Prensa y patrocinios {ico("arrow-ur")}
          </button>
        </div>
      </div>

      <div class="footer-bottom">
        <span>© <span data-year>2026</span> Prime Boxing Promotions. Todos los derechos reservados.</span>
        <span>HECHO PARA SENTIRSE. HECHO EN MONTERREY.</span>
      </div>
    </div>
  </footer>
"""


def page(filename, title, desc, active, body):
    html = f"""<!DOCTYPE html>
<html lang="es-MX">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta name="theme-color" content="#0A0A0A">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="es_MX">
  <meta property="og:site_name" content="Prime Boxing Promotions">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">

  <link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/styles.css">
  <script src="assets/js/config.js" defer></script>
  <script src="assets/js/main.js" defer></script>
</head>
<body>
{SPRITE}{header(active)}
  <main id="main">
{body}
  </main>
{footer()}
  <noscript>
    <p class="wrap gold">Activa JavaScript para abrir el menú, consultar boletos y ver la cuenta regresiva.</p>
  </noscript>
</body>
</html>
"""
    (ROOT / filename).write_text(html, encoding="utf-8")
    print("✓", filename)


# ------------------------------------------------------------------ piezas reutilizables
def page_hero(eyebrow, h1, lead):
    return f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{h1}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>"""


def countdown_block(label_text="Próxima Fight Night · cuenta regresiva de demostración"):
    return f"""
          <div>
            <p class="eyebrow" data-countdown-label>{label_text}</p>
            <div class="countdown" data-countdown role="timer" aria-label="Cuenta regresiva para la próxima Fight Night">
              <div><strong data-unit="days">00</strong><span>DÍAS</span></div>
              <div><strong data-unit="hours">00</strong><span>HORAS</span></div>
              <div><strong data-unit="minutes">00</strong><span>MINUTOS</span></div>
              <div><strong data-unit="seconds">00</strong><span>SEGUNDOS</span></div>
            </div>
          </div>"""


def tiers():
    return """
            <div class="tickets" role="group" aria-label="Categorías de boletos">
              <div class="tier"><strong>GENERAL</strong><span>Venta próximamente</span></div>
              <div class="tier"><strong>PREFERENTE</strong><span>Venta próximamente</span></div>
              <div class="tier tier-vip"><strong class="gold">RINGSIDE VIP</strong><span>Venta próximamente</span></div>
            </div>"""


def poster():
    return """
          <div class="event-art">
            <div class="event-poster">
              <p class="eyebrow">Prime Boxing Promotions presenta</p>
              <p class="display mt-3">FIGHT<br>NIGHT</p>
              <p class="display vs">SALINAS <span class="gold">/ VS /</span> TBA</p>
              <p class="eyebrow">El Penthouse · Monterrey</p>
            </div>
          </div>"""


def event_card(full):
    co_main = ""
    cta = f"""
            <a class="btn btn-block mt-3" href="eventos.html">Ver cartelera completa {ico("arrow-right")}</a>"""
    if full:
        co_main = f"""
            <div class="co-main">
              <p class="eyebrow">Co-Main Event · Campeonato estatal por confirmar</p>
              <h3>ÓSCAR “EL GUERRERITO” TORRES <span class="gold">VS. TBA</span></h3>
              <p class="muted small">División y rounds por confirmar</p>
            </div>
            {tiers()}"""
        cta = f"""
            <button class="btn btn-block mt-3" type="button" data-tickets>Consultar boletos {ico("arrow-right")}</button>"""

    return f"""
        <div class="event">{poster()}
          <div class="event-info">
            <span class="badge">Main Event</span>
            <span class="badge">WBC · por confirmar</span>

            <h3>NELSON “LA ROKA” SALINAS<br><span class="gold">VS. RIVAL POR ANUNCIAR</span></h3>
            <p class="muted small">División y rounds por confirmar</p>

            <div class="event-meta">{ico("calendar")}<span data-event-date>Fecha y horario por anunciar</span></div>
            <div class="event-meta">{ico("pin")}<span>El Penthouse, Monterrey, N.L.</span></div>
            {co_main}{cta}
          </div>
        </div>"""


def fighter_card(num, nick, name, flip=False):
    style = ' style="transform:scaleX(-1)"' if flip else ""
    return f"""
          <article class="fighter">
            <div class="portrait">
              <span class="number">{num}</span>
              <svg role="img" aria-label="Silueta ilustrativa de boxeador"{style}><use href="#fighter"/></svg>
              <span class="image-note">RETRATO PRÓXIMAMENTE</span>
            </div>
            <div class="fighter-body">
              <p class="eyebrow">“{nick}”</p>
              <h3>{name}</h3>
              <p class="muted small">División por confirmar · Monterrey, N.L.</p>
              <div class="record" role="group" aria-label="Récord pendiente de confirmación">
                <span>V — / D — / KO —</span>
                <span>RÉCORD POR CONFIRMAR</span>
              </div>
            </div>
          </article>"""


def partners():
    return """
    <section class="section section-tight" aria-labelledby="partnersTitle">
      <div class="wrap">
        <p id="partnersTitle" class="eyebrow center">El boxeo nos une · Partners y transmisión</p>
        <div class="partners">
          <div class="partner">WBC<small>WORLD BOXING COUNCIL</small></div>
          <div class="partner">BOX AZTECA<small>AMÉRICA</small></div>
          <div class="partner">MONTERREY<small>ORGULLO REGIOMONTANO</small></div>
          <a class="partner" href="contacto.html#patrocinios">TU MARCA AQUÍ<small>CONVIÉRTETE EN PATROCINADOR</small></a>
        </div>
        <p class="note center mt-3">Presentación conceptual. Alianzas, avales y transmisión sujetos a confirmación.</p>
      </div>
    </section>"""


def video_cards():
    def img(w):
        return (f'<img src="{IMG}/{GYM}?auto=format&fit=crop&q=75&w={w}" alt="" '
                f'loading="lazy" decoding="async" width="{w}" height="{int(w*.66)}">')

    def reel(key, title, eyebrow, h3):
        return f"""
            <article class="video-card">
              <img src="{IMG}/{RING}?auto=format&fit=crop&q=70&w=700" alt="" loading="lazy" decoding="async" width="700" height="466">
              <button class="play" type="button" data-video="{key}" data-title="{title}" aria-label="Ver {title}">{ico("play")}</button>
              <div class="video-copy"><p class="eyebrow">{eyebrow}</p><h3>{h3}</h3></div>
            </article>"""

    return f"""
        <div class="video-grid">
          <article class="video-card">
            {img(1000)}
            <button class="play" type="button" data-video="historia"
                    data-title="Historia en el Penthouse: El Nacimiento de un Campeón"
                    aria-label="Ver Historia en el Penthouse: El Nacimiento de un Campeón">{ico("play")}</button>
            <div class="video-copy">
              <span class="badge">Documental · Próximamente</span>
              <h3>HISTORIA EN EL PENTHOUSE:<br>EL NACIMIENTO DE UN CAMPEÓN</h3>
            </div>
          </article>

          <div class="reels">{reel("highlights", "Los mejores momentos de Fight Night", "Highlights · Próximamente", "EL RING NO OLVIDA.")}
            {reel("camp", "Dentro del campamento Prime", "Training camp · Próximamente", "EL TRABAJO INVISIBLE.")}
          </div>
        </div>"""


# ------------------------------------------------------------------ INICIO
page(
    "index.html",
    "Prime Boxing Promotions | El Penthouse del Boxeo",
    "Descubre Prime Boxing Promotions. El talento de Monterrey, la intensidad del ring y la experiencia del Penthouse del Boxeo.",
    "index.html",
    f"""
    <section class="hero">
      <img class="hero-bg" alt="" fetchpriority="high" decoding="async"
           src="{IMG}/{RING}?auto=format&fit=crop&q=80&w=1400"
           srcset="{unsplash(RING, (800, 1400, 2200))}" sizes="100vw">

      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow"><span class="live-dot"></span>Monterrey, Nuevo León · México</p>

          <h1>BIENVENIDOS AL<br><span>PENTHOUSE</span><br>DEL BOXEO.</h1>

          <p class="hero-copy">Donde el talento se convierte en legado. Noches de boxeo de primer nivel en
            Monterrey, con proyección internacional a través de Box Azteca América.</p>

          <div class="mt-3">{countdown_block()}
          </div>

          <div class="row">
            <button class="btn" type="button" data-tickets>Comprar boletos {ico("arrow-right")}</button>
            <a class="btn btn-outline" href="eventos.html">Ver cartelera {ico("arrow-right")}</a>
          </div>
        </div>

        <img class="hero-logo" src="assets/img/logo-white.svg" width="258" height="228" alt="" aria-hidden="true">
      </div>

      <div class="wrap hero-bottom">
        <span>EL TALENTO ES LOCAL. EL ESCENARIO ES MUNDIAL.</span>
        <span>BAJA Y SIENTE EL RING ↓</span>
      </div>
    </section>

    <section class="section" aria-labelledby="t-evento">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="eyebrow">Próxima función</p>
            <h2 id="t-evento">UNA NOCHE.<br><span class="gold">TODO EN JUEGO.</span></h2>
          </div>
          <p class="muted small">El ring está listo para la siguiente historia.<br>Cartelera ilustrativa · detalles por confirmar.</p>
        </div>
        {event_card(full=False)}
      </div>
    </section>

    <section class="section" aria-labelledby="t-peleadores">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="eyebrow">El talento de casa</p>
            <h2 id="t-peleadores">HECHOS DE <span class="gold">CARÁCTER.</span></h2>
          </div>
          <a class="text-link" href="peleadores.html">Conoce a todos {ico("arrow-right")}</a>
        </div>
        <div class="names">
          <a href="peleadores.html"><p class="eyebrow">“La Roka”</p><h3>NELSON SALINAS</h3></a>
          <a href="peleadores.html"><p class="eyebrow">“El Guerrerito”</p><h3>ÓSCAR TORRES</h3></a>
          <a href="peleadores.html"><p class="eyebrow">“The Juggernaut”</p><h3>JORGE CÁZARES</h3></a>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="t-penthouse">
      <div class="wrap split">
        <div class="photo" role="img" aria-label="Fotografía ilustrativa de entrenamiento de boxeo">
          <img src="{IMG}/{GYM}?auto=format&fit=crop&q=80&w=900" alt="" loading="lazy" decoding="async" width="900" height="600">
          <span class="eyebrow">Pasión a nivel de ring.</span>
        </div>
        <div class="split-copy">
          <img class="penthouse-logo" src="assets/img/penthouse.svg" width="500" height="500" alt="El Penthouse del Boxeo" loading="lazy" decoding="async">
          <p class="eyebrow">The Penthouse</p>
          <h2 id="t-penthouse">EL BOXEO.<br>EN OTRO <span class="gold">NIVEL.</span></h2>
          <p class="muted">La intensidad del primer round. La cercanía de una experiencia exclusiva. El Penthouse reúne
            el espíritu de Monterrey y la emoción del boxeo en una noche que se vive con todos los sentidos.</p>
          <a href="penthouse.html" class="text-link">Descubre la experiencia VIP {ico("arrow-ur")}</a>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="t-media">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="eyebrow">Prime original stories</p>
            <h2 id="t-media">DETRÁS <span class="gold">DEL RING.</span></h2>
          </div>
          <a class="text-link" href="media.html">Ver todo el contenido {ico("arrow-right")}</a>
        </div>
        {video_cards()}
      </div>
    </section>
{partners()}
    <section class="band" aria-labelledby="t-band">
      <div class="wrap band-inner">
        <img class="band-logo" src="assets/img/logo-black.svg" width="276" height="245" alt="Prime Boxing Promotions" loading="lazy">
        <div>
          <h2 id="t-band">ÚNETE AL CLUB PRIME.</h2>
          <p>Carteleras, preventas y las historias que merecen estar en primera fila.</p>
        </div>
        <a class="btn btn-dark" href="contacto.html#club">Quiero acceso {ico("arrow-right")}</a>
      </div>
    </section>""",
)

# ------------------------------------------------------------------ EVENTOS
page(
    "eventos.html",
    "Eventos y cartelera | Prime Boxing Promotions",
    "Cartelera, fecha, sede y boletos de la próxima Fight Night de Prime Boxing Promotions en Monterrey.",
    "eventos.html",
    f"""{page_hero("Próxima función", "UNA NOCHE.<br><span>TODO EN JUEGO.</span>",
                   "El ring está listo para la siguiente historia. Cartelera ilustrativa · detalles por confirmar.")}
    <section class="section" aria-label="Evento principal">
      <div class="wrap">
        <div class="mb-3">{countdown_block()}</div>
        {event_card(full=True)}
      </div>
    </section>

    <section class="section" aria-labelledby="t-cartelera">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="eyebrow">Cartelera completa</p>
            <h2 id="t-cartelera">ORDEN DE <span class="gold">COMBATES.</span></h2>
          </div>
          <p class="muted small">Peleas, divisiones y rounds sujetos a confirmación oficial.</p>
        </div>
        <ol class="bouts">
          <li class="bout">
            <span class="badge">Main Event</span>
            <h3>NELSON “LA ROKA” SALINAS <span class="gold">VS. TBA</span></h3>
            <span class="status">Por confirmar</span>
          </li>
          <li class="bout">
            <span class="badge">Co-Main Event</span>
            <h3>ÓSCAR “EL GUERRERITO” TORRES <span class="gold">VS. TBA</span></h3>
            <span class="status">Por confirmar</span>
          </li>
          <li class="bout">
            <span class="badge">Preliminares</span>
            <h3>CARTELERA POR ANUNCIAR</h3>
            <span class="status">Próximamente</span>
          </li>
        </ol>
      </div>
    </section>

    <section class="section" aria-labelledby="t-boletos">
      <div class="wrap split">
        <div>
          <p class="eyebrow">Boletos</p>
          <h2 id="t-boletos">TU LUGAR<br>JUNTO AL <span class="gold">RING.</span></h2>
          <p class="muted mt-2" style="max-width:420px">La venta aún no está disponible. La fecha, los precios y el enlace
            oficial de boletos se anunciarán próximamente.</p>
        </div>
        <div>
          {tiers().replace('class="tickets"', 'class="tickets" style="margin-top:0"')}
          <button class="btn btn-block mt-3" type="button" data-tickets>Consultar boletos {ico("arrow-right")}</button>
          <p class="note">Sede: El Penthouse, Monterrey, N.L.</p>
        </div>
      </div>
    </section>""",
)

# ------------------------------------------------------------------ PELEADORES
page(
    "peleadores.html",
    "Peleadores | Prime Boxing Promotions",
    "Conoce al talento de casa de Prime Boxing Promotions: Nelson Salinas, Óscar Torres y Jorge Cázares.",
    "peleadores.html",
    f"""{page_hero("El talento de casa", "HECHOS DE<br><span>CARÁCTER.</span>",
                   "Monterrey en la sangre. La cima en la mira.")}
    <section class="section" aria-label="Peleadores">
      <div class="wrap">
        <div class="roster">{fighter_card("01", "La Roka", "NELSON SALINAS")}
          {fighter_card("02", "El Guerrerito", "ÓSCAR TORRES", flip=True)}
          {fighter_card("03", "The Juggernaut", "JORGE CÁZARES")}
        </div>
        <p class="note mt-3">Retratos, récords y divisiones se publicarán al confirmarse la información oficial.</p>
      </div>
    </section>

    <section class="section section-tight">
      <div class="wrap section-head" style="margin-bottom:0">
        <div>
          <p class="eyebrow">¿Eres peleador?</p>
          <h2>QUEREMOS<br>CONOCERTE.</h2>
        </div>
        <a class="btn" href="contacto.html">Contáctanos {ico("arrow-right")}</a>
      </div>
    </section>""",
)

# ------------------------------------------------------------------ PENTHOUSE
page(
    "penthouse.html",
    "The Penthouse | Prime Boxing Promotions",
    "La experiencia VIP del Penthouse del Boxeo: la intensidad del primer round en una noche exclusiva en Monterrey.",
    "penthouse.html",
    f"""{page_hero("The Penthouse", "EL BOXEO.<br>EN OTRO <span>NIVEL.</span>",
                   "La intensidad del primer round. La cercanía de una experiencia exclusiva.")}
    <section class="section">
      <div class="wrap split">
        <div class="photo" role="img" aria-label="Fotografía ilustrativa de entrenamiento de boxeo">
          <img src="{IMG}/{GYM}?auto=format&fit=crop&q=80&w=900" alt="" loading="lazy" decoding="async" width="900" height="600">
          <span class="eyebrow">Pasión a nivel de ring.</span>
        </div>
        <div class="split-copy">
          <img class="penthouse-logo" src="assets/img/penthouse.svg" width="500" height="500" alt="El Penthouse del Boxeo" loading="lazy" decoding="async">
          <p class="eyebrow">La experiencia</p>
          <h2>UNA NOCHE QUE SE VIVE CON TODOS LOS <span class="gold">SENTIDOS.</span></h2>
          <p class="muted">El Penthouse reúne el espíritu de Monterrey y la emoción del boxeo en una noche
            diseñada para sentirse. Detalles de accesos, hospitalidad y paquetes por anunciar.</p>
          <div class="row">
            <button class="btn" type="button" data-tickets>Consultar boletos {ico("arrow-right")}</button>
            <a class="btn btn-outline" href="contacto.html">Informes VIP {ico("arrow-right")}</a>
          </div>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="t-feat">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="eyebrow">Lo que define la noche</p>
            <h2 id="t-feat">TRES RAZONES PARA<br><span class="gold">ESTAR AQUÍ.</span></h2>
          </div>
        </div>
        <div class="features">
          <article class="feature"><h3>LA INTENSIDAD</h3><p class="muted">La energía del primer round, desde la primera campana hasta el último combate.</p></article>
          <article class="feature"><h3>LA CERCANÍA</h3><p class="muted">Una experiencia exclusiva donde el ring se siente al alcance de la mano.</p></article>
          <article class="feature"><h3>MONTERREY</h3><p class="muted">El orgullo regiomontano y el talento local, con proyección internacional.</p></article>
        </div>
      </div>
    </section>

    <section class="band" aria-labelledby="t-band">
      <div class="wrap band-inner">
        <img class="band-logo" src="assets/img/logo-black.svg" width="276" height="245" alt="Prime Boxing Promotions" loading="lazy">
        <div>
          <h2 id="t-band">TU LUGAR JUNTO AL RING.</h2>
          <p>Ringside VIP, Preferente y General. Venta próximamente.</p>
        </div>
        <a class="btn btn-dark" href="eventos.html">Ver cartelera {ico("arrow-right")}</a>
      </div>
    </section>""",
)

# ------------------------------------------------------------------ MEDIA
page(
    "media.html",
    "Media | Prime Boxing Promotions",
    "Documentales, highlights y training camp de Prime Boxing Promotions. Antes de la campana, hay una historia.",
    "media.html",
    f"""{page_hero("Prime original stories", "DETRÁS<br><span>DEL RING.</span>",
                   "Antes de la campana, hay una historia.")}
    <section class="section">
      <div class="wrap">{video_cards()}
        <p class="note mt-3">Los videos oficiales se publicarán próximamente.</p>
      </div>
    </section>""",
)

# ------------------------------------------------------------------ CONTACTO
page(
    "contacto.html",
    "Contacto y Club Prime | Prime Boxing Promotions",
    "Únete al Club Prime y contacta a Prime Boxing Promotions para prensa, acreditaciones y patrocinios en Monterrey.",
    "contacto.html",
    f"""{page_hero("Acceso a lo extraordinario", "HABLEMOS<br><span>DE BOXEO.</span>",
                   "Suscríbete a las novedades o escríbenos para prensa, acreditaciones y patrocinios.")}
    <section id="club" class="section" aria-labelledby="t-club">
      <div class="wrap newsletter">
        <div>
          <p class="eyebrow">Club Prime</p>
          <h2 id="t-club" class="mt-1">ÚNETE AL <span class="gold">CLUB PRIME.</span></h2>
          <p class="muted small mt-2">Carteleras, preventas y las historias que merecen estar en primera fila.</p>
        </div>

        <form id="newsletter" novalidate>
          <label for="email" class="small">Tu correo electrónico</label>
          <div class="signup">
            <input id="email" name="email" type="email" autocomplete="email"
                   placeholder="tu@correo.com" required maxlength="254">
            <button type="submit" aria-label="Solicitar acceso al Club Prime">{ico("arrow-right")}</button>
          </div>
          <label class="check">
            <input type="checkbox" name="consent" required>
            Acepto recibir novedades de Prime Boxing Promotions.
          </label>
          <p id="signupStatus" class="note" role="status">Vista previa: el registro aún no está conectado a un servicio de correo.</p>
        </form>
      </div>
    </section>

    <section id="patrocinios" class="section" aria-label="Canales de contacto">
      <div class="wrap contact-grid">
        <article class="contact-card">
          <p class="eyebrow">Prensa</p>
          <h3>ACREDITACIONES</h3>
          <p class="muted small">Monterrey, Nuevo León, México. Canal oficial de contacto por anunciar.</p>
          <button class="text-link gold mt-2" type="button" data-contact>Escribir a prensa {ico("arrow-ur")}</button>
        </article>
        <article class="contact-card">
          <p class="eyebrow">Patrocinios</p>
          <h3>TU MARCA AQUÍ</h3>
          <p class="muted small">Conviértete en parte de las noches de boxeo de primer nivel en Monterrey.</p>
          <button class="text-link gold mt-2" type="button" data-contact>Hablar de patrocinios {ico("arrow-ur")}</button>
        </article>
        <article class="contact-card">
          <p class="eyebrow">Redes</p>
          <h3>SÍGUENOS</h3>
          <p class="muted small">Los perfiles oficiales se anunciarán próximamente.</p>
          <div class="socials mt-2" role="group" aria-label="Redes sociales">{social_buttons()}</div>
        </article>
      </div>
    </section>
{partners()}""",
)
