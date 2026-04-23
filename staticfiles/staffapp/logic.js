
/* add product page*/

document.addEventListener("DOMContentLoaded", function () {
    const fileInputs = document.querySelectorAll("input[type='file']");
    const previewBox = document.getElementById("imgPreview");
    const previewImg = document.getElementById("previewImg");

    fileInputs.forEach(input => {
        input.addEventListener("change", function () {
            if (this.files && this.files[0]) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    previewImg.src = e.target.result;
                    previewBox.classList.remove("d-none");
                };
                reader.readAsDataURL(this.files[0]);
            }
        });
    });
});


<script>
document.addEventListener("DOMContentLoaded", function () {

    let cartData = JSON.parse(localStorage.getItem("cart")) || [];

    function saveCartData() {
        localStorage.setItem("cart", JSON.stringify(cartData));
    }

    let buttons = document.querySelectorAll(".add-to-cart");

    buttons.forEach(function (btn) {
        btn.addEventListener("click", function () {

            let id = btn.getAttribute("data-id");
            let name = btn.getAttribute("data-name");
            let price = parseInt(btn.getAttribute("data-price"));
            let image = btn.getAttribute("data-image");

            let existing = cartData.find(function (p) {
                return p.id == id;
            });

            if (existing) {
                existing.qty = existing.qty + 1;
            } else {
                cartData.push({
                    id: id,
                    name: name,
                    price: price,
                    image: image,
                    qty: 1
                });
            }

            saveCartData();

            let oldText = btn.innerText;
            btn.innerText = "Added ✔";
            setTimeout(function () {
                btn.innerText = oldText;
            }, 800);
        });
    });

});
</script>
