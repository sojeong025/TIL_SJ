<template>
  <div>
    <input type="text" @keyup.enter="searchInput">
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods : {
    searchInput(event) {
      this.$emit('search-data', event.target.value)
    }
  }
}
</script>

<style>

</style>