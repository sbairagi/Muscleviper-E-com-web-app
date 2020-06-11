
console.log('working')

function incressqty_to_cart(pid, pname, price, pimg){

     //cart is alrady present
     let pcart = JSON.parse(localStorage.getItem('cart'));

     let oldProduct = pcart.find((item) => item.productId==pid)
     if (oldProduct){
             //we have to decreases the qty
            //  console.log(oldProduct.productQuentity)
             
                oldProduct.productQuentity -= 1
                pcart.map((item)=>{
                    if (item.productId==oldProduct.productId){
                        item.productQuentity = oldProduct.productQuentity;
                    }
                });
                localStorage.setItem('cart', JSON.stringify(pcart));
                $('#qty').html(oldProduct.productQuentity);
                $('#cartdetail').html('product quantity is decreases in your cart product quantity is ' + oldProduct.productQuentity + '.<br> your cart is ready to checkout !!');
                $('#qty1').html(oldProduct.productQuentity + ' Qty');
                console.log('product qty is decreases')
                
                if (oldProduct.productQuentity==0){
                    deleteItemFromCart(oldProduct.productId);
                }

             


     }
     else{
             //we have to add the product
             console.log('product is not added in your cart')


     }
     updateCart()


}






function add_to_cart(pid, pname, price, pimg){

    let cart = localStorage.getItem('cart')
    if (cart == null){
        //no cart yet
        let products = [];
        let product = {productId:pid, productName:pname, productPrice:price, productQuentity:1, productImage:pimg};
        products.push(product);
        localStorage.setItem('cart', JSON.stringify(products));
        $('#qty').html(product.productQuentity);
        $('#qty1').html(product.productQuentity + ' Qty');
        $('#cartdetail').html('product is added to your cart product quantity is ' + product.productQuentity + '.<br> your cart is ready to checkout !!');
        console.log('product is added for the first time')
    }
    else{
        //cart is alrady present
        let pcart = JSON.parse(cart);

        let oldProduct = pcart.find((item) => item.productId==pid)
        if (oldProduct){
                //we have to increase the qty
                oldProduct.productQuentity += 1
                pcart.map((item)=>{
                    if (item.productId==oldProduct.productId){
                        item.productQuentity = oldProduct.productQuentity;
                    }
                });
                localStorage.setItem('cart', JSON.stringify(pcart));
                $('#qty').html(oldProduct.productQuentity);
                $('#cartdetail').html('product is added to your cart product quantity is ' + oldProduct.productQuentity + '.<br> your cart is ready to checkout !!');
                $('#qty1').html(oldProduct.productQuentity + ' Qty');
                console.log('product qty is increased')


        }
        else{
                //we have to add the product
                let product = {productId:pid, productName:pname, productPrice:price, productQuentity:1, productImage:pimg};
                pcart.push(product)
                localStorage.setItem('cart', JSON.stringify(pcart));
                $('#qty').html(product.productQuentity);
                $('#qty1').html(product.productQuentity + ' Qty');
                $('#cartdetail').html('product is added to your cart product quantity is ' + product.productQuentity + '.<br> your cart is ready to checkout !!');

                console.log('product is added')


        }
    }
    
updateCart()

    
}

//update cart

function updateCart(){
    let cartstring = localStorage.getItem('cart');
    let cart = JSON.parse(cartstring);
    if (cart==null || cart.length==0){
        console.log('cart is empty');
        $('#cartdetail').html('no product in your cart. <br> cart is empty !!');
        $('.cart-items').html(' 0 ');
        $('.cart-body').html('<h3>cart does not have any items </h3>');
        $('.checkout-btn').addClass('disabled');

    }
    else{
        console.log(cart)
        
        

        let product = `
                        <div>  
        
        
        
        
        `;


        let totalPrice = 0
        let qty = 0

        cart.map((item)=>{
            
            product+=`
            <div class="lg:w-1/0 mt-2 md:w-1/2 p-4 w-full rounded border-2">
        <a class="block relative h-48 rounded overflow-hidden" href="../product-view-page/${item.productId}">
          <img alt="ecommerce" class="object-cover object-center w-100 block" src="${item.productImage}">
        </a>
        <div class="mt-4">
          <h6 class="text-gray-900 title-font  font-medium">${item.productName}</h6>
            <span class="title-font font-medium  text-gray-900" id="price">Price :- &#8377; ${item.productPrice}/-</span><br><h2 class="text-gray-900 title-font  font-medium">Quantity :- ${item.productQuentity}</h2>
            <span class="title-font font-medium  text-gray-900" id="price"> Total Price &#8377; ${item.productPrice*item.productQuentity}/-</span>
            <button onclick="deleteItemFromCart(${item.productId})" class=" m-2 btn-xs text-white text-center bg-indigo-500 border-0 py-2  focus:outline-none hover:bg-indigo-600 rounded text-lg">Remove Item</button>
        </div>
      </div>
        
            
            `

            totalPrice += item.productPrice * item.productQuentity;
            qty += item.productQuentity
        });

        product = product+`
        </div> 
        <div class="m-10"><b class="mb-24 text-2xl"> Total Price : ${totalPrice}/-</b></div>
        
        `
        $('.cart-body').html(product)
        $('.cart-items').html(`${qty}`);

    }
}


function deleteItemFromCart(pid){
        let cart = JSON.parse(localStorage.getItem('cart'));

        let newcart = cart.filter((item) => item.productId != pid)

        localStorage.setItem('cart',JSON.stringify(newcart))

        updateCart()
}


$(document).ready(function(){
    updateCart()
});



// $(document).ready(function () {


//     let qty = 0
//     var cart = {qty : 0}

//     $('#addtocart').click(function () {
//         cart[qty] +=1
//         $("#addtocart").replaceWith(`<button id="plus" class="flex btn-sm m-1 ml-auto text-white bg-indigo-500 border-0 py-2 focus:outline-none hover:bg-indigo-600 rounded">+</button> <span id='qty' class='text-capitalize ml-4 mt-2 text-center'>${qty} qty</span> <button id="minus" class="flex btn-sm ml-auto text-white bg-indigo-500 border-0 py-2 m-1 focus:outline-none hover:bg-indigo-600 rounded">-</button>`);
        
//         $('#plus').click(function () {
//             cart[qty] +=  1;
//             document.getElementById('qty').innerText = `${qty} qty`
//             console.log(cart.qty)
            
//         });


//         $('#minus').click(function () {
//             if (qty>=1) {
//                 cart[qty] -=  1;
//                 document.getElementById('qty').innerText = `${qty} qty`
//                 console.log(cart.qty)
                
//             }
            
//             else {
//                 console.log('qty is 0')
//             }
//         });


        

//     });

    

// });

