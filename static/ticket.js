let copyText = document.querySelector(".copy-text");
copyText.querySelector("button").addEventListener("click", function () {
  let input = copyText.querySelector("input.text");
  input.select();
  document.execCommand("copy");
  copyText.classList.add("active");
  window.getSelection().removeAllRanges();
  setTimeout(function () {
    copyText.classList.remove("active");
  }, 2500);
});
const openButton = document.getElementById("button");
const closeButton = document.getElementById("close-button");
const modalContainer = document.querySelector(".modal-container");

const targetList = [openButton, closeButton, modalContainer];

const handler = (e) => {
  e.stopPropagation();

  if (targetList.includes(e.target)) {
    modalContainer.classList.toggle("active");
  }
};

targetList.forEach((el) => el.addEventListener("click", handler));
