<template lang="pug">
  .container
    .flex.w-full.justify-between
      nav
        nuxt-link(:to="localePath('index')") {{ $t('menu.home') }}
        nuxt-link(:to="localePath('pictures')") {{ $t('menu.pictures') }}
        a(href="#") {{ $t('menu.exhibitions') }}
        a(href="#") {{ $t('menu.books') }}
        a(href="#") {{ $t('menu.people') }}
        a(href="#") {{ $t('menu.documents') }}
        a(href="#") {{ $t('menu.letters') }}
        a(href="#") {{ $t('menu.provenance') }}
        a(href="#") {{ $t('menu.articles') }}
        a(href="#") {{ $t('menu.biography') }}

      LayoutLangs

</template>

<script>
export default {

}
</script>

<style lang="postcss" scoped>
  a {
    @apply p-2;
  }

  .nuxt-link-exact-active {
    @apply text-pink-500;
  }

</style>