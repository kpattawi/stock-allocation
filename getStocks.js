var addStockButton = document.querySelector('.container #add-stock .btn');


var form = document.querySelector('#stock-form');
var stockList = document.querySelector('#stocks')
var quantityList = document.querySelector('#quantities')


form.addEventListener('submit', addStockItem);

function addStockItem(e){
    e.preventDefault();
    console.log(1);

    // Get input values
    var newTicker = document.querySelector('#ticker-input').value;
    var newQuantity = document.querySelector('#quantity-input').value;

    // Create new li elements
    var li = document.createElement('li');
    var ticker = document.createElement('span');
    var quantity = document.createElement('span');

    // Add class
    li.className = 'stocks';

    // Add text node with input value
    ticker.appendChild(document.createTextNode(newTicker));
    quantity.appendChild(document.createTextNode(newQuantity));

    // Add delete button
    var delButton = document.createElement('button');
    delButton.appendChild(document.createTextNode('X'));

    li.appendChild(ticker);
    li.appendChild(quantity);
    li.appendChild(delButton);

    stockList.appendChild(li);

}

function runEvent(e){
    e.preventDefault();
    console.log('EVENT TYPE: '+e.type);
    document.getElementById('')

    // console.log(e.target.value);
    // document.querySelector('#portfolio ul').innerHTML = '<h3>'+e.target.value+'</h3>';
}
