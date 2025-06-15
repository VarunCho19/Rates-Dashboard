<script setup>
import YieldCurve from '../components/YieldCurve.vue'
</script>

<template>
  <p class="text-gray-600 mb-4">This view displays the yield curve data fetched from the backend.</p>
  <div class="yc-view">
    <h1 class="text-2xl font-bold mb-4">Yield Curve View</h1>
    <YieldCurve />
  </div>
</template>
<style scoped>
</style>