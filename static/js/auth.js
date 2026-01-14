function requireAuth() {
  const token = localStorage.getItem("access_token");
  if (!token) {
    window.location.href = "/playground/login/";
  }
}

function logout() {
  localStorage.removeItem("access_token");
  window.location.href = "/playground/login/";
}

function isOrganizer(){
  const currentUser = JSON.parse(localStorage.getItem("currentUser"));
  return currentUser && currentUser?.role === "organizer";

}