import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import HappeedView from '../views/HappeedView.vue'
import HapplingView from '../views/HapplingView.vue'
import HapplossomeView from '../views/HapplossomeView.vue'
import HapplowerView from '../views/HapplowerView.vue'
import ErrorView from '../views/ErrorView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/happeed',
    name: 'HappeedView',
    component: HappeedView
  },
  {
    path: '/happling',
    name: 'HapplingView',
    component: HapplingView
  },
  {
    path: '/happlossome',
    name: 'HapplossomeView',
    component: HapplossomeView
  },
  {
    path: '/happlower',
    name: 'HapplowerView',
    component: HapplowerView
  },
  {
    path: '*',
    name: 'ErrorView',
    component: ErrorView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
