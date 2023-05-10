<template>
  <div class="happling">
    <h2>1단계</h2>
    <div class="container">
      <font-awesome-icon @click="alert" class="icon" icon="fa-solid fa-circle-chevron-left" />
      <img class="img" src="@/assets/happling.png" alt="">
      <font-awesome-icon @click="goToHapplossome" class="icon" icon="fa-solid fa-circle-chevron-right" />
    </div>
    <h2>해플링</h2>
  </div>
</template>

<script>

export default {
  name:'HapplingView',
  methods:{
    goToHapplossome(){
      this.$router.push({name:'HapplossomeView'})
    },
    alert(){
      alert('전 단계로 돌아갈 수 없음')
    }
  }
}
</script>

<style>
.happling{
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