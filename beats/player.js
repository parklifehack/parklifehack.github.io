(function () {
  const players = document.querySelectorAll("[data-player]");

  players.forEach((player) => {
    const audio = player.querySelector("[data-audio]");
    const currentTitle = player.querySelector("[data-current-title]");
    const tracks = Array.from(player.querySelectorAll(".album-track"));
    if (!audio || !tracks.length) return;

    let currentIndex = Math.max(0, tracks.findIndex((track) => track.classList.contains("is-active")));

    function labelFor(index) {
      const track = tracks[index];
      const number = track?.querySelector(".track-number")?.textContent?.trim() || String(index + 1).padStart(2, "0");
      const title = track?.dataset.title || "";
      return `${number} / ${title}`;
    }

    function syncState() {
      tracks.forEach((track, index) => {
        const button = track.querySelector(".track-play");
        const isActive = index === currentIndex;
        const isPlaying = isActive && !audio.paused;

        track.classList.toggle("is-active", isActive);
        track.classList.toggle("is-playing", isPlaying);

        if (button) {
          button.textContent = isPlaying ? "❚❚" : "▶";
          button.setAttribute("aria-label", `${track.dataset.title || "track"}を${isPlaying ? "一時停止" : "再生"}`);
        }
      });

      if (currentTitle) currentTitle.textContent = labelFor(currentIndex);
    }

    function loadTrack(index, autoplay) {
      const track = tracks[index];
      if (!track) return;

      currentIndex = index;
      if (audio.getAttribute("src") !== track.dataset.src) {
        audio.setAttribute("src", track.dataset.src);
        audio.load();
      }
      syncState();

      if (autoplay) {
        audio.play().catch(() => {
          syncState();
        });
      }
    }

    tracks.forEach((track, index) => {
      const button = track.querySelector(".track-play");
      button?.addEventListener("click", () => {
        if (index === currentIndex && !audio.paused) {
          audio.pause();
          syncState();
          return;
        }

        if (index === currentIndex && audio.paused) {
          audio.play().catch(() => {
            syncState();
          });
          return;
        }

        loadTrack(index, true);
      });
    });

    audio.addEventListener("play", syncState);
    audio.addEventListener("pause", syncState);
    audio.addEventListener("ended", () => {
      const nextIndex = currentIndex + 1;
      if (nextIndex < tracks.length) {
        loadTrack(nextIndex, true);
      } else {
        syncState();
      }
    });

    loadTrack(currentIndex, false);
  });
})();
