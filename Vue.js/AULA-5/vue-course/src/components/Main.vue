<template>
  <main>
    <section>
      <div>
        <input type="text" 
        v-model="text"
        placeholder="pesquise aqui...">
        <button type="submit">click</button>
        {{ text }}
      </div>
    </section>
  </main>
</template>

<script>
export default {
  data(){
    return{
      text:''
    }
  }
}
</script>

<style>
main {
  background-color: red;
}
</style>
