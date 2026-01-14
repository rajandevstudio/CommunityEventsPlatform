function formatDate(dateString) {
  const options = {
    year: "numeric",
    month: "long",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  };
  return new Date(dateString).toLocaleDateString(undefined, options);
}

async function loadEvents() {
  requireAuth();

  const container = document.getElementById("events");
  container.innerHTML = `<p class="text-gray-500">Loading events...</p>`;

  try {
    const data = await apiFetch("/api/v1/events/");
    const events = data.results;
    const currentUser = JSON.parse(localStorage.getItem("currentUser"));
      console.info(currentUser, 'currentUser')

    container.innerHTML = "";

    if (events.length === 0) {
      container.innerHTML = `<p class="text-gray-500">No events found.</p>`;
      return;
    }

    events.forEach((e) => {
      const description =
        e.description.length > 100
          ? `${e.description.substring(0, 100)}...`
          : e.description;
      const isOrganizer = e.organizer?.username === currentUser.username;
      const hasJoined = e.participants.includes(currentUser.username);
      const isFull = e.participants.length >= e.capacity;

      let actionButton;
      if (isOrganizer) {
        actionButton = `
          <div class="flex space-x-2">
            <button
              class="w-1/2 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg"
              onclick="handleEditEvent(${e.id})"
            >
              Edit
            </button>
            <button
              class="w-1/2 bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-lg"
              onclick="handleDeleteEvent(${e.id})"
            >
              Delete
            </button>
          </div>
        `;
      } else if (hasJoined) {
        actionButton = `
          <button
            class="w-full bg-yellow-500 hover:bg-yellow-600 text-white font-bold py-2 px-4 rounded-lg"
            onclick="handleLeaveEvent(${e.id}, this)"
          >
            Leave Event
          </button>
        `;
      } else if (isFull) {
        actionButton = `
          <button
            class="w-full bg-gray-400 text-white font-bold py-2 px-4 rounded-lg"
            disabled
          >
            Event Full
          </button>
        `;
      } else {
        actionButton = `
          <button
            class="w-full bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out"
            onclick="handleJoinEvent(${e.id}, this)"
          >
            Join Event
          </button>
        `;
      }
      console.log(e);
      const eventCard = `
        <div class="bg-white rounded-xl shadow-md overflow-hidden flex flex-col">
          <div class="p-6">
            <h3 class="text-2xl font-semibold text-gray-800 mb-2">${
              e.title
            }</h3>
            <p class="text-sm text-gray-500 mb-4">
              <span class="font-semibold">When:</span> ${formatDate(
                e.start_time
              )}
            </p>
            <p class="text-sm text-gray-500 mb-4">
              <span class="font-semibold">Where:</span> ${e.location}
            </p>
            <p class="text-gray-700 mb-4">${description}</p>
             <p class="text-sm text-gray-600">
              <span class="font-semibold">Organizer:</span> ${
                e.organizer ? e.organizer?.username || e.organizer : "N/A"
              }
            </p>
          </div>

          <div class="px-6 pb-4 flex flex-col justify-end h-full mt-auto">
            <div class="flex justify-between items-center text-sm text-gray-600 mb-4">
              <span>
                <span class="font-semibold">Capacity:</span>
                ${e.participants.length} / ${e.capacity}
              </span>
            </div>
            ${e.participants && e.participants.length > 0
  ? `
    <div class="flex justify-between items-center text-sm text-gray-600 mb-4">
      <span>
        <span class="font-semibold">Participants:</span>
        ${e.participants}
      </span>
    </div>
  `
  : ""
}

            
            ${actionButton}
          </div>
        </div>
      `;
      container.innerHTML += eventCard;
    });
  } catch (error) {
    container.innerHTML = `<p class="text-red-500">Error loading events. Please try again later.</p>`;
    console.error("Failed to load events:", error);
  }
}

async function handleJoinEvent(id, btn) {
  btn.disabled = true;
  btn.innerText = "Joining...";

  try {
    await apiFetch(`/api/v1/events/${id}/join/`, {
      method: "POST",
    });

    showToast("Joined event successfully", "success");
    loadEvents(); // Reload events to show updated state
  } catch (error) {
    btn.disabled = false;
    btn.innerText = "Join Event";
    showToast(error.message || "Failed to join event", "error");
  }
}

async function handleLeaveEvent(id, btn) {
  btn.disabled = true;
  btn.innerText = "Leaving...";

  try {
    await apiFetch(`/api/v1/events/${id}/leave/`, {
      method: "POST",
    });

    showToast("Left event successfully", "success");
    loadEvents(); // Reload events to show updated state
  } catch (error) {
    btn.disabled = false;
    btn.innerText = "Leave Event";
    showToast(error.message || "Failed to leave event", "error");
  }
}

function handleEditEvent(eventId) {
  window.location.href = `/playground/events/create/?id=${eventId}`;
}

async function handleDeleteEvent(eventId) {
  if (!confirm("Are you sure you want to delete this event?")) {
    return;
  }

  try {
    await apiFetch(`/api/v1/events/${eventId}/`, {
      method: "DELETE",
    });

    showToast("Event deleted successfully", "success");
    loadEvents(); // Reload events to reflect the deletion
  } catch (error) {
    showToast(error.message || "Failed to delete event", "error");
  }
}

