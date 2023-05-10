<template>
  <div id="app">
    <h1>YOUTUBE</h1>
    <iframe :src="`https://www.youtube.com/embed/${videoId}`" frameborder="0"></iframe>
    <p>{{ title }}</p>
  </div>
</template>

<script>
import axios from 'axios'

const YOUTUBE_URL='https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'App',
  data(){
    return{
      videoId:null,
    }
  },
  methods: {
    getVideo(){
    }
  },
  created(){
    axios({
      method:'get',
      url: YOUTUBE_URL,
      params : {
        key: process.env.API_KEY,
        part: 'snippet',
        type: 'video',
        q : '코딩노래'
      }
    })
    .then((response)=> {
      this.videoId = response.data.items[0].id.videoId
      this.title = response.data.items[0].snippet.title
    })
    .catch((err) => console.log(err))
  }
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap");
#app {
  font-family: 'Poppins';
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
