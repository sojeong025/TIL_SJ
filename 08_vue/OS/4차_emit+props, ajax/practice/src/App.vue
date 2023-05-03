<template>
  <div id="app">
    
    <!-- vue-directive -->
    <!-- 내 element에 어떤 data를 바인딩 하는 방법 -->
    <!-- v-bind:변수명="JS 표현식" -->
    <HelloWorld :msg="message"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data() {
    return {
      message: '안녕 친구들'
    }
  },
  components: {
    HelloWorld
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
