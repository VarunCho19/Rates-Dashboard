<script setup>
console.log('CryptoTicker component loaded');
import { ref, onMounted, reactive, onBeforeUnmount, watch } from 'vue';
 

const price = ref(null)
const bid = ref(null)
const ask = ref(null)
const priceChangeClass = ref('')

let socket = null;
let previousPrice = price.value;


onMounted(() => {
  socket = new WebSocket('wss://ws-feed.exchange.coinbase.com');
    socket.onopen = () => {
        console.log('WebSocket connection established');
        socket.send(JSON.stringify({
        type: 'subscribe',
        channels: [{ name: 'ticker', product_ids: ['BTC-USD'] }]
        }));
    };
    socket.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.type === 'ticker') {
            price.value = data.price;
            updatePrice(parseFloat(data.price));
            bid.value = data.best_bid;
            ask.value = data.best_ask;
            
        }
    };
    socket.onerror = (error) => {
        console.error('WebSocket error:', error);
    };
    socket.onclose = () => {
        console.log('WebSocket connection closed');
    };

});

onBeforeUnmount(() => {
    if (socket) {
        socket.close();
        console.log('WebSocket connection closed on component unmount');
    }
});

function updatePrice(newPrice) {
    if (newPrice > previousPrice) {
        priceChangeClass.value = 'flash-up'
    } else if (newPrice < previousPrice) {
        priceChangeClass.value = 'flash-down'
    } else {
    priceChangeClass.value = ''
    }
    previousPrice = newPrice;

    if (priceChangeClass.value) {
        setTimeout(() => {
        priceChangeClass.value = ''
        }, 500) // duration must match animation time
    }

};
</script>

<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
        <div class="text-center mb-8">
            <h1 class="text-3xl font-bold mb-4">Crypto Ticker</h1>
            <p class="text-gray-700">Live updates for BTC-USD</p>
        </div>
    </div>
    <div class="p-4 text-white bg-gray-900 rounded shadow-md w-72 font-mono">
        <h2 class="text-xl font-semibold mb-3">BTC-USD Live Ticker</h2>
        <p v-if="price" :class="priceChangeClass" class="price"> <strong>Price:</strong> ${{ parseFloat(price).toFixed(2) }}</p>
        <p v-if="bid"> <strong>Bid:</strong> ${{ parseFloat(bid).toFixed(2) }}</p>
        <p v-if="ask"> <strong>Ask:</strong> ${{ parseFloat(ask).toFixed(2) }}</p>
    <p v-if="!price">Connecting...</p>
  </div>
</template>

<style scoped>
.price {
  font-size: 2rem;
  font-weight: bold;
  transition: color 0.3s ease;
}

.flash-up {
  color: #4caf50;
  animation: flashGreen 0.3s;
}

.flash-down {
  color: #f44336;
  animation: flashRed 0.3s;
}

@keyframes flashGreen {
  0% { color: #4caf50; }
  50% { color: white; }
  100% { color: #4caf50; }
}

@keyframes flashRed {
  0% { color: #f44336; }
  50% { color: white; }
  100% { color: #f44336; }
}

</style>