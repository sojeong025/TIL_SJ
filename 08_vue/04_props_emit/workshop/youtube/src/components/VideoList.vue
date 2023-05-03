<template>
<div>
  <h2>Video List</h2>
  <ul>
    <VideoListItem v-for="video in videos" :key="video.id.videoId" :video="video"
    @select-video="SelectVideo"/>
  </ul>
</div>
</template>

<script>
import VideoListItem from '@/components/VideoListItem'
export default {
  name:'VideoList',
  components:{
    VideoListItem,
  },
  props:{
      videos:Array,
  },
  methods:{
    SelectVideo(video){
      this.$emit('select-video',video)
    }
  }
}

</script>

<style>

</style>