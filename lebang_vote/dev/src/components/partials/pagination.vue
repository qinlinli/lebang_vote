<template>
  <div class="pagination flex">
    <a @click="prev" class="prev arrow-left solid" :class="prevBtn.disabled ? 'disabled' : '' ">{{ prevBtn.text || '&nbsp;' }}</a>
    <span class="page">{{ current }} / <span>{{ total }}</span></span>
    <a @click="next" class="next" :class="{ disabled: nextBtn.disabled, 'arrow-right': rightArrowShow, solid: rightArrowShow }">{{ nextBtn.text || '&nbsp;' }}</a>
  </div>
</template>

<script>
export default {
  props: {
    prevBtn: {
      type: Object,
      default () {
        return {
          text: '',
          disabled: false
        }
      }
    },
    nextBtn: {
      type: Object,
      default () {
        return {
          text: '',
          disabled: false
        }
      }
    },
    current: {
      type: Number,
      default: 1
    },
    total: {
      type: Number,
      default: 1
    }
  },
  computed: {
    rightArrowShow () {
      return this.current < this.total
    }
  },
  methods: {
    prev () {
      this.$emit('prev')
    },
    next () {
      this.$emit('next')
    }
  }
}
</script>
