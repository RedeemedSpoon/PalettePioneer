document.addEventListener("DOMContentLoaded", function () {
   const imageInput = document.getElementById("imageinput");
   const importButton = document.getElementById("importbutton");
   const loadingModal = document.getElementById("loadingmodal");
   const dotsElement = document.getElementById("dots");

   document.getElementById("imagecontainer").addEventListener("click", function () {
      imageInput.click();
   });

   importButton.addEventListener("click", function () {
      imageInput.click();
   });

   imageInput.addEventListener("change", function () {
      if (this.files?.[0]) {
         showLoadingModal();

         const formData = new FormData();
         formData.append("imageinput", this.files[0]);

         fetch("/results", {
            method: "POST",
            body: formData,
         })
            .then((response) => response.text())
            .then((html) => {
               document.body.innerHTML = html;
               hideLoadingModal();
            });
      }
   });

   function showLoadingModal() {
      loadingModal.style.display = "block";
      startLoadingAnimation();
   }

   function hideLoadingModal() {
      loadingModal.style.display = "none";
   }

   function startLoadingAnimation() {
      let counter = 1;

      function animateDots() {
         dotsElement.textContent += ".";
         counter++;
         if (counter > 5) {
            counter = 1;
            dotsElement.textContent = "";
         }
         setTimeout(animateDots, 750);
      }
      animateDots();
   }
});
