<template>
  <header>
    <div v-if="hours == 'bom-dia'">bom dia {{ name }}</div>
    <div v-if="hours == 'boa-tarde'">boa tarde {{ name }}</div>
    <div v-if="hours == 'boa-noite'">boa noite {{ name }}</div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      name: 'gabriel',
      showname: true,
      hours: 'bom-dia'
    }
  }
}
</script>
<style>
header {
  background-color: black;
  color: white;
}
</style>
