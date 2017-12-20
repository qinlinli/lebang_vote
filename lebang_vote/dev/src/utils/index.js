/**
 * Created by ushio on 2017/11/23.
 */
import toast from './toast.js'

/** 本地静态字典 **/
export const EFFECTIVE_TIME = [
  {
    value: 'current',
    text: '本月生效'
  },
  {
    value: 'next',
    text: '下月生效'
  }
]

export const SOCIAL_ROUNDING_MODE = {
  'rounding_to_fen': '四舍五入到分',
  'rounding_to_jiao': '四舍五入到角',
  'rounding_to_yuan': '四舍五入到元',
  'ceil_to_jiao': '见分进角',
  'ceil_to_yuan': '见角进元',
  'ignore_fraction': '舍弃小数',
  'rounding_0_or_5': '加1或2后取整0或5'
}

export const SOCIAL_RULE = {
  'fixed': '固定值',
  'salary': '基本工资',
  'salary+performance': '基本工资+绩效工资'
}

/** 类型判断方法 **/
export function isArray (arr) {
  return isType(arr, 'Array')
}

export function isObject (obj) {
  return isType(obj, 'Object')
}

export function isFunction (fn) {
  return isType(fn, 'Function')
}

export function isEmpty (obj) {
  if (!obj) {
    return true
  }
  if (isArray(obj) && obj.length === 0) {
    return true
  }
  if (isObject(obj) && Object.keys(obj).length === 0) {
    return true
  }
  return false
}

export function isType (obj, type) {
  return Object.prototype.toString.call(obj) === '[object ' + type + ']'
}

/** 表单校验方法 **/
export function validateLength (prop, length, message, callback) {
  if (prop.length > length) {
    if (message) {
      toast(`长度不能超过${length}字！`)
    }
    callback && callback()
    return false
  }
  if (prop.length <= 0) {
    if (message) {
      toast(message)
    }
    callback && callback()
    return false
  }
  return true
}

/** 日期格式化 **/
export function fmtDate (date, fmt) {
  let reg = /^\d{4}(-|[\u4e00-\u9fa5])\d{1,2}(-|[\u4e00-\u9fa5])\d{1,2}/
  if (reg.test(date)) {
    date = new Date(date.replace(/-|[\u4e00-\u9fa5]/g, '/'))
  }
  date = new Date(date)
  let o = {
    'M+': date.getMonth() + 1, // 月份
    'd+': date.getDate(), // 日
    'h+': date.getHours(), // 小时
    'm+': date.getMinutes(), // 分
    's+': date.getSeconds(), // 秒
    'q+': Math.floor((date.getMonth() + 3) / 3), // 季度
    'S': date.getMilliseconds() // 毫秒
  }
  if (/(y+)/.test(fmt)) {
    fmt = fmt.replace(RegExp.$1, (date.getFullYear() + '').substr(4 - RegExp.$1.length))
  }
  for (var k in o) {
    if (new RegExp('(' + k + ')').test(fmt)) {
      fmt = fmt.replace(RegExp.$1, (RegExp.$1.length === 1) ? (o[k]) : (('00' + o[k]).substr(('' + o[k]).length)))
    }
  }
  return fmt
}

/** 排序方法 **/
export function sortBy (array, string, reverse = false) {
  let arr = []
  arr = array.sort((a, b) => {
    return a[string] <= b[string] ? 1 : -1
  })
  return reverse ? arr.reverse() : arr
}

export function sortByCh (array, string, reverse = false) {
  let arr = []
  arr = array.sort(function (a, b) {
    return typeof String.prototype.localeCompare === 'function' ? a[string].localeCompare(b[string]) : array
  })
  return reverse ? arr.reverse() : arr
}

/** 过滤方法 **/
export function filterArray (array, keyword) {
  let arr = []
  array.forEach((item) => {
    if (item.includes(keyword)) {
      arr.push(item)
    }
  })
  return arr.length === 0 ? array : arr
}

/** editable方法 **/
export function updateEditableView (row, result) {
  row.id = result.id
  row.params = result
  row.columns.forEach((col) => {
    if (col.type === 'select') {
      col.value = col.multiple ? col.model.text.join(',') : col.model.text
    } else {
      col.value = col.model
    }
  })
}

export function formatEditableParams (col) {
  let param = ''
  if (col.type === 'select') {
    param = col.model.value
  } else {
    param = col.model
  }
  return param
}

/** 弹窗方法 **/
export function openModal (context, ref) {
  context.$refs[ref].$el.classList.remove('hide')
  setTimeout(() => {
    context.$refs[ref].$el.classList.remove('fade')
  }, 200)
}

/** dom操作 **/
export function prevSibling (node) {
  if (!node) {
    return
  }
  return node.previousElementSibling || node.previousSibling
}

export function nextSibling (node) {
  if (!node) {
    return
  }
  return node.nextElementSibling || node.nextSibling
}

export function parent (node, selector) {
  if (!node || !selector) {
    return
  }
  let target = node
  if (selector.indexOf('#') > -1) {
    while (target.parentNode.id !== selector.slice(1)) {
      target = target.parentNode
    }
  } else if (selector.indexOf('.') > -1) {
    while (target.parentNode.classList.contains(selector.slice(1))) {
      target = target.parentNode
    }
  } else {
    while (target.parentNode.tagName.toLowerCase() !== selector) {
      target = target.parentNode
    }
  }
  return target.parentNode
}

export function prev (node, selector) {
  if (!node || !selector) {
    return
  }
  let target = node
  if (selector.indexOf('#') > -1) {
    while (prevSibling(target).id !== selector.slice(1)) {
      target = prevSibling(target)
    }
  } else if (selector.indexOf('.') > -1) {
    while (prevSibling(target).classList.contains(selector.slice(1))) {
      target = prevSibling(target)
    }
  } else {
    while (prevSibling(target).tagName.toLowerCase() !== selector) {
      target = prevSibling(target)
    }
  }
  return prevSibling(target)
}

export function next (node, selector) {
  if (!node || !selector) {
    return
  }
  let target = node
  if (selector.indexOf('#') > -1) {
    while (nextSibling(target).id !== selector.slice(1)) {
      target = nextSibling(target)
    }
  } else if (selector.indexOf('.') > -1) {
    while (target.parentNode.classList.contains(selector.slice(1))) {
      target = nextSibling(target)
    }
    while (nextSibling(target).classList.contains(selector.slice(1))) {
      target = nextSibling(target)
    }
  } else {
    while (nextSibling(target).tagName.toLowerCase() !== selector) {
      target = nextSibling(target)
    }
  }
  return nextSibling(target)
}

export function siblings (node, selector) {
  if (!node) {
    return
  }
  let el = node.previousSibling
  let siblings = []
  while (el) {
    if (node.nodeType === 1) {
      siblings.push(el)
    }
    el = el.previousSibling
  }
  el = node.nextSibling
  while (el) {
    if (node.nodeType === 1) {
      siblings.push(el)
    }
    el = el.nextSibling
  }
  return siblings
}
