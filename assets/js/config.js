/*
 * CONFIGURACIÓN DE LANZAMIENTO — edita solo este archivo.
 * Reemplaza los valores vacíos por información verificada.
 * Mientras estén vacíos, el sitio muestra mensajes de "próximamente".
 */
window.PRIME_CONFIG = {
  // Fecha confirmada del evento. Formato: "2027-02-20T20:00:00-06:00"
  eventDate: null,
  // Fecha usada SOLO para la cuenta regresiva de demostración (se etiqueta como tal).
  demoDate: "2026-11-28T18:00:00-06:00",

  ticketUrl: "https://boletomovil.com/evento/prime-boxing-003-2026-11-28?utm_source=ig&utm_medium=social&utm_content=link_in_bio&fbclid=PAZXh0bgNhZW0CMTEAcGRvZgJzcnRjBmFwcF9pZA85MzY2MTk3NDMzOTI0NTkAAafZUSpFdg1s5mz7luGci7At7yWd8auWs4SIDr5_uTAgoaGh83uHFA6dRWwhHw_aem_3ee5a86VSzfRyVmOLuid_w",           // https://...
  newsletterEndpoint: "",  // POST JSON { email, consent: true } → respuesta 2xx
  contactEmail: "",        // prensa@tudominio.com

  socials: { Instagram: "https://www.instagram.com/primeboxingmx?utm_source=ig_web_button_share_sheet&psln=ZDNlZDc0MzIxNw==", Facebook: "https://www.facebook.com/profile.php?id=61588041005790&ref=PROFILE_EDIT_xav_ig_profile_page_web", YouTube: "" },

  // URLs HTTPS de MP4 autorizados para activar el reproductor.
  videos: { historia: "", highlights: "", camp: "" }
};
