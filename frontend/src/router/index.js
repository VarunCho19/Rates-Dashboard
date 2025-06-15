import {createRouter, createWebHistory} from 'vue-router';
import Home from '../views/Home.vue';
import YieldCurve from '../views/yc_view.vue';
import crypto_view from '../views/crypto_view.vue';


const routes = [
    {path: '/', name: 'Home', component: Home },
    {path: '/yc_view', name: 'YieldCurve', component: YieldCurve },
    {path: '/crypto_view', name: 'CryptoView', component: crypto_view }
    
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
});

export default router