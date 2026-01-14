async function apiFetch(url, options = {}) {
  const token = localStorage.getItem("access_token");

  const headers = {
    "Content-Type": "application/json",
    ...(options.headers || {}),
  };

  if (token) {
    headers["Authorization"] = "Bearer " + token;
  }

  try {
    const response = await fetch(url, {
      ...options,
      headers,
    });
    console.log(response);

    // 🔐 Auth expired
    if (response.status === 401) {
    //   showToast("Session expired. Please login again.", "error");
      localStorage.removeItem("access_token");
      setTimeout(() => {
        window.location.href = "/playground/login/";
      }, 1500);
      throw new Error("Unauthorized");
    }

    const data =
      response.status !== 204 ? await response.json() : null;

    if (!response.ok) {
      const message =
        data?.detail ||
        data?.message ||
        "Something went wrong";
      throw new Error(message);
    }

    return data;
  } catch (err) {
    console.error(err.message || "Network error");
    throw err;
  }
}
