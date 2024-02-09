<template lang="">
  <div id="main-banner">
    <h1>Make your Burger</h1>
  </div>
</template>
<script>
export default {
  name: 'Banner'
}
</script>
<style scoped>
#main-banner {
  display: flex;
  align-items: center;
  width: 100%;
  height: 70vh;
  background: url(../../public/img/burger.jpg);
  background-size: cover;
  background-position: center center;
}

#main-banner h1 {
  background-color: #222;
  color: white;
  font-size: 4rem;
  font-variant: small-caps;
  padding: 3%;
  border-radius: 0px 12px 12px 0px;
}

#main-banner h1:hover {
  padding: 4%;
  background-color: #fff;
  color: #222;
  cursor: pointer;
}

</style>
