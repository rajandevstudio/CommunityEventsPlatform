(function () {
  const container = document.createElement("div");
  container.id = "toast-container";
  container.className =
    "fixed top-5 right-5 z-50 space-y-3";
  document.body.appendChild(container);

  window.showToast = function (
    message,
    type = "info",
    timeout = 3000
  ) {
    const toast = document.createElement("div");

    const colors = {
      success: "bg-green-500",
      error: "bg-red-500",
      info: "bg-blue-500",
      warning: "bg-yellow-500 text-black",
    };

    toast.className = `
      ${colors[type] || colors.info}
      text-white px-4 py-3 rounded shadow-lg
      animate-fade-in
    `;

    toast.innerText = message;
    container.appendChild(toast);

    setTimeout(() => {
      toast.classList.add("opacity-0");
      setTimeout(() => toast.remove(), 300);
    }, timeout);
  };
})();
