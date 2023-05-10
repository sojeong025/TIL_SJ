<template>
  <div class="happeed">
    <h2>시작</h2>
    <div class="container">
      <font-awesome-icon @click="goToHome" class="icon" icon="fa-solid fa-circle-chevron-left" />
      <img class="img" src="@/assets/happeed.png" alt="">
      <font-awesome-icon @click="goToHappling" class="icon" icon="fa-solid fa-circle-chevron-right" />
    </div>
    <h2>해피드</h2>
  </div>
</template>

<script>

export default {
  name:'HappeedView',
  methods:{
    goToHome(){
      this.$router.push({name:'home'})
    },
    goToHappling(){
      this.$router.push({name:'HapplingView'})
    }
  }
}
</script>

<style>
.happeed{
  width: 500px;
  height: 500px;
  box-shadow: 0px 3px 7px gray;  
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: auto;
}
.img {
  width: 350px;
  height: 300px;
}
.container {
  display: flex;
  align-items: center;
}
.icon {
  width: 30px;
  height: 30px;
  cursor: pointer;
}
</style>