<script>
import Banner from '@/components/Banner.vue'
import FormBuger from '@/components/FormBuger.vue'

export default {
  name: 'Home',
  components: {
    Banner,
    FormBuger,
  }
}
</script>

<template>
  <Banner />
  <main class="main-container">
    <h1>Monte o Seu Burger:</h1>
    <FormBuger />
  </main>
</template>

<style></style>
