document.addEventListener("DOMContentLoaded", () => {

    /* ===============================
       NAVBAR ACTIVE LINK
    =============================== */
    const links = document.querySelectorAll(".nav-links .nav-link");
    const path = window.location.pathname;

    links.forEach(link => {
        const href = link.getAttribute("href");
        if (href && href !== "#" && path.includes(href)) {
            link.classList.add("active");
        }
    });


    /* ===============================
       HERO CONTENT (Home Page)
    =============================== */
    const hero = document.getElementById("heroContent");
    if (hero) {
        hero.innerHTML = `
            <h1>Discover the Best</h1>
            <h1>Smartphones</h1>
            <p>Shop Now & Save Big!</p>
            <a href="/products/" class="btn btn-success">Shop Now</a>
        `;
    }


    /* ===============================
       CONTACT FORM (Contact Page)
    =============================== */
    const form = document.getElementById("contactForm");
    const status = document.getElementById("formStatus");

    if (form && status) {
        form.addEventListener("submit", (e) => {
            e.preventDefault();
            status.textContent = "Message sent successfully! (Demo)";
            status.className = "text-success";
            form.reset();
        });
    }


    /* ===============================
       MOBILES FILTER (Mobiles Page)
    =============================== */
    const filter = document.getElementById("priceFilter");
    const items = document.querySelectorAll(".mobile-item");

    if (filter && items.length > 0) {
        filter.addEventListener("change", function () {
            const value = this.value;

            items.forEach(item => {
                const priceType = item.getAttribute("data-price");

                if (value === "all" || priceType === value) {
                    item.style.display = "";
                } else {
                    item.style.display = "none";
                }
            });
        });
    }

});


/* ===============================
   PROMO / DISCOUNT SECTION
=============================== */
document.addEventListener("DOMContentLoaded", () => {
    const promoCards = document.querySelectorAll(".promo-card");

    promoCards.forEach(card => {
        card.addEventListener("mouseenter", () => {
            card.classList.add("shadow-lg");
            card.style.transform = "scale(1.02)";
        });

        card.addEventListener("mouseleave", () => {
            card.classList.remove("shadow-lg");
            card.style.transform = "scale(1)";
        });
    });
});
/* categories */
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".add-cart-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            btn.innerText = "Added!";
            btn.classList.remove("btn-warning");
            btn.classList.add("btn-success");
        });
    });
});


/*offer*/
document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll(".offer-btn").forEach(btn => {
        btn.addEventListener("click", () => {
            btn.innerText = "Added!";
            btn.classList.remove("btn-warning");
            btn.classList.add("btn-success");
        });
    });
});

/* product details */
const img = document.getElementById("mainImage");

img.addEventListener("mouseover", () => {
    img.style.transform = "scale(1.1)";
});

img.addEventListener("mouseout", () => {
    img.style.transform = "scale(1)";
});

