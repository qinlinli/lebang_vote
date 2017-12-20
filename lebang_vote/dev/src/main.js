import 'font-awesome/css/font-awesome.css'
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Axios from 'axios'
import App from './App'
import router from './router'
import * as utils from './utils'
import Toast from './utils/toast.js'
import * as filter from './utils/filter.js'

Vue.config.productionTip = false

Vue.prototype.$toast = Toast
Vue.prototype.$axios = Axios
Vue.prototype.$utils = utils
/* eslint-disable no-new */
Object.keys(filter).forEach(k => {
  Vue.filter(k, filter[k])
})

new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
