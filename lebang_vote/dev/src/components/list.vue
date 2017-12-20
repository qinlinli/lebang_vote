<template>
  <main>
    <header-bar :title="header.title" :closeWindow="header.closeWindow"></header-bar>
    <ul class="list bg-white border-bottom">
      <li class="border-top" v-for="(item, index) in list" :key="index">
        <router-link tag="a" :to="{ path: '/vote/detail/' + item.id }" class="arrow-right">{{ item.title }}</router-link>
      </li>
    </ul>
  </main>
</template>

<script>
import headerBar from './partials/header'
export default {
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
    this.$axios.get('/game/api/games/?format=json').then(res => {
      this.list = res.data
    })
  }
}
</script>

<style scoped>
</style>
