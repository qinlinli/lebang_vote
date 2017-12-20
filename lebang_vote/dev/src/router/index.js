import Vue from 'vue'
import Router from 'vue-router'
import VoteList from '@/components/list'
import VoteDetail from '@/components/detail'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/vote',
      name: 'VoteList',
      component: VoteList
    },
    {
      path: '/vote/detail/:id',
      name: 'VoteDetail',
      component: VoteDetail
    }
  ]
})
