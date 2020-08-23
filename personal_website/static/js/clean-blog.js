// open external links in new tab
// https://stackoverflow.com/a/4425214
$(document.links).filter(function() {
  return this.hostname != window.location.hostname;
}).attr('target', '_blank')