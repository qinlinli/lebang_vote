const toast = (obj) => {
  const oo = {}
  if (typeof obj === 'object') {
    oo.msg = obj.msg || '网络出现错误，请稍后重试'
    oo.timer = obj.time || 2000
    oo.type = obj.type
  } else {
    oo.msg = obj || '网络出现错误，请稍后重试'
    oo.timer = 2000
  }
  var toast = document.getElementById('toast')
  if (!toast) {
    toast = document.createElement('div')
    toast.setAttribute('id', 'toast')
    toast.className = 'ev-toast'
    document.body.appendChild(toast)
  } else {
    toast.style.display = 'block'
  }
  toast.innerHTML = '<div class="ev-toast-msg"><i class="' + oo.type + '"></i>' + oo.msg + '</div>'
  setTimeout(() => {
    toast.style.display = 'none'
  }, oo.timer)
}

export default toast
