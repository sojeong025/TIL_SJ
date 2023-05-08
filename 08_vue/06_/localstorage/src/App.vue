<template>
  <div id="app">
    <button class="myButton" @click="getCatImage">getCat</button>
    <button class="myButton" @click="getDogImage">getDog</button>
    <AnimalImages/>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import AnimalImages from "@/components/AnimalImages.vue"

export default {
  name: 'app',
  components: {
    AnimalImages,
  },
  methods: {
    getCatImage() {
      this.$store.dispatch('getCatImage')
    },
    ...mapActions(['getDogImage']),
  },
}
</script>

<style>
#app {
  display: flex;
  justify-content: center;
  margin-top: 60px;
}
.myButton {
  background-color: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  text-transform: uppercase;
  letter-spacing: 1px;
  cursor: pointer;
  border-radius: 20px;
}
</style>
