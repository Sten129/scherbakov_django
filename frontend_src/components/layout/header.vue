<template lang="pug">
  .container
    .flex.w-full.justify-between
      nav
        nuxt-link(:to="localePath('index')") Home
      LayoutLangs
</template>

<script>
export default {
  computed: {
    availableLocales () {
      return this.$i18n.locales.filter(i => i.code !== this.$i18n.locale)
    }
  }
}
</script>
