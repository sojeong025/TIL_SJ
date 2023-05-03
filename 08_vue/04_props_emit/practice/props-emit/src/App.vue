<template>
  <div id="app">
    <h1>APP</h1>
    <!--input에 입력되는 값을 appData에 바인딩해서 화면에 보이도록 하고 싶다-->
    <!--양방향 바인딩을 해주는 directive v-model-->
    <!--input의 value와 vue의 data 중, 특정 속성을 양방향으로 묶어버린다-->
    <input type="text" v-model="appData">
      <p>Appdata: {{ appData }}</p>
      <p>parentData: {{ parentData }}</p>
      <p>childData: {{ childData }}</p>
      <!--내가 가진 데이터를 prop 시켜주자-->
      <!--dynamic prop -> v-bind를 써서 하위 컴포넌트에 어떠한 값을 넘겨준다-->
      <!--이때 이름은 kebob case로 짓는다-->
    <AppParent
      @parent-input-change="onParentInputData"
      @child-input-change="onChildInputData"
      :app-data="appData"
    />
  </div>
</template>

<script>
import AppParent from './components/AppParent.vue'

export default {
  name: 'App',
  components: {
    AppParent,
  },
  data(){
    return{
      appData:'',
      parentData:'',
      childData:'',
    }
  },
  methods:{
    onChildInputData(childInputData){
      this.childData= childInputData
    },
    onParentInputData(parentInputData) {
      this.parentData=parentInputData
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
