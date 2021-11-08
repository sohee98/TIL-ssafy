<template>
  <div @click="selectVideo">
    <img 
      :src="video.snippet.thumbnails.default.url" 
      alt="youtube thumbnail"
    >
    {{ video.snippet.title }}
  </div>
</template>

<script>
export default {
  name: 'VideoListItem',
  props: {
    video: {
      type: Object,
      required: true,
    }
  },
  methods: {
    selectVideo: function () {
      this.$emit('select-video', this.video)
    }
  }
}
</script>

<style>

</style>
