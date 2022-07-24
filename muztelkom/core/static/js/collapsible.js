let coll = document.getElementsByClassName("collapsible");
let i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
  this.classList.toggle("activeArticle");
  let content = this.nextElementSibling;
  content.style.maxHeight ? content.style.maxHeight = null : content.style.maxHeight = content.scrollHeight + "px";
});
}