<template>
  <Navbar :logo="logo_src" :alt="alt_src" />
  <RouterView />
  
</template>

<script>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'

export default {
  components: {
    Navbar,
    Footer,
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
  width: 100vw;
  height: 100vh;
  background-color: aliceblue;
  display: flex;
  color: black;
  flex-direction: column;
  
}

.main-container h1{
  display: flex;
  justify-content: center;
  margin: 20px;
}
</style>
