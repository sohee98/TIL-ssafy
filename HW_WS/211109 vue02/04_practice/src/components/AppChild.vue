<template>
  <div>
    <h1>AppChild</h1>
    <input type="text" @input='onChildInputChange'>
    <p>appData : {{ appData }}</p>
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
  </div>
</template>

<script>
export default {
  name: 'AppChild',
  props: {
    appData: {
      type: String
    },
    parentData: {
      type: String
    },
    childData: {
      type: String
    },
  },
  methods: {
    onChildInputChange: function (event) {
      this.$emit('app-child-change', event.target.value)
    } 
  }
  
}
</script>

<style>

</style>