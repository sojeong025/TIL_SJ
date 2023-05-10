<template>
  <div class="first">
    <img alt="Vue logo" src="../assets/logo.png">
    <HelloWorld msg="첫번째 페이지입니다"/>
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'

export default {
  name: 'HomeView',
  components: {
    HelloWorld
  }
}
</script>
