self.addEventListener('install', (event) => {
    console.log('Service Worker: Install event triggered');
});

self.addEventListener('activate', (event) => {
    console.log('Service Worker: Activate event triggered');
});