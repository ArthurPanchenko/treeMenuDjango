let toggler = document.getElementsByClassName("title");
for (let i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("mouseover", function() {
    this.parentElement.querySelector(".nested").classList.add("active");
  });
}