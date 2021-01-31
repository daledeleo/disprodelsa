'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  API:`${process.env.VUE_APP_BASE_URL}`,
  USERNAME:`${process.env.VUE_APP_USERNAME}`,
  PASSWORD:`${process.env.VUE_APP_PASSWORD}`,
})
