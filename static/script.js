document.getElementById("imagecontainer").addEventListener("click", function () {
   document.getElementById("imageinput").click();
});

document.getElementById("imageinput").addEventListener("change", function (e) {
   const file = e.target.files[0];
   if (file) {
      const reader = new FileReader();
      reader.onload = function (event) {
         document.getElementById("previewimage").src = event.target.result;
         document.getElementById("importbutton").style.display = "block";
      };
      reader.readAsDataURL(file);
   }
});
