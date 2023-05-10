<template>
  <div class="happlossome">
    <h2>2단계</h2>
    <div class="container">
      <font-awesome-icon @click="alert" class="icon" icon="fa-solid fa-circle-chevron-left" />
      <img class="img" src="@/assets/happlossome.png" alt="">
      <font-awesome-icon @click="goToHapplower" class="icon" icon="fa-solid fa-circle-chevron-right" />
    </div>
    <h2>해플라썸</h2>
  </div>
</template>

<script>

export default {
  name:'HapplossomeView',
  methods: {
    goToHapplower(){
      this.$router.push({name:'HapplowerView'})
    },
    alert(){
      alert('전 단계로 돌아갈 수 없음')
    }
  }
}
</script>

<style>
.happlossome{
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