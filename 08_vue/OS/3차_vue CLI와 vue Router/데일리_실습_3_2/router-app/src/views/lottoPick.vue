<template>
  <div>
    <h1>로또</h1>
    <button @click="getNumber">Get Lucky Numbers</button>
    <p>{{ numbers }}</p>
  </div>
</template>

<script>
export default {
  name:'lottoPick',
  data(){
    return{
      numbers:'',
    }
  },
  methods:{
    getNumber(){
      const _ = require('lodash')
      this.numbers=_.sampleSize(_.range(1,46),6)
    }
  }
}
</script>

<style>

</style>