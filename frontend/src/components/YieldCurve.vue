<template>
  <div class="p-4">
    <h2 class="text-xl font-bold mb-4">U.S. Treasury Yield Curve</h2>
    <Line v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>Loading...</p>
  </div>
</template>

<script setup>
console.log('YieldCurve component loaded');
import { ref, onMounted } from 'vue';
import { Line } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js';

ChartJS.register(Title, Tooltip, Legend, LineElement,CategoryScale, PointElement, LinearScale);


const chartData = ref(null)
const chartOptions = ref({
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Yield Curve',
    },
  },
});

const fetchYieldCurveData = async () => {
  try {
    console.log('Fetching yield curve data...');
    const response = await fetch('https://rates-dashboard.onrender.com/yields')
    const data = await response.json()
    console.log('Yield Curve Data Recevied:', data);

    const labels = Object.keys(data)
    const values = Object.values(data)

    chartData.value = {
      labels: labels,
      datasets: [
        {
          label: 'Yield Curve',
          backgroundColor: '#4B9CD3',
          borderColor: '#4B9CD3',
          data: values,
          fill: false,
          tension: 0.3,
        }
      ]
    };
    console.log('Yield Curve Data:', chartData.value);

  }
    catch (error) {
        console.error('Error fetching yield curve data:', error);
    }
};

onMounted(() => {
    fetchYieldCurveData();
});
</script>

<style scoped>

</style>