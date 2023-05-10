import Vue from 'vue'
import VueRouter from 'vue-router'
import lunchMenu from '../views/lunchMenu.vue'
import lottoPick from '../views/lottoPick.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'lunch',
    component: lunchMenu
  },
  {
    path: '/lotto/',
    name: 'lotto',
    component: lottoPick
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
