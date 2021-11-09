<template>
  <div v-if="video">
    <iframe :src="videoUrl" frameborder="0"></iframe>
    <hr>
    <h2>{{ video.snippet.title }}</h2>
    <p>{{ video.snippet.description }}</p>
  </div>
</template>

<script>
export default {  
  name: 'VideoDetail',
  props: {
    video: {
      type: Object,
    }
  },
  computed: {
    videoUrl: function () {
      const videoId = this.video.id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    }
  }
}
</script>

<style>

</style>