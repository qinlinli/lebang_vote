<template>
  <dl class="twotabs">
    <dd class="twotabs-btn left-btn" :class="active === 'left' ? 'active' : ''" @click="leftTabClick">{{ leftBtn.text }}</dd>
    <dd class="twotabs-btn right-btn" :class="active === 'right' ? 'active' : ''" @click="rightTabClick">{{ rightBtn.text }}</dd>
    <dt class="twotabs-cursor"></dt>
  </dl>
</template>
<script>
  export default {
    props: {
      leftBtn: {
        type: Object,
        default () {
          return {
            text: ''
          }
        }
      },
      rightBtn: {
        type: Object,
        default () {
          return {
            text: ''
          }
        }
      }
    },
    data () {
      return {
        active: 'left'
      }
    },
    methods: {
      leftTabClick () {
        this.active = 'left'
        this.$emit('leftTabClick')
      },
      rightTabClick () {
        this.active = 'right'
        this.$emit('rightTabClick')
      }
    }
  }
</script>
