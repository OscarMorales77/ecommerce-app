document.addEventListener('DOMContentLoaded',() => {
    let totalPrice=0;
    document.querySelector("#confirm").onclick=() => {
        $('#shoppinModal').modal('show');
    };
    document.querySelectorAll('.btn-outline-dark').forEach((button) => {
        totalPrice+=Number(button.dataset.price);   
        console.log("array of buttons created")
        button.onclick = () => {
            const request = new XMLHttpRequest();
            request.open('POST', '/remove');
            const data = new FormData();
            data.append('orderType', button.dataset.type); 
            data.append('id',button.dataset.id); 
            data.append('csrfmiddlewaretoken',document.querySelector('input[name=csrfmiddlewaretoken]').value);
            request.send(data);
            totalPrice-=button.dataset.price;
            totalPrice=Math.round(totalPrice * 1000) / 1000;
            document.querySelector("#cartTotal").innerHTML= `$${totalPrice.toFixed(2)}`; 
            button.parentNode.parentNode.remove();// remove element from page
        };
    });
    totalPrice=Math.round(totalPrice * 1000) / 1000;
    document.querySelector("#cartTotal").innerHTML= `$${totalPrice.toFixed(2)}`;  //template literals

});