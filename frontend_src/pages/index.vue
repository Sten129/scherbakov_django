<template lang="pug">
  .container
    Tutorial
    pre(v-show="loaded") {{ $t('wording.name') }}: {{ name }}
    .loading(v-show="!loaded") Loading...
</template>

<script lang="ts">
import Vue from 'vue'

export default Vue.extend({
  name: 'IndexPage',
  async asyncData({ $axios }) {
    const persons = await $axios.$get('http://web:8000/api/persone/?format=json')
    return {
      loaded: true,
      persons,
      name: persons.results[0].name
     }
  }
})
</script>
