import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'
const DOG_API_URL = 'https://api.thedogapi.com/v1/images/search'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    images: []
  },
  getters: {
  },
  mutations: {
    GET_IMAGE(state, payload) {
      state.images.push(payload)
    }
  },
  actions: {
    getCatImage({commit}){
      axios({
        method:'get',
        url:CAT_API_URL,
      })
      .then(res => {
        const payload = {
          id: new Date().getTime(),
          url: res.data[0].url,
          status: 'cat'
        }
        commit('GET_IMAGE', payload)
      })
      .catch(err => console.log(err))
    },
    getDogImage({commit}){
      axios({
        method:'get',
        url:DOG_API_URL,
      })
      .then(res => {
        const payload = {
          id: new Date().getTime(),
          url: res.data[0].url,
          status: 'dog'
        }
        commit('GET_IMAGE', payload)
      })
      .catch(err => console.log(err))
    }
  },
  modules: {
  }
})
