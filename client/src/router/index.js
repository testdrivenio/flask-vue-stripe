import Vue from 'vue';
import Router from 'vue-router';
import Books from '../components/Books.vue';
import OrderCanceled from '../components/OrderCanceled.vue';
import OrderSuccess from '../components/OrderSuccess.vue';
import Ping from '../components/Ping.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
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
  ],
});
