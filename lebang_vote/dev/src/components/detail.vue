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
          <em>{{ vote.visited }}</em>
        </li>
      </ul>
      <div class="time">
        <p><i class="fa fa-clock-o"></i>开始时间：{{ vote.start ? formatDate(vote.start) : '' }}</p>
        <p><i class="fa fa-clock-o"></i>结束时间：{{ vote.end ? formatDate(vote.end) : '' }}</p>
      </div>
      <p v-if="vote.rule" class="rule"><i class="fa fa-warning-o"></i>投票规则：{{ vote.content }}</p>
      <div v-if="vote.content" class="article">
        <button class="link arrow-bottom" @click="showContent = !showContent"><i class="fa fa-list-alt"></i>活动介绍&nbsp;&nbsp;&nbsp;</button>
        <p v-show="showContent">{{ vote.content }}</p>
      </div>
      <ul class="options flex">
        <li v-for="(option, index) in vote.options" :key="index">
          <img v-if="option.banner" src="option.banner" />
          <span class="person">{{ ++index + '.' }} {{ option.content }} <a :href="option.url"></a></span>
          <button class="btn primary" :class="{ disabled: !option.can_vote }" @click="postVote(option)">{{ option.voted ? '已投票' : '投票' }}</button>
          <em>{{ option.count_vote }}</em>
        </li>
      </ul>
    </div>
  </main>
</template>

<script>
import headerBar from './partials/header'
export default {
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
    this.id = this.$route.params.id
    if (this.id) {
      this.$axios.get('/game/api/games/' + this.id).then(res => {
        let result = res.data
        this.vote = result
        this.header.title = this.vote.title
      })
    }
  },
  methods: {
    back () {
      this.$router.replace({
        name: 'VoteList'
      })
    },
    postVote (option) {
      this.$axios.post('/game/api/vote', {
        id: option.id
      }).then(res => {
        if (res.data.code === 0) {
          this.$toast('投票成功！')
          option.voted = true
          option.count_vote++
          this.vote.voted_amount++
        } else {
          this.$toast(res.data.error)
        }
      })
    },
    formatDate (string) {
      return string.replace(/[T|Z]/g, ' ')
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
    line-height: 1.5;
    margin-bottom: 1em;
  }
  .article button {
    padding-right: .8em;
    padding-left: 0;
  }
  .article button::before {
    margin-top: -.5em;
    color: #bbb;
  }
  .options {
    flex-wrap: wrap;
    align-items: flex-start;
    margin-left: -5%;
  }
  .options li {
    flex-basis: 45%;
    background: #fff;
    border: 1px solid #4DB87F;
    margin-left: 5%;
    margin-bottom: .5em;
    border-radius: .3em;
    padding: .8em .6em;
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
  .fa {
    color: #4DB87F;
    margin-right: .5em;
  }
</style>
