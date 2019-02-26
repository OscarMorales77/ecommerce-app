document.addEventListener('DOMContentLoaded', () => {
    // $('#exampleModalCenter').modal('show');
    let numInput=null;
    let pizzaID=null;
    document.querySelectorAll('.btn-outline-dark').forEach((button) => {
        console.log("array of buttons created");
        button.onclick = () => {
            document.querySelector('.modal-body').innerHTML=""; //clear content when a different item is selected
             numInput = button.dataset.toppings; //get the number of toppings
             pizzaID=button.dataset.id;
    
            // Use handlebars template system to dynamically generate input fields
            const post_template = Handlebars.compile(document.querySelector('#inputTemplate').innerHTML);
            const post = post_template();
            //add the select option elements into the body of the html
            for (let i = 0; i < numInput; i++) {
                document.querySelector('.modal-body').innerHTML += post;
            }
            //show the modal
            $('#exampleModalCenter').modal('show');

        };
    });

    //jquery- when the modal is closed
    $('#exampleModalCenter').on('hidden.bs.modal', function () {
        // select all 'select' elements and grab the value
        console.log("#toppings is"+numInput+"  and unique id "+pizzaID);
        const toppings=[]
        document.querySelectorAll('.custom-select').forEach((e) => {
            toppings.push(e.options[e.selectedIndex].value);
            //console.log( e.options[e.selectedIndex].value);
        });
        /*
        const request = new XMLHttpRequest();
        request.open('POST', '/private');
        const data = new FormData();
        data.append('orderType', 'Pizza'); //tell the server what type of order is being processed
        data.append('id',pizzaID); //get the unique id price order to look-up in the database
        //send the required CSRF token, can also be implemented via cookie and @ensure_csrf_cookie decorator
        data.append('csrfmiddlewaretoken',document.querySelector('input[name=csrfmiddlewaretoken]').value);
        request.send(data);
        */
        console.log(toppings)
        var token=document.querySelector('input[name=csrfmiddlewaretoken]').value;
        $.ajax({
            type: 'POST',
            url: '/private',
            data: {'csrfmiddlewaretoken':token,'toppings[]': toppings,'orderType': 'Pizza','id':pizzaID},
        });

        
    });

});


/*
$.ajax({
    type: 'POST',
    url: '/private',
    data: {'toppings[]': toppings},
});
*/