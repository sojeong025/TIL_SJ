<template>
  <li @click='selectVideo'>
    <img :src="video.snippet.thumbnails.default.url" alt="">
    {{video.snippet.title}}
  </li>
</template>

<script>
export default {
  name:'VideoListItem',
  props:{
    video:Object,
  },
  methods:{
    selectVideo(){
      this.$emit('select-video', this.video)
    }
  }

}
</script>

<style>

</style>