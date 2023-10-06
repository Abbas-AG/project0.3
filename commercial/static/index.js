document.addEventListener("DOMContentLoaded",  ()=> {

//   footer code 
  const footer = document.querySelector('#footer');
  window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      const windowHeight = window.innerHeight;
      const documentHeight = document.documentElement.scrollHeight;
  
     
      const distanceFromBottom = documentHeight - (scrollY + windowHeight);
  
     
      if (distanceFromBottom < 100) { 
          footer.style.bottom = '0';
      } else {
          footer.style.bottom = '-100px';
      }
  });
  

 //  input code
 const quantityInput = document.getElementById('quantity');

 quantityInput.addEventListener('input', () => {
   if (quantityInput.value < 0) {
     quantityInput.value = 0;
   }
 });


 const secondQuantityInput = document.getElementById('second-quantity');

 secondQuantityInput.addEventListener('input', () => {
   if (secondQuantityInput.value < 0) {
     secondQuantityInput.value = 0;
   }
 });
 
});

