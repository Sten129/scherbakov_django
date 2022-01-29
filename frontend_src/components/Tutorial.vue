<!-- Please remove this file from your project -->
<template>
  <div class="relative flex items-top justify-center min-h-screen bg-gray-100 sm:items-center sm:pt-0">
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.1.2/dist/tailwind.min.css" rel="stylesheet">
    <div class="max-w-4xl mx-auto sm:px-6 lg:px-8">
      <h1 class="text-2xl leading-7 font-semibold">{{ $t('wording.language') }}</h1>
      <nuxt-link
        class="block"
        v-for="locale in availableLocales"
        :key="locale.code"
        :to="switchLocalePath(locale.code)">{{ locale.code }}</nuxt-link>
      <nuxt-link :to="localePath('index')">link to home</nuxt-link>
    </div>
  </div>
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
