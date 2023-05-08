<template>
  <div>
    <ul>
      <AnimalCard
      v-for="image in images"
      :key="image.id"
      :image="image"
      />
    </ul>
  </div>
</template>

<script>
import AnimalCard from './AnimalCard.vue'
export default {
  name:'AnimalImages',
  components: {
    AnimalCard
  },
  computed: {
    images(){
      return this.$store.state.images
    }
  }

}
</script>

<style>

</style>