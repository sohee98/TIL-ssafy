<template>
  <div>
    <h1>AppParent</h1>
    <input type="text" @input='onParentInputChange'>
    <p>appData : {{ appData }}</p>
    <p>childData: {{ childData }}</p>
    <hr>
    <app-child
      :app-data='appData'
      :parent-data='parentData'
      :child-data='childData'  
      @app-child-change='onChildInputChange'
    >
    </app-child>
  </div>
</template>

<script>
import AppChild from './AppChild'

export default {
  name: 'AppParent',
  components: {
    AppChild
  },
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
    onParentInputChange: function (event) {
      this.$emit('app-parent-change', event.target.value)
    },
    onChildInputChange: function (childInputValue) {
      this.childData = childInputValue
      this.$emit('app-child-change', childInputValue)
    }

  }
}
</script>

<style>

</style>