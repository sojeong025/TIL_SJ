import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    number: 0,
  },
  getters: {
    doubleCounter(state){
      return state.number * 2
    }
  },
  mutations: {
    INCREASE(state, increaseNumber){
      state.number = increaseNumber
    },
    DECREASE(state, decreaseNumber){
      state.number = decreaseNumber
    }
  },
  actions: {
    increase(context, number){
      context.commit('INCREASE', number+1)
    },
    decrease(context, number){
      context.commit('DECREASE', number-1)
    }
  },
  modules: {
  }
})
