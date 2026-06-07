const V = 'rodada-v4'; // ← subir versión fuerza recarga de todos los archivos
const SHELL = ['./', './index.html', './manifest.json', './icon.svg'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(V).then(c => c.addAll(SHELL)));
  self.skipWaiting();
});

self.addEventListener('activate', e => {
  // Elimina cachés viejos (v1, v2-anterior, etc.)
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== V).map(k => {
        console.log('Eliminando caché viejo:', k);
        return caches.delete(k);
      }))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const url = e.request.url;
  // Tiles, fonts y CDNs: red primero (siempre frescos)
  if (url.includes('tile') || url.includes('fonts') ||
      url.includes('unpkg') || url.includes('googleapis') ||
      url.includes('anthropic')) {
    e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
    return;
  }
  // App shell: network first para ver siempre cambios frescos
  e.respondWith(
    fetch(e.request)
      .then(res => {
        const clone = res.clone();
        caches.open(V).then(c => c.put(e.request, clone));
        return res;
      })
      .catch(() => caches.match(e.request))
  );
});
