//handles all the JS logic for the pizza html file
document.addEventListener('DOMContentLoaded', () => {
    let numInput = null;
    let pizzaID = null;
    document.querySelectorAll('.btn-outline-dark').forEach((button) => {
        //if the selected item does not have toppings don't open the modal
        if (button.dataset.toppings != 0) {
            button.onclick = () => {
                document.querySelector('.modal-body').innerHTML = ""; //clear modal content when a different item is selected
                numInput = button.dataset.toppings; //get the number of toppings
                pizzaID = button.dataset.id;//unique id to be used by server

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

        } else {
            button.onclick = () => {
                const toppings = []
                pizzaID = button.dataset.id;
                var token = document.querySelector('input[name=csrfmiddlewaretoken]').value;
                //send price modal id to server when user clicks on button with no toppings
                $.ajax({
                    type: 'POST',
                    url: '/private',
                    data: { 'csrfmiddlewaretoken': token, 'toppings[]': toppings, 'orderType': 'Pizza', 'id': pizzaID },
                });

            }

        }

    });

    //When the modal is closed, send a ajax request to the server 
    $('#exampleModalCenter').on('hidden.bs.modal', function () {

        const toppings = []
        // select all elements and grab the value (toppings)
        document.querySelectorAll('.custom-select').forEach((e) => {
            toppings.push(e.options[e.selectedIndex].value);
        });

        var token = document.querySelector('input[name=csrfmiddlewaretoken]').value;
        $.ajax({
            type: 'POST',
            url: '/private',
            data: { 'csrfmiddlewaretoken': token, 'toppings[]': toppings, 'orderType': 'Pizza', 'id': pizzaID },
        });


    });

});

