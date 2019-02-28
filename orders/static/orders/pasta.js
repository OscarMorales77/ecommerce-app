document.addEventListener('DOMContentLoaded',() => {
  //document.querySelector('#orderType').innerText;
    console.log("dom loaded")
    document.querySelectorAll('.btn-outline-dark').forEach((button) => {
        console.log("array of buttons created")
        button.onclick = () => {
            const request = new XMLHttpRequest();
            request.open('POST', '/private');
            const data = new FormData();
            data.append('orderType', 'pasta'); //tell the server what type of order is being processed
            data.append('id',button.dataset.id); //get the unique id price order to look-up in the database
            //send the required CSRF token, can also be implemented via cookie and @ensure_csrf_cookie decorator
            data.append('csrfmiddlewaretoken',document.querySelector('input[name=csrfmiddlewaretoken]').value);
            request.send(data);
            console.log("it worked!?")
        };
    });
    
});