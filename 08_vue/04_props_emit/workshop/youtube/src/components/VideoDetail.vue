<template>
<div v-if="video">
  <h2>Video Detail</h2>
  <iframe :src='videoURI' frameborder="0"></iframe>
</div>
</template>

<script>
export default {
  props:{
    video:Object,
  },
  computed:{
    videoURI(){
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>