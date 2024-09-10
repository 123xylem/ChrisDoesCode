document.addEventListener("DOMContentLoaded", function () {
  burger = document.querySelector(".hamburger");
  navClose = document.querySelector(".close-nav");
  if (burger) {
    burger.addEventListener("click", toggleMenu);
  }
  if (navClose) {
    navClose.addEventListener("click", toggleMenu);
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
    if (!customFormTextareaValidation(".form-message textarea")) {
      return "Spam Detected";
    }

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

  function customFormTextareaValidation(selector) {
    // List of blocked words
    let blockedWords = [
      " seo ",
      "marketing",
      "plugin",
      "website",
      "backlink",
      "link building",
      "emails",
      " market",
      " ai ",
      "million",
      "billion",
      " users",
      " volume",
      " spam",
      "business",
      "healthy",
      "drug",
    ];
    let blocked = false;

    // Get the textarea field value and convert to lowercase
    let fieldSubmit = document.querySelector(selector).value.toLowerCase();

    // Regular expressions for Russian, Chinese, and Cyrillic characters
    let russianRegex = /[\u0400-\u04FF]/;
    let chineseRegex = /[\u4E00-\u9FFF]/;
    let cyrillicRegex = /[\u0400-\u04FF]/;

    blockedWords.forEach(function (word) {
      if (fieldSubmit.includes(word)) {
        blocked = true;
      }
    });

    if (
      russianRegex.test(fieldSubmit) ||
      chineseRegex.test(fieldSubmit) ||
      cyrillicRegex.test(fieldSubmit)
    ) {
      blocked = true;
    }

    // If blocked content is found, show an alert message or handle error as needed
    if (blocked) {
      alert("Your message contains prohibited content.");
      return false;
    }

    return true;
  }
});
