<template lang="pug">
  .container
    pre(v-show="loaded") {{ $t('wording.name') }}: {{ name }}
    .loading(v-show="!loaded") Loading...
</template>

<script lang="ts">
import Vue from "vue"

export default Vue.extend({
  async asyncData({ $axios }) {
    const persons = await $axios.$get('/persons/?format=json').then((result) => {
      return result
    }).catch((error) => {
      console.log(error)
    })
    return {
      loaded: true,
      persons,
      name: persons?.results[0].name
    }
  }
})
</script>
