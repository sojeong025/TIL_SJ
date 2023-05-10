<template>
  <div class="lunch">
    <h1>점심메뉴</h1>
    <button @click="getLunch">Pick Lunch</button>
    <p>{{ lunch }}</p>

    <br>
    <h2>로또를 뽑아보자</h2>
    <button @click="goToLotto">Pick Lotto</button>
  </div>
</template>

<script>
export default {
  name:'lunchMenu',
  data() {
    return{
      lunch:'',
    }
  },
  methods:{
    goToLotto(){
      this.$router.push({name:'lotto'})
    },
    getLunch(){
      const _ = require('lodash')
      const menu = ['고기', '햄버거', '국밥', '치킨', '피자']
      this.lunch = _.sample(menu)
    }
  },
}
</script>

<style>

</style>