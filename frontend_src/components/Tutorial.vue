<!-- Please remove this file from your project -->
<template lang="pug">
  .relative.flex.items-top.justify-center.min-h-screen.bg-gray-100(class="sm:items-center sm:pt-0")
    .max-w-4xl.mx-auto(class="sm:px-6 lg:px-8")
      h1.text-2xl.leading-7.font-semibold
        span {{ $t('wording.language') }}
      nuxt-link(
        class="block"
        v-for="locale in availableLocales"
        :key="locale.code"
        :to="switchLocalePath(locale.code)") {{ locale.code }}
      nuxt-link(:to="localePath('index')") link to home page
</template>

<script>
export default {
  name: 'NuxtTutorial',
  computed: {
    availableLocales () {
      return this.$i18n.locales.filter(i => i.code !== this.$i18n.locale)
    }
  }
}
</script>

<style lang="postcss">
  h1 {
    @apply relative text-white;
    @apply before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-pink-500 relative inline-block;
  }

  h1 span {
    @apply relative;
    z-index: 2;
  }
</style>