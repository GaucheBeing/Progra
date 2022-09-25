// document.querySelectorAll('.accordion-button').forEach(button => {
//     button.addEventListener("click", () => {
//        const accordionContent = button.nextElementSibling;
//       button.classList.toggle("accordion-button:focus");
//       if (button.classList.contains("accordion-button:focus")) {
//         accordionContent.style.maxheight = accordionContent.scrollHeight + "px";
//       } else {
//         accordionContent.style.maxheight = 0;
//       }
//     });
//   });


// var buttonActive = document.querySelectorAll('.accordion-button');
// buttonActive.forEach(button => {
//     button.addEventListener("click", () => {
//         resetButton();
//         button.classList.add("accordion-button:focus");
//     })
// })
// function resetButton() {
//     buttonActive.forEach(button => {
//         button.classList.remove("accordion-button:active")
//     })
// }

// var allCollapsibles = document.querySelectorAll('.accordion-button');
// allCollapsibles.forEach(item => {
//   item.addEventListener("click", function() {
//      if(this.nextElementSibling.classList.contains('active')) {
//        this.nextElementSibling.classList.remove('active')
//      } else {
//        this.nextElementSibling.classList.add('active')
//      }
//   });
// });