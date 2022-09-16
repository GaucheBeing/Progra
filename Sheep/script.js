document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener("click", () => {
      const accordionContent = button.nextElementSibling;
      button.classList.toggle("accordion-button.active");
      if (button.classList.contains("accordion-button.active")) {
        accordionContent.style.maxheight = accordionContent.scrollHeight + "px";
      } else {
        accordionContent.style.maxheight = 0;
      }
    });
  });
var buttonActive = document.querySelectorAll()
function resetButton() {
    
}