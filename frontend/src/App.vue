<script setup>
import HelloWorld from './components/HelloWorld.vue'
import YieldCurve from './components/YieldCurve.vue'
</script>

<template>
  <header class="bg-gray-900 text-white shadow-md">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
      <h1 class="text-xl font-bold tracking-wide">📊 Rates Dashboard</h1>
      <nav class="space-x-4">
        <router-link to="/" class="nav-link">
          Home
        </router-link>
        <router-link to="/yc_view" class="nav-link">
          Yield Curve
        </router-link>
        <router-link to="/crypto_view" class="nav-link">
          Crypto Market
        </router-link>
      </nav>
    </div>
    <router-view></router-view>
  </header>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.nav-link {
  padding: 0.5rem 0.75rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
  transition: background-color 0.2s ease;
}
.nav-link:hover {
  background-color: #4b5563; /* Tailwind's gray-700 */
}
</style>
