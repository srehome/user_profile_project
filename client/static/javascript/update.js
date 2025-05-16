document.addEventListener('DOMContentLoaded', () => {
  const registerButton = document.querySelector(".register-button");

  if (registerButton) {
    registerButton.addEventListener('mouseover', () => {
      registerButton.style.transform = 'scale(0.95)';
    });
    registerButton.addEventListener('mouseout', () => {
      registerButton.style.transform = 'scale(1)';
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