var items = document.getElementsByClassName("style-scope ytd-playlist-video-renderer");
function deleteWL(i) {
    setInterval(function () {
        items[i].click();
        document.getElementsByClassName("style-scope ytd-menu-popup-renderer")[0].click
    }, 500);
}
for (var i = 0; i < items.length; ++i)
    deleteWL(i);