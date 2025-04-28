document.addEventListener("DOMContentLoaded", async () => {
    const catalog = document.getElementById("catalog");
    const response = await fetch("https://lavandershopbot.onrender.com/products");
    const products = await response.json();

    products.forEach(product => {
        catalog.innerHTML += `
            <div class="product-card">
                <img src="${product.photo_url}" alt="${product.name}">
                <h3>${product.name}</h3>
                <p>${product.description}</p>
                <span>${product.price} ₽</span>
            </div>
        `;
    });
});