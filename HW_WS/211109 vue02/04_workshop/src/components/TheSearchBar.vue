<template>
  <div>
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

</style>