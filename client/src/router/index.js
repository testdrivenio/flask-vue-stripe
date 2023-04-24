import { createRouter, createWebHistory } from 'vue-router'
import Books from '../components/Books.vue'
import OrderCanceled from '../components/OrderCanceled.vue'
import OrderSuccess from '../components/OrderSuccess.vue'
import Ping from '../components/Ping.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/success',
      name: 'OrderSuccess',
      component: OrderSuccess,
    },
    {
      path: '/canceled',
      name: 'OrderCanceled',
      component: OrderCanceled,
    },
  ]
})

export default router
