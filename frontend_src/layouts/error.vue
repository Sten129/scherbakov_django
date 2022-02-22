<template lang="pug">
  .container
    h2 Error
    h2(v-if="error.statusCode === 404") 404
    h2(v-else) {{ error.statusCode }}
</template>

<script lang="ts">
import Vue from "vue"

export default Vue.extend({
  name: 'Error',
  props: {
    error: { type: Object, default: null }
  }
})
</script>
