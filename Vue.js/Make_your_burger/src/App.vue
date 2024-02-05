<template>
  <Navbar :logo="logo_src" :alt="alt_src" />
  <RouterView />
  <Footer />
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

export default {
  components: {
    Navbar,
    Footer
  },
  data() {
    return {
      logo_src: '/img/logo.png',
      alt_src: 'make your burge'
    }
  }
}
</script>

<style>
.main-container {
  width: 100%;
  height: 100vh;
  background-color: aliceblue;
  display: flex;
  justify-content: center;
  color: black;
  
}
</style>
