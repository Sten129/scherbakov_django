<template lang="pug">
  .container Pictures
    pre {{ pictures }}
</template>

<script lang="ts">
import Vue from "vue"

export default Vue.extend({
  async asyncData({ $axios }) {
    const pictures = await $axios.$get('/picture/?format=json').then((result) => {
      return result
    }).catch((error) => {
      console.log(error)
    })
    return {
      loaded: true,
      pictures,
      list: pictures
    }
  }
})
</script>
