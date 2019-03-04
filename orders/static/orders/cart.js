document.addEventListener('DOMContentLoaded', () => {
    let totalPrice = 0;

    document.querySelectorAll('.btn-outline-dark').forEach((button) => {
        //get the current shopping cart total
        totalPrice += Number(button.dataset.price);
        //when a user deletes an item send an ajax request to remove it from DB (server side)
        button.onclick = () => {
            const request = new XMLHttpRequest();
            request.open('POST', '/remove');
            const data = new FormData();
            data.append('orderType', button.dataset.type);
            data.append('id', button.dataset.id); //unique id of order
            data.append('csrfmiddlewaretoken', document.querySelector('input[name=csrfmiddlewaretoken]').value);
            request.send(data);
            totalPrice -= button.dataset.price; //update the shopping cart total
            totalPrice = Math.round(totalPrice * 1000) / 1000;
            document.querySelector("#cartTotal").innerHTML = `$${totalPrice.toFixed(2)}`;
            button.parentNode.parentNode.remove();// remove element from page
        };
    });
    
    totalPrice = Math.round(totalPrice * 1000) / 1000;
    document.querySelector("#cartTotal").innerHTML = `$${totalPrice.toFixed(2)}`;
});