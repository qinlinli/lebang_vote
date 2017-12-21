<template>
  <main class="vote-detail">
    <header-bar :title="header.title" @back="back"></header-bar>
    <div v-if="detail.image_url" class="banner">
      <img :src="detail.image_url" :alt="detail.title" />
    </div>
    <div class="content">
      <div v-if="detail.content" class="article">
        <h2>{{ detail.title }}</h2>
        <p v-html="detail.content"></p>
      </div>
      <div class="action">
        <button class="btn primary" :class="{ disabled: !detail.can_vote }" @click="postVote()">{{ detail.voted ? '已投票' : '投票' }}</button>
      </div>
      <ul class="statistics flex">
        <li><span>累计投票：</span><em>{{ detail.count_vote }}</em></li>
        <li><span>访问次数：</span><em>{{ detail.count_visit }}</em></li>
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
      detail: {}
    }
  },
  components: {
    headerBar
  },
  beforeRouteEnter (to, from, next) {
    next((vm) => {
      vm.setFrom(from)
    })
  },
  created () {
    this.id = this.$route.params.id
    if (this.id) {
      this.$axios.get('/game/api/options/' + this.id).then(res => {
        let result = res.data
        this.detail = result
      })
    }
  },
  methods: {
    back () {
      this.$router.replace({
        path: this.from.fullPath
      })
    },
    postVote () {
      this.$axios.post('/game/api/vote', {
        id: this.detail.id
      }).then(res => {
        if (res.data.code === 0) {
          this.$toast('投票成功！')
          this.detail.voted = true
          this.detail.count_vote++
        } else {
          this.$toast(res.data.error)
        }
      })
    },
    setFrom (value) {
      this.from = value
    }
  }
}
</script>

<style scoped>
  .statistics {
    color: #4DB87F;
    padding: .5em 0;
  }
  .statistics li {
    text-align: center;
    line-height: 1.5;
  }
  .statistics span {
    color: #333;
  }
  .statistics em {
    font-style: normal;
    font-family: Arial;
  }
  .article {
    line-height: 1.5;
    margin-bottom: 1em;
  }
  .article h2 {
    font-weight: bold;
    margin-bottom: .3em;
  }
  .action {
    margin: 1em 0;
  }
  .action button {
    line-height: 2; 
  }
  .fa {
    color: #4DB87F;
    margin-right: .5em;
  }
</style>
