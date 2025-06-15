<script setup>
import CryptoTicker from '../components/CryptoTicker.vue'
</script>
<template>
  <div class="crypto-view">
    <h1 class="text-2xl font-bold mb-4">Crypto Market</h1>
    <CryptoTicker />
    <div class="mt-8">
      <p class="text-gray-600">Live updates for BTC-USD</p>
      <p class="text-gray-600 mt-2">Powered by Coinbase WebSocket API</p>
    </div>
  </div>
</template>
<style scoped>
</style>