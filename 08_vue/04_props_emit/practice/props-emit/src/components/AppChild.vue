<template>
  <div>
    <h1>App Child</h1>
    <input type="text" v-model="childData" @input="onChildInputData">
      <p>appData : {{ appData }} </p>
      <p>parentData : {{ parentData }}</p>
      <p>childData : {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name:'AppChild',
  props:{
    appData: String,
    parentData: String,
  },
  data() {
    return {
      childData: ''
    }
  },
  methods : {
    onChildInputData(){
      // 내가 특정한 type의 이벤트가 발생하도록 만들 수 있다
      // this.$emit(발생시킬 이벤트 명(문자열), 함께 전달할 데이터)
      this.$emit('child-input-change', this.childData)
    }
  }
}
</script>

<style>

</style>