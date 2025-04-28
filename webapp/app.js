window.onload = async function() {
    const container = document.getElementById('products');
    let response = await fetch('/static/products.json');
    let products = await response.json();

    products.forEach(product => {
        let div = document.createElement('div');
        div.className = 'product';
        div.innerHTML = `<b>${product.name}</b><br>
                         Цена: ${product.price} ₽<br>
                         <i>${product.description}</i><br>
                         <button onclick="selectProduct('${product.name}')">Выбрать</button>`;
        container.appendChild(div);
    });
}

function selectProduct(name) {
    alert('Товар выбран: ' + name);
    Telegram.WebApp.close(); // закрыть приложение
}
