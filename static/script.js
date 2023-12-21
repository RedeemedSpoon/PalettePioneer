document.addEventListener("DOMContentLoaded", function () {
   document.getElementById("imagecontainer").addEventListener("click", function () {
      document.getElementById("imageinput").click();
   });

   document.getElementById("importbutton").addEventListener("click", function () {
      document.getElementById("imageinput").click();
   });

   document.getElementById("imageinput").addEventListener("change", function () {
      if (this.files?.[0]) {
         document.getElementById("uploadForm").submit();
      }
   });
});
