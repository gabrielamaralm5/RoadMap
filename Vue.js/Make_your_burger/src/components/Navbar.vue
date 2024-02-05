<template lang="">
  <div id="Navbar">
    <nav>
      <router-link to="/"> <img :src="logo" :alt="alt" /> </router-link>
      <div clas="NavLink">
        <RouterLink to="/" class="a">Home</RouterLink>
        <RouterLink to="/pedidos" class="a">pedidos</RouterLink>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  props: ['logo', 'alt']
}
</script>

<style>
#Navbar {
  background-color: black;
  width: 100%;
  height: 15vh;
}
.navlink {
}
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  height: 100%;
  padding: 4%;
}
img {
  width: 40%;
}
.a {
  margin: 10%;
  color: orange;
  font-size: 1.3rem;
  text-decoration: none;
}
.a:hover{
  transition: .5s;
  color: white;
  text-decoration: underline;
}
</style>
