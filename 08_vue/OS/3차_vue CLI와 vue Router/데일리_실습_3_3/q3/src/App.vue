<template>
  <div id="app">
    <nav>
      <h1>캐릭터 진화 단계 가이드</h1>
      <button class="button" @click="goToHome">Home</button>
      <button class="button" @click="goToHappeed">Start</button>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default{
  name:'app',
  methods:{
    goToHome(){
      if(this.$route.name != 'home'){
        this.$router.push({name:'home'})
      }
    },
    goToHappeed(){
      this.$router.push({name:'HappeedView'})
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
}
.button {
  border: 2px solid #F1A324;
  background-color: white;
  font-size: 1.25rem;
  border-radius: 15px;
  width: 100px;
  height: 60px;
  margin: 20px;
  cursor: pointer;

}
.button:hover {
  background-color: #F7E43A;
}
nav {
  padding: 30px;
}
</style>
