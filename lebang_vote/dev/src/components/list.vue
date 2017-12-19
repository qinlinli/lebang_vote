<template>
  <main>
    <header-bar :title="header.title" :closeWindow="header.closeWindow"></header-bar>
    <ul class="list bg-white border-bottom">
      <li class="border-top" v-for="(item, index) in list" :key="index">
        <router-link tag="a" :to="{ path: '/detail', query: {id: item.id}, params: {vote: item} }" class="arrow-right">{{ item.title }}</router-link>
      </li>
    </ul>
  </main>
</template>

<script>
import headerBar from './partials/header'
export default {
  name: 'list',
  data () {
    return {
      header: {
        title: '乐帮投票',
        closeWindow: true
      },
      list: []
    }
  },
  components: {
    headerBar
  },
  created () {
    this.$axios.get('/game/games/?format=json').then(res => {
      this.list = res.data
    })
  }
}
</script>

<style scoped>
</style>
