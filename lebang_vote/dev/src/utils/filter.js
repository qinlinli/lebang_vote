import * as utils from './index.js'

export function date (str, format) {
  return utils.fmtDate(new Date(str), format)
}

export function sortByCh (array, string, reverse) {
  return utils.sortByCh(array, string, reverse)
}

export function filterArray (array, keyword) {
  return utils.filterArray(array, keyword)
}
