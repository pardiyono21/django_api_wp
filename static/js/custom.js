let lastScrollPosition = 0;

window.addEventListener('scroll', function () {
    const scrollMenu = document.getElementById('scrollMenu');
    const currentScrollPosition = window.pageYOffset;

    if (currentScrollPosition > lastScrollPosition) {
        // Scroll ke bawah -> Sembunyikan menu
        scrollMenu.classList.add('hidden');
    } else {
        // Scroll ke atas -> Tampilkan menu
        scrollMenu.classList.remove('hidden');
    }

    // Perbarui posisi scroll terakhir
    lastScrollPosition = currentScrollPosition;
});


// Ambil semua tombol tema
const themeButtons = document.querySelectorAll('[data-bs-theme-value]');

// Fungsi untuk mengganti tema
function setTheme(theme) {
  // Ganti atribut data-bs-theme pada elemen <html>
  document.documentElement.setAttribute("data-bs-theme", theme);

  // Update kelas active pada tombol dropdown
  themeButtons.forEach(button => {
    const isLight = button.getAttribute("data-bs-theme-value") === "light";
    if (theme === "light" && isLight) {
      button.classList.add("active");
    } else if (theme === "dark" && !isLight) {
      button.classList.add("active");
    } else {
      button.classList.remove("active");
    }
  });

  // Simpan tema pilihan pengguna ke localStorage (agar tetap bertahan setelah refresh)
  localStorage.setItem("theme", theme);
}

// Cek tema yang disimpan di localStorage dan terapkan
const storedTheme = localStorage.getItem("theme");
if (storedTheme) {
  setTheme(storedTheme);
} else {
  setTheme("light"); // Default mode
}

// Event listener untuk tombol dropdown
themeButtons.forEach(button => {
  button.addEventListener("click", (e) => {
    const selectedTheme = e.target.getAttribute("data-bs-theme-value");
    setTheme(selectedTheme);
  });
});
