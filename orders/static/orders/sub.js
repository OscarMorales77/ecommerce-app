//Handles the JS logic for the sub page
document.addEventListener('DOMContentLoaded', () => {
    let orderType = document.querySelector('#orderType').innerText;
    let id = null;
    let extra = null;
    document.querySelectorAll('.btn-outline-dark').forEach((button) => {
        button.onclick = () => {
            //get the unique price model id to send to server
            id = button.dataset.id
            //reset the extra cheese selection option to the default value
            document.querySelector('.custom-select').selectedIndex = 0;
            $('#exampleModalCenter').modal('show');
        };
    });
    //when the modal is close send an ajax request to the server with the selected price mdodel
    $('#exampleModalCenter').on('hidden.bs.modal', function () {
        let e = document.querySelector(".custom-select");
        extra = e.options[e.selectedIndex].value;
        var token = document.querySelector('input[name=csrfmiddlewaretoken]').value;
        $.ajax({
            type: 'POST',
            url: '/private',
            data: { 'csrfmiddlewaretoken': token, 'orderType': orderType, 'id': id, "extra": extra },
        });


    });

});