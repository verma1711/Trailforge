window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 10) {
      navbar.classList.add('bg-gray-800', 'bg-opacity-90', 'shadow-md');
    } else {
      navbar.classList.remove('bg-gray-800', 'bg-opacity-90', 'shadow-md');
    }
  });

// -------------------------------------------- Dashboard Edit and forgot password logic -----------------------------------
const body = document.body;
    function openModal(id) {
      const m = document.getElementById(id);
      if (!m) return;
      m.classList.remove('hidden');
      m.classList.add('flex');
      body.classList.add('overflow-hidden');
    }
    function closeModal(id) {
      const m = document.getElementById(id);
      if (!m) return;
      m.classList.add('hidden');
      m.classList.remove('flex');
      body.classList.remove('overflow-hidden');
    }
    document.getElementById('editProfileBtn')?.addEventListener('click', () => openModal('editProfileModal'));
    document.getElementById('forgotPwdBtn')?.addEventListener('click', () => openModal('forgotPwdModal'));
    document.querySelectorAll('[data-close]').forEach(btn => {
      btn.addEventListener('click', () => closeModal(btn.getAttribute('data-close')));
    });
    ['editProfileModal','forgotPwdModal'].forEach(id => {
      const modal = document.getElementById(id);
      modal?.addEventListener('click', (e) => { if (e.target === modal) closeModal(id); });
    });
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeModal('editProfileModal');
        closeModal('forgotPwdModal');
      }
    });
    const profileAvatar = document.getElementById('profileAvatar');
    const profileName = document.getElementById('profileName');
    const greetingName = document.getElementById('greetingName');
    const inputFullName = document.getElementById('inputFullName');
    const inputUsername = document.getElementById('inputUsername');
    const inputAvatar = document.getElementById('inputAvatar');
    const editPreviewAvatar = document.getElementById('editPreviewAvatar');
    if (!profileAvatar.getAttribute('src')) {
      profileAvatar.setAttribute('src', 'data:image/svg+xml;utf8,' + encodeURIComponent(`<svg xmlns="http://www.w3.org/2000/svg" width="128" height="128"><rect width="100%" height="100%" fill="#374151"/><circle cx="64" cy="48" r="24" fill="#9CA3AF"/><rect x="24" y="84" width="80" height="28" rx="14" fill="#9CA3AF"/></svg>`));
      editPreviewAvatar.setAttribute('src', profileAvatar.getAttribute('src'));
    }
    inputFullName.addEventListener('input', () => {
      profileName.textContent = inputFullName.value || 'New Driver';
      greetingName.textContent = inputFullName.value || 'Driver';
    });
    inputAvatar.addEventListener('change', (e) => {
      const file = e.target.files && e.target.files[0];
      if (!file) return;
      const validTypes = ['image/jpeg','image/png','image/webp','image/gif'];
      if (!validTypes.includes(file.type)) {
        alert('Please choose an image file (jpg, png, webp, gif).');
        e.target.value = '';
        return;
      }
      const reader = new FileReader();
      reader.onload = (evt) => {
        const dataUrl = evt.target.result;
        editPreviewAvatar.src = dataUrl;
        profileAvatar.src = dataUrl;
      };
      reader.readAsDataURL(file);
    });
    function applyProfileChanges() {
      const uname = inputUsername.value.trim();
      closeModal('editProfileModal');
    }
    window.applyProfileChanges = applyProfileChanges;
    // -------------------------------------------- END Dashboard Edit and forgot password logic -----------------------------------
