import Vue from 'vue'
import Router from 'vue-router'
import VoteList from '@/components/list'
import Vote from '@/components/vote'
import VoteDetail from '@/components/detail'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/vote',
      name: 'VoteList',
      component: VoteList
    },
    {
      path: '/vote/:id',
      name: 'Vote',
      component: Vote
    },
    {
      path: '/vote/detail/:id',
      name: 'VoteDetail',
      component: VoteDetail
    }
  ]
})
