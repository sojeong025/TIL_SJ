<template>
  <div id="app">
    <p ref="test">Counter : {{number}}</p>
    <p>Double counter : {{doubleCounter}}</p>
    <button @click="increase">increase +</button>
    <button @click="decrease">decrease -</button>

  </div>
</template>

<script>


export default {
  name: 'App',
  computed: {
    number(){
      return this.$store.state.number
    },
    doubleCounter(){
      return this.$store.getters.doubleCounter
    },
  },
  methods: {
    increase(){
      this.$store.dispatch('increase', this.$store.state.number)
    },
    decrease(){
      this.$store.dispatch('decrease', this.$store.state.number)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
