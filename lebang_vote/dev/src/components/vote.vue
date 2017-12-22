<template>
  <main class="vote">
    <header-bar :title="header.title" @back="back"></header-bar>
    <div class="content">
      <ul class="statistics flex">
        <li>
          <h3>参与选手</h3>
          <em>{{ vote.options ? vote.options.length : 0 }}</em>
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
        <div v-show="showContent">
          <h2>{{ vote.title }}</h2>
          <p class="vote-content" v-html="vote.content"></p>
        </div>
      </div>
      <ul class="options flex">
        <router-link tag="li" :to="{ path: '/vote/detail/' + option.id}" v-for="(option, index) in vote.options" :key="index">
          <img v-if="option.image_url" :src="option.image_url" />
          <span ref="detail" class="desc">{{ ++index + '.' }} {{ shrinkText(option.title) }}</span>
          <button class="btn primary" :class="{ disabled: !option.can_vote }" @click="postVote($event, option)">{{ option.voted ? '已投票' : '投票' }}</button>
          <em>{{ option.count_vote }}</em>
        </router-link>
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
        title: '乐帮投票'
      },
      showContent: true,
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
      })
    }
  },
  methods: {
    back () {
      this.$router.replace({
        name: 'VoteList'
      })
    },
    postVote (e, option) {
      e.cancelBubble = true
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
    },
    shrinkText (content) {
      if (content && content.length > 14) {
        content = content.slice(0, 14) + '...'
      }
      return content
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
  .article h2 {
    font-weight: bold;
    margin-bottom: .3em;
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
    padding: .5em .6em .8em;
  }
  .options .desc {
    display: block;
    font-size: 90%;
  }
  .options button {
    margin: .5em 0;
  }
  .options li img {
    margin-bottom: .5em;
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
