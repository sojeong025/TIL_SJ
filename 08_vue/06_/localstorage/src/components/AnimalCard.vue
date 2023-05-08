<template>
  <div>
    <p
    :class="{
      'cat': image.status === 'cat',
      'dog': image.status === 'dog'
    }">
    {{image.status}}
    <img :src="image.url" alt="">
    
    </p>
  </div>
</template>

<script>
export default {
  name:'AnimalCard',
  props: {
    image:Object,
  }
}
</script>

<style>
.cat {
  color:red;
}
.dog {
  color: blue;
}
.image {
  margin: 20px;
  text-align: center;
}
</style>