<template>
  <div id="app">
    <h1>My first youtube project</h1>
    <TheSearchBar
      @search-data="searchInput"/>
    <VideoDetail :video="selectedVideo"/>
    <VideoList :videos="videos" @select-video="SelectVideo"/>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = 'AIzaSyDdEafSYJoXdBmVqV0Z7oll3O_yucres-0'

import TheSearchBar from '@/components/TheSearchBar.vue'
import VideoDetail from '@/components/VideoDetail.vue'
import VideoList from '@/components/VideoList.vue'

export default {
  name:'App',
  components:{
    TheSearchBar,
    VideoDetail,
    VideoList,
  },
  data(){
    return {
      inputValue: null,
      videos:[],
      selectedVideo: null,
    }
  },
  methods: {
    SelectVideo(video){
      this.selectedVideo=video
    },
    searchInput(inputText){
      this.inputValue=inputText
      const params = {
        key:API_KEY,
        part:'snippet',
        type:'video',
        q:this.inputValue,
      }
      axios({
        method:'get',
        url:API_URL,
        params,
      })
      .then(res => {
        this.videos = res.data.items
        console.log(res.data.items)
      })
      .catch(error => {
        console.log(error)
      })
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