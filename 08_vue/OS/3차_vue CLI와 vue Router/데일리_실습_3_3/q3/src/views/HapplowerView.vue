<template>
  <div class="happlower">
    <h2>3단계</h2>
    <div class="container">
      <font-awesome-icon @click="alert" class="icon" icon="fa-solid fa-circle-chevron-left" />
      <img class="img" src="@/assets/happlower.png" alt="">
      <font-awesome-icon @click="goToHome" class="icon" icon="fa-solid fa-circle-chevron-right" />
    </div>
    <h2>해플라워</h2>
  </div>
</template>

<script>

export default {
  name:'HapplowerView',
  methods: {
    goToHome(){
      this.$router.push({name:'home'})
      alert('홈으로 돌아갑니다')
    },
    alert(){
      alert('전 단계로 돌아갈 수 없음')
    }
  }
}

</script>

<style>
.happlower{
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