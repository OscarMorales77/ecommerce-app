document.addEventListener('DOMContentLoaded',() => {
    let orderType=document.querySelector('#orderType').innerText;
    let id=null;
    let extra=null;
      document.querySelectorAll('.btn-outline-dark').forEach((button) => {
          console.log("array of buttons created")
          button.onclick = () => {
              id=button.dataset.id
            $('#exampleModalCenter').modal('show');
          };
      });

      $('#exampleModalCenter').on('hidden.bs.modal', function () {
       let e= document.querySelector(".custom-select");
        extra=e.options[e.selectedIndex].value;
        console.log(extra);
        console.log(orderType);
        console.log(id);
        var token=document.querySelector('input[name=csrfmiddlewaretoken]').value;
        
        $.ajax({
            type: 'POST',
            url: '/private',
            data: {'csrfmiddlewaretoken':token,'orderType': orderType,'id':id,"extra":extra},
        });
        
        
    });
      
  });