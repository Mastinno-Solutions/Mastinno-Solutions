function formatCurrency(value) {
  return "₹" + value.toFixed(2);
}

function calculateTotal() {
  let subtotal = 0;
  const discount = 50; 
  const taxRate = 0.05; 

  document.querySelectorAll('.item-total').forEach(item => {
      const price = parseFloat(item.getAttribute('data-price')) || 0;
      const quantity = parseInt(item.getAttribute('data-quantity')) || 0;
      const itemTotal = price * quantity;
      item.textContent = formatCurrency(itemTotal);
      subtotal += itemTotal;
  });

  let tax = subtotal * taxRate;
  let finalTotal = subtotal + tax - discount;

  document.getElementById('subtotal').textContent = formatCurrency(subtotal);
  document.getElementById('tax').textContent = formatCurrency(tax);
  document.getElementById('total').textContent = formatCurrency(finalTotal);
}

document.addEventListener('DOMContentLoaded', calculateTotal);