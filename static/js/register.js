// If user is already logged in, redirect to events page
if (localStorage.getItem("access_token")) {
  window.location.href = "/playground/events/";
}

async function handleRegister(event) {
  event.preventDefault();

  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirm-password").value;
  const roleSelect = document.getElementById("role");
  // Default to 'attendee' if role selection is not present or empty
  const role = roleSelect && roleSelect.value ? roleSelect.value : "member";

  if (password !== confirmPassword) {
    showToast("Passwords do not match", "error");
    return;
  }

  const submitBtn = event.target.querySelector("button[type='submit']");
  const originalBtnText = submitBtn ? submitBtn.innerText : "Register";

  if (submitBtn) {
    submitBtn.disabled = true;
    submitBtn.innerText = "Creating Account...";
  }

  try {
    await apiFetch("/api/v1/users/register/", {
      method: "POST",
      body: JSON.stringify({
        username,
        email,
        password,
        role,
      }),
    });

    showToast("Registration successful! Redirecting to login...", "success");
    setTimeout(() => {
      window.location.href = "/playground/login/";
    }, 1500);
  } catch (error) {
    if (submitBtn) {
      submitBtn.disabled = false;
      submitBtn.innerText = originalBtnText;
    }
    showToast(error.message || "Registration failed", "error");
  }
}