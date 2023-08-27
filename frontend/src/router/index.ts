// Composables
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('@/views/Home.vue')
  }, {
    path: '/add',
    component: () => import ('@/views/Add.vue')
  }, {
    path: '/query',
    component: () => import ('@/views/Query.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
