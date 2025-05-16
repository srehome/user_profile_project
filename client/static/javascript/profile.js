document.addEventListener('DOMContentLoaded', () => {
  const logoutButton = document.querySelector(".logout-btn");

  if (logoutButton) {
    logoutButton.addEventListener('mouseover', () => {
      logoutButton.style.transform = 'scale(0.95)';
    });
    logoutButton.addEventListener('mouseout', () => {
      logoutButton.style.transform = 'scale(1)';
    });
  }
});
document.addEventListener('DOMContentLoaded', () => {
  const updateButton = document.querySelector(".update-btn");

  if (updateButton) {
    updateButton.addEventListener('mouseover', () => {
      updateButton.style.transform = 'scale(0.95)';
    });
    updateButton.addEventListener('mouseout', () => {
      updateButton.style.transform = 'scale(1)';
    });
  }
});
document.addEventListener('DOMContentLoaded', () => {
  const uploadButton = document.querySelector(".upload-btn");

  if (uploadButton) {
    uploadButton.addEventListener('mouseover', () => {
      uploadButton.style.transform = 'scale(0.95)';
    });
    uploadButton.addEventListener('mouseout', () => {
      uploadButton.style.transform = 'scale(1)';
    });
  }
});
document.addEventListener('DOMContentLoaded', () => {
  const selectButton = document.querySelector(".custom-file-upload");

  if (selectButton) {
    selectButton.addEventListener('mouseover', () => {
      selectButton.style.transform = 'scale(0.95)';
    });
    selectButton.addEventListener('mouseout', () => {
      selectButton.style.transform = 'scale(1)';
    });
  }
});

document.addEventListener('DOMContentLoaded', () => { /* <-- modified AI-answer */
  const closeButton = document.querySelector('.alert-warning .close');
  const alertWarning = document.querySelector('.alert-warning');

  if (closeButton && alertWarning) {
    closeButton.addEventListener('click', () => {
      alertWarning.style.display = 'none';
    });
  }
});