document.addEventListener('DOMContentLoaded', () => {
  const registerButton = document.querySelector(".register-btn");
  const loginButton = document.querySelector(".login-btn");

  if (registerButton && loginButton) {
    registerButton.addEventListener('mouseover', () => {
      registerButton.style.transform = 'scale(0.95)';
      registerButton.style.backgroundColor = '#f0f0f0';
    });
    registerButton.addEventListener('mouseout', () => {
      registerButton.style.transform = 'scale(1)';
      registerButton.style.backgroundColor = 'white';
    });
    loginButton.addEventListener('mouseover', () => {
      loginButton.style.transform = 'scale(0.95)';
      loginButton.style.backgroundColor = '#f0f0f0';
    });
    loginButton.addEventListener('mouseout', () => {
      loginButton.style.transform = 'scale(1)';
      loginButton.style.backgroundColor = 'white';
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