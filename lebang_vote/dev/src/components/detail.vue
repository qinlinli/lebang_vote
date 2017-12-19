<template>
  <main class="detail">
    <header-bar :title="header.title" @back="back"></header-bar>
    <div class="content">
      <ul class="statistics flex">
        <li>
          <h3>参与选手</h3>
          <em>{{ vote.voted_person }}</em>
        </li>
        <li>
          <h3>累计投票</h3>
          <em>{{ vote.voted_amount }}</em>
        </li>
        <li>
          <h3>访问次数</h3>
          <em>{{ vote.visted }}</em>
        </li>
      </ul>
      <div class="time">
        <p>开始时间：{{ vote.start }}</p>
        <p>结束时间：{{ vote.end }}</p>
      </div>
      <p v-if="vote.rule" class="rule">投票规则：{{ vote.content }}</p>
      <div v-if="vote.content" class="article">
        <button class="link arrow-bottom" @click="showContent = !showContent">活动介绍&nbsp;&nbsp;&nbsp;</button>
        <p v-show="showContent">{{ vote.content }}</p>
      </div>
      <ul class="options">
        <li v-for="(option, index) in vote.options" :key="index">
          <img v-if="option.banner" src="option.banner" />
          <span class="person">{{ index + '.' }} {{ option.content }} <a :href="option.url"></a></span>
          <button class="btn primary">投票</button>
          <em>{{ option.count_vote }}</em>
        </li>
      </ul>
    </div>
  </main>
</template>

<script>
import headerBar from './partials/header'
export default {
  name: 'detail',
  data () {
    return {
      header: {
        title: ''
      },
      showContent: false,
      vote: {}
    }
  },
  components: {
    headerBar
  },
  created () {
    this.vote = this.$router.params
    if (!this.vote) {
      let index = location.hash.indexOf('=')
      let id = location.hash.slice(index + 1)
      this.$axios.get('/game/games/?format=json').then(res => {
        let result = res.data
        result.forEach(item => {
          if (id === item.id) {
            this.vote = item
          }
          return
        })
        this.header.title = this.vote.title
      })
    }
  },
  methods: {
    back () {
      this.$router.push({
        name: 'List'
      })
    }
  }
}
</script>

<style scoped>
  .statistics {
    background: #4DB87F;
    border-radius: .5em;
    color: #fff;
    padding: .5em 0;
  }
  .statistics li {
    text-align: center;
    line-height: 1.5;
    border-left: 1px solid #fff;
  }
  .statistics li:first-child {
    border: none;
  }
  .statistics h3 {
    text-align: center;
  }
  .statistics em {
    font-style: normal;
  }
  .time {
    margin: 1em 0;
  }
  .time  p{
    margin: .5em 0;
  }
  .rule,
  .article {
    line-height: 1.75;
    margin-bottom: 1em;
  }
  .article button {
    padding-right: 1em;
    padding-left: 0;
  }
  .article button::before {
    color: #ccc;
  }
  .options {
    margin-left: -5%;
  }
  .options li {
    float: left;
    width: 45%;
    background: #ddd;
    margin-left: 5%;
    padding: .5em 1em;
  }
  .options .person {
    display: block;
  }
  .options button {
    margin: .5em 0;
  }
  .options li em {
    display: block;
    font-style: normal;
    text-align: center;
  }
</style>
