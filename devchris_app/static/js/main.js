document.addEventListener("DOMContentLoaded", function () {
  burger = document.querySelector(".hamburger");
  navClose = document.querySelector(".close-nav");
  logoDiv = document.getElementById("site-name");
  if (burger) {
    burger.addEventListener("click", toggleMenu);
  }
  if (navClose) {
    navClose.addEventListener("click", toggleMenu);
  }

  if (logoDiv) {
    logoDiv.addEventListener("click", goHome);
  }

  function toggleMenu() {
    document.querySelector(".main-nav").classList.toggle("active");
  }

  function goHome() {
    window.location.href = "/";
  }

  anchor = document.querySelector(".back-to-top");
  anchor.addEventListener("click", function (e) {
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior: "smooth",
    });
  });

  function pauseVideoOnScroll() {
    var video = document.querySelector(".bg-video");
    if (video) {
      video.pause();
    }
  }

  window.addEventListener("scroll", pauseVideoOnScroll, { passive: true });

  const contactForm = document.getElementById("my-contact-form");
  const fMessage = document.getElementById("form-message");

  contactForm.addEventListener("submit", function (e) {
    e.preventDefault();
    var formData = new FormData(this);
    fetch(this.action, {
      method: "POST",
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]")
          .value,
      },
    })
      .then((response) => response.json())
      .then((data) => {
        loadMessage(data);
      })
      .catch((error) => {
        loadMessage(error);
      });
  });

  function loadMessage(data) {
    fMessage.innerHTML = '<div class="loader"></div>';
    setTimeout(() => {
      if (data.success) {
        fMessage.innerHTML =
          '<span style="color:green;">' + data.message + "</span>";
      } else {
        fMessage.innerHTML =
          '<span style="color:red;">An error occurred. Please try again later.</span>';
      }
      document.getElementById("my-contact-form").reset();
    }, 1200);
  }
});
