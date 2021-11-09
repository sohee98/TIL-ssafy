<template>
  <div id="app">
    <!-- <p>click: 
      <hello-world @click="onClick"></hello-world>
    </p>
    <p>click.native: 
      <hello-world @click.native="onClick"></hello-world>
    </p> -->

    <h1>APP</h1>
    <input type="text" v-model='appData'>
    <!-- <p>appData : {{ appData }}</p> -->
    <p>parentData: {{ parentData }}</p>
    <p>childData: {{ childData }}</p>
    <hr>
    <app-parent
      :app-data='appData'
      :parent-data='parentData'
      :child-data='childData'
      @app-parent-change="onParentChange"
      @app-child-change="onChildChange"
    >
    </app-parent>
  </div>
</template>

<script>
import AppParent from '@/components/AppParent'
// import HelloWorld from '@/components/HelloWorld'


export default {
  name: 'App',
  components: {
    AppParent,
    // HelloWorld
  },
  data: function () {
    return {
      appData: null,
      parentData: null,
      childData: null,
    }
  },
  methods: {
    onParentChange: function (parentInputValue) {
      this.parentData = parentInputValue
    },
    onChildChange: function (childInputValue) {
      this.childData = childInputValue
    },
    onClick: function () {
      console.log('Hello!')
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
