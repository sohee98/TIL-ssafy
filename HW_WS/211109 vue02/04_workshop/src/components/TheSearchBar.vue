<template>
  <div class='search-bar'>
    <input type="text" @keyup.enter='onInputData'>
  </div>
</template>

<script>
export default {
  name: 'TheSearchBar',
  methods:{
    onInputData: function (event) {
      this.$emit('input-change', event.target.value)
    }
  }
}
</script>

<style>
.search-bar > input {
  width: 100%;      
  padding: 0.5rem;
  font-size: 2rem;
}
.search-bar {
  transition-duration: 0.5s;
}
</style>