/* PRIME BOXING PROMOTIONS — comportamiento compartido (todas las páginas) */
(() => {
  "use strict";

  const C = window.PRIME_CONFIG || {};
  const $ = (sel, root = document) => root.querySelector(sel);
  const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

  /* ---------- Menú móvil ---------- */
  const menuButton = $("#menuButton");
  const navigation = $("#navigation");

  if (menuButton && navigation) {
    const setMenu = open => {
      navigation.classList.toggle("open", open);
      menuButton.setAttribute("aria-expanded", String(open));
      menuButton.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
    };

    menuButton.addEventListener("click", () =>
      setMenu(!navigation.classList.contains("open")));

    navigation.addEventListener("click", e => {
      if (e.target.closest("a")) setMenu(false);
    });

    document.addEventListener("keydown", e => {
      if (e.key === "Escape" && navigation.classList.contains("open")) {
        setMenu(false);
        menuButton.focus();
      }
    });

    document.addEventListener("click", e => {
      if (!e.target.closest(".nav")) setMenu(false);
    });

    matchMedia("(min-width:761px)").addEventListener("change", () => setMenu(false));
  }

  /* ---------- Movimiento progresivo, sin ocultar contenido base ---------- */
  const motionPreference = matchMedia("(prefers-reduced-motion: reduce)");
  const activeAnimations = new Set();
  const entrance = (element, delay = 0) => {
    if (motionPreference.matches || !element.animate) return;
    const animation = element.animate([
      { opacity: 0, transform: "translateY(24px)" },
      { opacity: 1, transform: "translateY(0)" }
    ], { duration: 720, delay, easing: "cubic-bezier(.22,1,.36,1)", fill: "backwards" });
    activeAnimations.add(animation);
    animation.finished.catch(() => {}).finally(() => activeAnimations.delete(animation));
  };
  motionPreference.addEventListener("change", () => {
    if (motionPreference.matches) activeAnimations.forEach(animation => animation.cancel());
  });

  $$(".hero-grid > div > *, .hero-logo, .page-hero .wrap > *")
    .forEach((element, index) => entrance(element, Math.min(index, 5) * 85));

  if ("IntersectionObserver" in window) {
    const reveal = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        entrance(entry.target, Number(entry.target.dataset.motionDelay || 0));
        reveal.unobserve(entry.target);
      });
    }, { threshold: 0.08 });
    $$(".section-head, .event, .names, .split > *, .fighter, .feature, .video-card, .contact-card, .newsletter, .band-inner, .partners")
      .forEach(element => {
        const siblings = Array.from(element.parentElement.children);
        element.dataset.motionDelay = Math.min(siblings.indexOf(element), 2) * 70;
        reveal.observe(element);
      });

    const header = $(".nav");
    const hero = $(".hero, .page-hero");
    if (header && hero) {
      new IntersectionObserver(([entry]) => {
        header.classList.toggle("is-scrolled", !entry.isIntersecting);
      }).observe(hero);
    }
  }

  /* ---------- Diálogo accesible (se crea al primer uso) ---------- */
  let dialog, titleEl, textEl, player;

  function ensureDialog() {
    if (dialog) return;

    dialog = document.createElement("dialog");
    dialog.setAttribute("aria-labelledby", "dialogTitle");
    dialog.setAttribute("aria-describedby", "dialogText");
    dialog.innerHTML =
      '<button class="icon-btn close" type="button" aria-label="Cerrar ventana">' +
        '<svg class="i" aria-hidden="true"><use href="#i-x"/></svg></button>' +
      '<p class="eyebrow">Prime Boxing Promotions</p>' +
      '<h2 id="dialogTitle"></h2><p id="dialogText"></p>' +
      '<video controls playsinline preload="none" hidden aria-label="Reproductor de video"></video>' +
      '<button class="btn mt-2" type="button">Entendido</button>';
    document.body.appendChild(dialog);

    titleEl = $("#dialogTitle", dialog);
    textEl = $("#dialogText", dialog);
    player = $("video", dialog);

    $$("button", dialog).forEach(b => b.addEventListener("click", () => dialog.close()));

    dialog.addEventListener("click", e => {
      if (e.target !== dialog) return;
      const r = dialog.getBoundingClientRect();
      const outside = e.clientX < r.left || e.clientX > r.right ||
                      e.clientY < r.top || e.clientY > r.bottom;
      if (outside) dialog.close();
    });

    dialog.addEventListener("close", () => {
      player.pause();
      player.removeAttribute("src");
      player.load();
      player.hidden = true;
    });

    player.addEventListener("error", () => {
      textEl.textContent = "No se pudo cargar el video. Inténtalo de nuevo más tarde.";
    });
  }

  function showInfo(title, message, videoSrc) {
    ensureDialog();
    titleEl.textContent = title;
    textEl.textContent = message;
    if (videoSrc) { player.src = videoSrc; player.hidden = false; }
    dialog.showModal();
  }

  /* ---------- Boletos ---------- */
  $$("[data-tickets]").forEach(btn => btn.addEventListener("click", () => {
    if (C.ticketUrl) { window.location.assign(C.ticketUrl); return; }
    showInfo(
      "TU LUGAR JUNTO AL RING.",
      "La venta aún no está disponible. La fecha, los precios y el enlace " +
      "oficial de boletos se anunciarán próximamente."
    );
  }));

  /* ---------- Videos ---------- */
  $$("[data-video]").forEach(btn => btn.addEventListener("click", () => {
    const src = (C.videos || {})[btn.dataset.video];
    const title = btn.dataset.title || "Video";
    showInfo(
      title,
      src ? "Disfruta la historia."
          : "Este contenido se estrenará próximamente. El reproductor estará " +
            "disponible cuando se publique el video oficial.",
      src
    );
  }));

  /* ---------- Redes sociales ---------- */
  $$("[data-social]").forEach(btn => btn.addEventListener("click", () => {
    const network = btn.dataset.social;
    const url = (C.socials || {})[network];
    if (url) window.open(url, "_blank", "noopener,noreferrer");
    else showInfo(network, "El perfil oficial se anunciará próximamente.");
  }));

  /* ---------- Prensa y patrocinios ---------- */
  $$("[data-contact]").forEach(btn => btn.addEventListener("click", () => {
    if (C.contactEmail) { window.location.href = "mailto:" + C.contactEmail; return; }
    showInfo(
      "HABLEMOS DE BOXEO.",
      "Para prensa, acreditaciones y patrocinios en Monterrey: el canal " +
      "oficial de contacto se anunciará próximamente."
    );
  }));

  /* ---------- Cuenta regresiva (zona horaria de Monterrey explícita) ---------- */
  const countdowns = $$("[data-countdown]");
  const target = Date.parse(C.eventDate || C.demoDate);

  if (countdowns.length) {
    const fmt = new Intl.DateTimeFormat("es-MX", {
      dateStyle: "long", timeStyle: "short", timeZone: "America/Monterrey"
    });
    const pad = n => String(n).padStart(2, "0");

    const tick = () => {
      countdowns.forEach(box => {
        const label = $("[data-countdown-label]", box.parentElement) || $("[data-countdown-label]");

        if (!Number.isFinite(target)) {
          if (label) label.textContent = "Próxima función · Fecha por anunciar";
          return;
        }

        const now = Date.now();
        const s = Math.max(0, Math.floor((target - now) / 1000));
        const v = {
          days: Math.floor(s / 86400),
          hours: Math.floor((s % 86400) / 3600),
          minutes: Math.floor((s % 3600) / 60),
          seconds: s % 60
        };
        Object.keys(v).forEach(k => {
          const el = $('[data-unit="' + k + '"]', box);
          if (el) el.textContent = pad(v[k]);
        });

        if (label) {
          label.textContent = now >= target
            ? (C.eventDate ? "La cuenta regresiva ha terminado · Consulta la cartelera"
                           : "Cuenta regresiva de demostración finalizada")
            : (C.eventDate ? "Próxima Fight Night · " + fmt.format(target)
                           : "Próxima Fight Night · cuenta regresiva de demostración");
        }
      });
    };

    tick();
    let timer = setInterval(tick, 1000);

    /* No gastar CPU con la pestaña en segundo plano */
    document.addEventListener("visibilitychange", () => {
      clearInterval(timer);
      if (!document.hidden) { tick(); timer = setInterval(tick, 1000); }
    });

    if (C.eventDate && Number.isFinite(target)) {
      $$("[data-event-date]").forEach(el => {
        el.textContent = fmt.format(target) + " · Hora de Monterrey";
      });
    }
  }

  /* ---------- Año del footer ---------- */
  $$("[data-year]").forEach(el => { el.textContent = new Date().getFullYear(); });

  /* ---------- Club Prime (solo en contacto) ---------- */
  const form = $("#newsletter");
  if (form) {
    const status = $("#signupStatus");
    const button = $("button[type=submit]", form);

    form.addEventListener("submit", async e => {
      e.preventDefault();
      if (!form.reportValidity()) return;

      if (!C.newsletterEndpoint) {
        status.textContent =
          "Registro en modo de vista previa: tu correo no se ha enviado ni " +
          "guardado. El Club Prime abrirá próximamente.";
        return;
      }

      button.disabled = true;
      form.setAttribute("aria-busy", "true");
      status.textContent = "Enviando solicitud…";

      try {
        const res = await fetch(C.newsletterEndpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ email: form.elements.email.value.trim(), consent: true })
        });
        if (!res.ok) throw new Error("Subscription failed");
        status.textContent = "Solicitud recibida. Revisa tu correo para confirmar tu suscripción.";
        form.reset();
      } catch {
        status.textContent = "No se pudo completar el registro. Inténtalo de nuevo más tarde.";
      } finally {
        button.disabled = false;
        form.removeAttribute("aria-busy");
      }
    });
  }
})();
